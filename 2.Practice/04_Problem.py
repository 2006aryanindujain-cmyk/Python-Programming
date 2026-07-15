import os

#select a directory whose content you wnat to list
path = "D:\REPOSITORIES"

#use the os module to list the directory contents
contents = os.listdir(path)

for item in contents:
    print(item)
