#!/bin/sh

while true; do
	python gamebanana-pages.py
	python gamebanana-itemizer.py
	git add gamebanana-items
	if ! python new-items-webhook.py; then
		git commit -m `date`
	else
		# nothing new right now...
	fi
	sleep 300
done
