#!/bin/bash
source secrets.sh

while true; do
	python3 gamebanana-pages.py
	python3 gamebanana-itemizer.py
	git add --quiet gamebanana-items
	if python3 new-items-webhook.py ; then
		git commit -m "`date`"
	#else
		# nothing new right now...
	fi
	sleep 300
done
