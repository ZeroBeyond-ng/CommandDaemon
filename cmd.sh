#!/bin/bash
now=$(date +"%T")
echo "Current time : $now"
for i in $(seq 10)
do
	echo "test seq number $i"
done

