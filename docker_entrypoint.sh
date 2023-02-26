#!/bin/bash

set -e
for f in  {1..2}; do python3  mail_sender/main.py -prt $f ; done