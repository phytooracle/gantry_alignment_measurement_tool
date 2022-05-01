
<img align='right' width='30%' src='https://github.com/phytooracle/gantry_alignment_measurement_tool/raw/main/docs/assets/screen.png'>
<img align='right' width='30%' src='https://github.com/phytooracle/gantry_alignment_measurement_tool/raw/main/docs/assets/rose.png'><br>

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

# Launching Vice Application
1. https://de.cyverse.org/
2. click apps on the left side
3. login on the top right
4. click apps under development in the dropdown on the top left
5. click gantry_alignment_measurement_tool
6. name analysis (this is the name of the folder where results.csv will be stored)
7. keep clicking next, and then hit launch analysis


# First time setup
9. click to go analysis in top left
10. git clone https://github.com/phytooracle/gantry_alignment_measurement_tool.git
11. cd gantry_alignment_measurement_tool/
12. sudo apt-get install vim (or other editor of your choice)
13. Edit the bash file `convert_bin_to_tiff.bash` so that it knows where your raw gantry data are
        - this boots having access to all of the data store so you allready have access to all data at /home/user/work/data/iplant/home/shared/phytooracle
14. bash setup_vice.sh
15. conda activate gantry



# Processing
15. bash run_vice.sh
16. process images using above instructions
17. when finished,
18. mv results.csv ~/work/data/output/
19. click disconnect in top left menue
20. the application will continue running with no output untiul you terminate it at https://de.cyverse.org/analyses by click the checkmark next to the analysis, and clicking terminate, you can then find the outputs in your personal de at ~/analyses/{analyses name}
21. this allows you to click the box with the arrow on that same page to go back into the application for three days, you can also click the timer icon to extend the active time

