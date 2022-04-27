import sys, os, glob, pdb
import numpy as np
import math
import pandas as pd
import rasterio, pprint
from pathlib import Path
import matplotlib.pyplot as plt

data_dir = "data/"
reference_tiff_paths = glob.glob(os.path.join(data_dir, "*_right_pos*_ref.tif"))

def onclick(event):
    global keep_app_alive, selected_ref_loc, selected_scan_loc
    global ref_point, scan_point

    try: # use try/except in case we are not using Qt backend
        zooming_panning = ( fig.canvas.cursor().shape() != 0 ) # 0 is the arrow, which means we are not zooming or panning.
    except:
        zooming_panning = False

    if not zooming_panning:
        if event.inaxes == axes[0]:
            pass
            print("Left side")
            selected_ref_loc = [event.xdata, event.ydata]
            #if ref_point is not None:
                #ref_point[0].remove()
            ref_point = axes[0].plot(event.xdata, event.ydata, marker='v', color="white")
        if event.inaxes == axes[1]:
            pass
            print("Right side")
            selected_scan_loc = [event.xdata, event.ydata]
            #if scan_point is not None:
                #scan_point[1].remove()
            scan_point = axes[1].plot(event.xdata, event.ydata, marker='v', color="white")
        #if event.xdata != None and event.ydata != None:
            #print(event.xdata, event.ydata)

def save_point():
    global current_ref_idx, current_scan_idx, scan_id
    global return_scan_paths, reference_tiff_paths
    global selected_ref_loc, selected_scan_loc

    #ref_tiff_path = reference_tiff_paths[current_ref_idx]
    return_scan_path = return_scan_paths[current_scan_idx]

    delta_x = selected_ref_loc[0] - selected_scan_loc[0]
    delta_y = selected_ref_loc[1] - selected_scan_loc[1]

    pp_scan = prettyPrintScanPath(return_scan_path)
    results_df.loc[return_scan_path] = [return_scan_path,
                                        pp_scan,
                                        pp_scan.split("_")[1],
                                        delta_x,
                                        delta_y]

def onkey(event):
    global keep_app_alive, selected_ref_loc, selected_scan_loc
    global results_df
    #axes[1].imshow(scan_tiff.read(1), cmap='plasma')
    #fig.canvas.draw()
    #fig.canvas.flush_events()
    if event.key == "n":
        print(f"onkey(): {event.key}")
        print(f"Saving REF:  {selected_ref_loc}")
        print(f"Saving SCAN: {selected_scan_loc}")
        if selected_ref_loc is None:
            print(f"You must select a reference point (left image)")
        elif selected_scan_loc is None:
            print(f"You must select a scan point (right image)")
        else:
            save_point()
            showNextScan()
    elif event.key == "k":
        print(f"KILL")
        keep_app_alive = False
    else:
        print(f"onkey(): {event.key}")

def showNextScan():
    global ref_tiff_path, ref_idx, scan_id, return_scan_paths, reference_tiff_paths
    global current_scan_idx, current_ref_idx

    if len(return_scan_paths) > (current_scan_idx+1):
        # Show next scan for current reference scan
        print("Show next scan for current reference scan")
        current_scan_idx += 1
        showCurrentScan()
    else:
        # Show next reference scan
        print("Show next reference scan")
        if len(reference_tiff_paths) > (current_ref_idx+1):
            current_scan_idx = 0
            current_ref_idx += 1
            showCurrentReference()
            showCurrentScan()
        else:
            print("Nothing left to show.")
            print("All done")
            keep_app_alive = False


def prettyPrintScanPath(scan_path):
    # Before:
    #   tif_outputs/685d3fc1-ae83-4e89-8daa-b8288e5a5290_right_pos2_test2.tif
    # After:
    #   right_pos2_test2
    #
    # take everything right of the slash
    # take everything right of the underscore
    # join with underscore
    # take everything before the period.
    return "_".join(scan_path.split("/")[1].split("_")[1:]).split(".")[0]

