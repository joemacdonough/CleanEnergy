#!/bin/bash
while :
do
        output=$(who -a | grep +)
        epochtime=$(date +%s)
        filename="sessions-$epochtime"
        echo "$filename"
        #echo $output | ssh auth@100.64.2.85 cat > './logs/${filename}'
        echo $output | ssh auth@100.64.2.85 "cat > /home/auth/logs/${filename}"
        ssh auth@100.64.2.85 pwd
        sleep 30
done    

