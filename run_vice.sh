

conda env create -f ./gantry_alignment_tool_env.yml --force
bash convert_bin_to_tiff.bash 
python alignment_measurement_tool.py

