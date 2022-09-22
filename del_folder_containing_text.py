import os
import shutil
os.chdir("d:\\project_backup")
i = 1
for paths, dirs, files in os.walk(".", topdown = False):    
    for name in dirs:
        if "RELEASED_" in name :
            print(i+1)                   
            shutil.rmtree(os.path.join(paths, name))
     
#import os
#import sys
#import shutil
#rootdir = os.chdir("d:\\Odoo 13.0\\server\\odoo\\odoo13_custom\\odoo15_custom\\")
#folder_name_text = ''
#for paths, dirs, files in os.walk("d:\\Odoo 13.0\\server\\odoo\\odoo13_custom\\odoo15_custom\\"):
#    for name in dirs:
#        folder_name_text = folder_name_text +' '+ name + '/'
#print(folder_name_text)

 


