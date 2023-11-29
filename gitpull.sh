#!/bin/bash
#. /etc/profile
echo " ========================== " >> ~/wk/gitlog.txt
time=$(date "+%Y-%m-%d %H:%M:%S")
cd `dirname $0` || exit 1 

cd /home/ubuntu/wk/linux 
echo "${time}: == > " >> ~/wk/gitlog.txt
/usr/bin/git pull >> ~/wk/gitlog.txt 

cd /home/ubuntu/wk/

python3.11 ./sidebuilder.py -i linux -overwrite

echo "${time}:执行完成" >> ~/wk/wklog.txt
