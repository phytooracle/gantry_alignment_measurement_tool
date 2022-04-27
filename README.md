
<img align='right' width='40%' src='https://github.com/phytooracle/gantry_alignment_measurement_tool/raw/main/docs/assets/screen.png'><br>
<img align='right' width='40%' src='https://github.com/phytooracle/gantry_alignment_measurement_tool/raw/main/docs/assets/rose.png'>


This is not a good example of how to write code.

# Overview

This tool is used to measure how well the gantry returns to a known location. It was developed for use during testing of the gantry rewrite.

These are the basic steps...

1. Put bin/json files into a directory (e.g. `raw_data_from_gantry`)
1. Edit the bash file `convert_bin_to_tiff.bash` so that it knows where they are.
1. Run `. ./convert_bin_to_tiff.bash`
1. Run `python alignment_measurement_tool.py`

The Gui...

1. Click the point you want measured on the reference (left side) image.
1. Click the point you want measured on the return scan (right side) image.
1. Type `n` to proceed to the _next_ scan.
1. If you get to the last image, it will save the results to `results.csv`.  It will overwrite this file if it exists.
1. Type `k` to quit and save `results.csv` before reaching the end.  It will overwrite this file if it exists.

Pro Tip: You can use the keyboard shortcut `o` to turn on the "zoom to rectangle" cursor (croshairs) and then zoom in on the image.  Then press `o` again to return to the regular pointer (arrow) to click the location.

A few notes about the GUI...

1. The last point clicked is the one used.

