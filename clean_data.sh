#!/bin/bash

grep -A 4 CID0 source_web.txt | grep name > source_web_clean.txt
grep checkbox source_web_clean.txt > d_names.txt