def showCurrentScan():
    global ref_tiff_path, current_ref_idx, current_scan_idx, scan_id
    global return_scan_paths, reference_tiff_paths, scan_point
    global selected_scan_loc

    selected_scan_loc = None

    print(f"showCurrentScan()")
    print(f"current_scan_idx:     {current_scan_idx}")
    print(f"return_scan_paths:    {return_scan_paths}")

    if scan_point is not None:
        scan_point[0].remove()

    fig.suptitle(f"Alignment Measurement Tool", fontsize=16)
    return_scan_path = return_scan_paths[current_scan_idx]
    scan_tiff = rasterio.open(return_scan_path)
    implot_right = axes[1].imshow(scan_tiff.read(1), cmap='pink')
    axes[1].set_title(f"{prettyPrintScanPath(return_scan_path)}")
    fig.suptitle(f"Reference #{current_ref_idx+1}/{len(reference_tiff_paths)}\n\
                   Scan #{current_scan_idx+1}/{len(return_scan_paths)}")
    plt.draw()

def showCurrentReference():

    global ref_tiff_path, current_ref_idx, current_scan_idx, scan_id
    global return_scan_paths, reference_tiff_paths, ref_point
    global selected_ref_loc

    selected_ref_loc  = None

    print(f"current_ref_idx:      {current_ref_idx}")
    print(f"reference_tiff_paths: {reference_tiff_paths}")

    if ref_point is not None:
        ref_point[0].remove()

    ref_tiff_path = reference_tiff_paths[current_ref_idx]
    ref_tiff = rasterio.open(ref_tiff_path)
    implot_left = axes[0].imshow(ref_tiff.read(1), cmap='pink')
    axes[0].set_title(f"{prettyPrintScanPath(ref_tiff_path)}")
    #fig.suptitle(f"Reference #{current_ref_idx+1}/{len(reference_tiff_paths)}")
    fig.suptitle(f"Reference #{current_ref_idx+1}/{len(reference_tiff_paths)}\n\
                   Scan #{current_scan_idx+1}/{len(return_scan_paths)}")
    ref_filename = os.path.basename(ref_tiff_path)
    scan_id = ref_filename.split("_")[2]
    return_scan_paths = glob.glob(os.path.join(data_dir, f"*_right_{scan_id}_test*.tif"))

plt.close()

fig, axes = plt.subplots(1,2)

scan_id = ""
return_scan_paths = []
current_scan_idx = 0
current_ref_idx  = 0
selected_scan_loc = None
selected_ref_loc  = None
ref_point  = None
scan_point  = None
results_df = pd.DataFrame(columns = [ "return_scan_path",
                                      "scan_id",
                                      "pos",
                                      "delta_x",
                                      "delta_y",])


#fig.canvas.mpl_connect('button_press_event', onclick)
fig.canvas.mpl_connect('button_release_event', onclick)
fig.canvas.mpl_connect('key_release_event', onkey)
showCurrentReference()
showCurrentScan()
fig.show()

keep_app_alive = True
while keep_app_alive:
    plt.pause(0.5)

print("Left keep alive loop")
plt.close('all')

results_df.to_csv("results.csv")

plt.close('all')
fig = plt.figure(figsize=(8,8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)

colors = [plt.cm.tab20(i) for i,x in enumerate(results_df.pos.unique())]

for idx, pos in enumerate(results_df.pos.unique()):

    x = results_df[results_df.pos == pos].delta_x.values
    y = results_df[results_df.pos == pos].delta_y.values

    radii = [math.sqrt(x*x+y*y) for x,y in zip(x,y)]
    theta = [math.atan(y/x) for x,y in zip(x,y)]

    width = 0.1
    bars = ax.bar(theta, radii, width=width, bottom=0.0, color=colors[idx], label=pos, alpha=0.5)

#for r,bar in zip(radii, bars):
    #bar.set_facecolor( cm.jet(r/10.))
    #bar.set_alpha(0.5)

ax.legend()
plt.show()

## ZOOMING (deprecated)
# ysize = tiff1.read(1).shape[0]
# xsize = tiff1.read(1).shape[1]
#  Values to zoom in
# yquarter = int(ysize/4)
# y1 = yquarter
# y2 = y1 + yquarter*2
# xquarter = int(xsize/4)
# x1 = xquarter
# x2 = x1 + xquarter*2
# implot1 = axes[0].imshow(tiff1.read(1)[y1:y2,x1:x2], cmap='pink')

