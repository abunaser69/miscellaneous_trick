import pandas as pd
import os
import errno
from os import listdir
from os.path import isfile,join
import csv
import re
import shutil

#assign working directory to variable
file_path=os.getcwd()


#setting path for data folder
data_path = os.path.abspath(os.path.join(file_path,'../Data/01_Raw'))

#while True:
try:
    if not os.path.exists(os.path.dirname('rename')):
        rename = os.mkdir(os.path.join(data_path, "rename"))
        os.makedirs(rename)       
except Exception:
    print("Folder Already exists, I am not making any folder")     
else: 
    try:
        if os.path.exists(os.path.dirname('rename')):
            pass
    except Eception:
        print("Stay cool")
finally:
    print("Its all good") 
    

#exception_handling

try:
    if not os.path.exists(os.path.dirname('rename')):
        os.makedirs(os.path.dirname('rename'))
except OSError as err:
    print(err)
    
#Change name of the file
#src_folder = data_path
#make a directory for new data file 
    
dest_folder = os.path.join(data_path, "rename")

lis = os.listdir(data_path)

for file in lis:
    try:
        pat = re.compile(r'999*')
        ms = pat.match(file)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    else:
        break
        
    if(bool(ms) == True):
        shutil.copy(os.path.join(data_path, file), os.path.join(dest_folder,"Validation.csv"))
    else:
        shutil.copy(os.path.join(data_path,file), os.path.join(dest_folder, "Production.csv")) 
        
# extracting file names without extensions
file_names=[".".join(f.split(".")[:-1]) for f in listdir(dest_folder) if isfile (join(dest_folder,f))] 

# extracting file names with extensions
full_file_names=[f for f in listdir(dest_folder) if isfile (join(dest_folder,f))]

#checking file names and extensions
print(file_names)
print(full_file_names)

#sorting list
full_file_names.sort()

print(full_file_names)
type(full_file_names)
#len(full_file_names_sort)

#creating a dictionary with file names and their extensions
dict_del= {}
delimit=[]
i=0
for i in range(len(full_file_names)):
    delimit.append(i)

#print(list(delimit))

t=0
for s in full_file_names:
    with open(dest_folder+'/'+s, newline='', encoding="utf8") as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read())
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        #delimit[t]=dialect.delimiter
        dict_del[s]=delimit[t]
        t+=1
        
import collections
od = collections.OrderedDict(sorted(dict_del.items(), reverse=False))

print(od)
#sorting the dictionary
#dict_del_sort = sorted(dict_del.keys(), key=lambda x:x.lower())
#dict_del_sort

#checking dictionary and delimiters
print(dict_del)
#type(dict_del)
#print(delimit)
dict_del.keys()
dict_del.values()

#creating globals/locals variables depend on file names
z=0
files_ready=[]
for f,r in zip(file_names,full_file_names):
    locals()[f]=pd.read_csv(dest_folder+'/'+r,sep=dict_del[r])        
    files_ready.append(f)
    z+=1

import os
import shutil
def copy_rename(old_file_name, new_file_name):
        src_dir= os.curdir
        dst_dir= os.path.join(os.curdir , "subfolder")
        src_file = os.path.join(src_dir, old_file_name)
        shutil.copy(src_file,dst_dir)
        
        dst_file = os.path.join(dst_dir, old_file_name)
        new_dst_file_name = os.path.join(dst_dir, new_file_name)
        os.rename(dst_file, new_dst_file_name)
 

