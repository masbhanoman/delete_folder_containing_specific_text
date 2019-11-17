import os
import shutil
os.chdir("d:\\project_backup")
i = 1
for paths, dirs, files in os.walk(".", topdown = False):    
    for name in dirs:
        if "RELEASED_" in name :
            print(i+1)                   
            shutil.rmtree(os.path.join(paths, name))
     


 


