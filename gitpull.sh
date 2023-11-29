#!/bin/bash
  
echo " ========================== " >> ~/wk/gitlog.txt
time=$(date "+%Y-%m-%d %H:%M:%S")
cd `dirname $0` || exit 1 

cd /home/$(whoami)/wk/ 
echo "${time}: == > " >> ~/wk/gitlog.txt
/usr/bin/git pull >> ~/wk/gitlog.txt 

cd /home/$(whoami)/wk/

python3.11 ./sidebuilder.py -i docs/linux -overwrite
python3.11 ./sidebuilder.py -i docs/arduino
python3.11 ./sidebuilder.py -i docs/stm32 

echo "${time}:执行完成" >> ~/wk/gitlog.txt
