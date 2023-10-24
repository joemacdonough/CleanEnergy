#!/bin/bash
while true; do
    output=$(who -a | grep +)
    epochtime=$(date +%s)
    filename="sessions-$epochtime"
    #echo "$filename"
    ssh user@ip echo $output > ./$filename
    sleep 180  # Sleep for 3 minutes (180 seconds)
done
