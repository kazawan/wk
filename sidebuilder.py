# -*-coding:utf-8 -*-

import os
import sys
import re

filesDocument = ""
is_overWrite = 0

if len(sys.argv) <= 1:
    print("Error: 缺少参数 i 文档路径")
    sys.exit()

if sys.argv[1] == '-h':
    print("-i   参数地址 (./docs)" ,end='\n')
    print("-overwrite  填入代表覆盖_sidebar.md")
    sys.exit()
    

for i in range(len(sys.argv)):
    if sys.argv[i] == '-i':
        dirpath = sys.argv[i+1]
        if os.path.exists(dirpath):
            # print("is has document")
            filesDocument = dirpath
        else:
            # print("does't not exist")
            sys.exit()
    if sys.argv[i] == '-overwrite' :
            is_overWrite = 1


if  is_overWrite == 1 :
    sidebarremove = open("./_sidebar.md", "w", encoding="utf-8")
    sidebarremove.close()


sidebarpy = open("./_sidebar.md", "a", encoding="utf-8")
layer = 0


arr = []
arrdir = []




fileswalk = os.walk(filesDocument)
search_text = '\\'
replace_text = '/'


sidebarpy.write('- [:book:  ' + filesDocument + '](./)' + '\n')

for root ,dirs,files in fileswalk:
    for file in files:
        if file == '_sidebar.md':
            continue
        if file.endswith('.md'):
            path = os.path.join(root,file)
            path = path.replace(search_text, replace_text)
            path = '  - [' + file[:-3] + '](' + path + ')'
            sidebarpy.write(path+'\n')
            #print(path)
            
#print("转换完成")
