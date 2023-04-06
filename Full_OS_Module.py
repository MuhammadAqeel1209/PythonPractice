import os
#print(os.name) #--> For Name
#print(os.sep) #-->/ Forward For Linus #-->\ Backward For Window

#os.makedirs("Folder_One")
current = (os.getcwd()) #-->Get Current directory of working
# print(f"First Current Folder->{current}")

#print(os.walk(current))

# for item in os.walk(current): #-->Get Detail Of Current Folder using os.walk
#     print(item)

# for root,filenames,dirnames in os.walk(current):
#     #print(root) #-->Directory Path
#     print(filenames) #--> Folder Name in Current Folder Name
#     #print(dirnames) #--> Directory Name

# os.chdir("E:\\Python\\In VsCode\\Folder_One") #-->Change The Directory Address
# print(f"Second Current Folder->{ os.getcwd()}")

#print(os.stat("Libarry.txt")) #--> State Of Files

#os.path.join --> join two folder or files
# NewFolder = os.path.join(current,"Folder_One") #-->path join --> join the current path and other folder
# file = os.path.join(NewFolder,"Sample.txt") #--> path join --> join new folder and make the new file in new folder

# with open(file,"w") as f:
#     f.write("Hello") 

#print(os.path.exists("Aqeel_Folder")) #--> Check path of folder or folder exist or not

# if not os.path.exists("Aqeel_Folder"): #--> Using If Condition path exist or not
#     os.mkdir("Aqeel_Folder") #--> Making directory

#file = os.path.join(current,"Sample_text.txt")
# print(os.path.split(file)) #--> Split File Name and Folder name
#print(os.path.splitext(file)) #--> Split Folder name and show only file extension not ful name
#print(os.rename(file, "new_File.txt")) #-->Rename The File

#--> Cut And Copy
file = os.path.join(current,"Sample.txt") #--> First get original file address in the current directory
#folder_path = os.path.join(current,"Aqeel_Folder") #--> Second Get original addressNew Folder in current directory
#print(os.rename(file, f"{folder_path}/python.txt")) #--> Cut The file from first get addres to second address

#os.remove(file) #--> Remove the files
#os.removedirs("Folder_One") #--> Remove Directory