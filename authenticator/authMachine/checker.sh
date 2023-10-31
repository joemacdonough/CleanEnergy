#!/bin/bash
users=("auth" "john")
while :
do
	files=$(ls ./logs)
	result=$(python3 ./scan.py "${files}")
	if [ "$result" = "t" ]; then
		for user in ${users[@]}; do
			#ssh auth@100.64.1.93 "killall -u ${user}"
			echo $user
		done
	fi
	sleep 30
done
