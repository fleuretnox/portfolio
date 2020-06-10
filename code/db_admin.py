import os
import shutil

##https://www.youtube.com/watch?v=YT8UMQAJVnE
# We want to have a source and destinational path to move from one place to another
src_server = r'C:\Users\huhl\Desktop\devops\portfolio\Backup Server' + '\\'
dest_server = r'C:\Users\huhl\Desktop\devops\portfolio\DR Server' + '\\'

# '\\' to make folder variable

# for and if statement logic
# os.walk method contains and returns path, dir, and file
# for path, dir, files in os.walk(src_server):
#     if files:
#         for all_file in files:
#             if not os.path.isfile(dest_server + file):
#                 os.rename(path + '\\' + file, dest_server + file)


# create a function to move files
# 2 parameters to have source and dest path
def mv_files (sourcepath, dest_server):
    for (path, dirs, files) in os.walk(src_server):
        #for all_file in files:  #any files you see on that path source server
                #if the file doesn't exist on the given path
            if not files in os.path.isfile(dest_server + files):
                    #move the folder
                shutil.move(path + '\\' + files)
                print ("all files were moved")
            else:
                print ("files not found")


mv_files (src_server, dest_server)
