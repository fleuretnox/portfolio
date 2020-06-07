import os
src_server = r'C:\Users\huhl\Desktop\devops\portfolio\src_server' + '\\'


for path1, dir2, files3 in os.walk(src_server):
    print (path1)
    print (dir2)
    print (files3)

#print(src_server)
