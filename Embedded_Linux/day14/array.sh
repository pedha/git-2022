#!/bin/bash
index_array={1 2 3 4 5 6}
echo ${index_array[0]}
for i in ${index_array[@]}
do
	echo $i
done
echo "length of the array is : ${#index_array[@]}"
name[0]="Amit"
name[1]="Bhakti"
name[2]="Ashish"
name[3]="Gautam"
name[4]="Sayali"
echo "First Index value : ${name[0]}"
echo "All members of array : ${name[*]}"
echo "All members of array : ${name[@]}"
