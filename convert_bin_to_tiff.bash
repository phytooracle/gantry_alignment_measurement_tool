bins=(raw_data_from_gantry/04262022-test_data/*.bin)
jsons=(raw_data_from_gantry/04262022-test_data/*.json)
length_bins=${#bins[@]}
length_jsons=${#jsons[@]}
count=0
echo "-------------------------------------"
echo "About to process $length_bins bin files..."
echo "About to process $length_jsons json files..."
echo "-------------------------------------"
echo ""
for i in "${bins[@]}"
do
    echo $i
    echo ${jsons[$count]}
    ./rgb_bin_to_tif/rgb_bin2tif.py -o data/ -m ${jsons[$count]} $i
    let "count=count+1"
    echo "-------------------------------------"
done
