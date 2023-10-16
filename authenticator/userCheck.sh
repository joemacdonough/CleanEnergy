#!/bin/bash
output=$(who -a | grep +)
epochtime=$(date +%s)
filename="sessions-$epochtime"
#echo "$filename"
ssh user@ip echo $output > ./$filename
