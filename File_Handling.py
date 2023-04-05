#open(filename ,mode(r->reading,w->writting,a->append,rb->Read binary)) #-->Method For to open the file

#Code 👇
# file = open("myFile.txt","rb") #--> file created -->then read Using (r) mode
# text = file.read() #-->Read method
# print(text)
# file.close() #-->Without {with keyword} we use close and {in with keyword} file automatically close

#Information about File Handling 👇
# #MODULES IN FILE HANDLING
# #1)read(r) 2)write(w) 3)append(a) 4)create(x) 5)text(t) 6)Binary(b)

#code 👇
# file = open("myFile.txt","w") #-->(Write) remove all data that is written already they specially use for overwrite
# file.write("Hello,I am Aqeel Jan ")
# file = open("myFile.txt","a") #-->(Append) modified the file and does not over write
# file.write("Good Bye ")
# file.close()

# with open("myFile.txt","a") as file: #--> We use here with keyword benefit of keyword that they automatically close the file when we complete our work
#     file.write(("\nI am using with keyword"))


with open("myFile.txt",'r') as file:
    while True:
        line = file.readline() #-->ReadLine -->user read line by line file
        print(line)
        if not line:
            print(type(line)) #-->Type -->tell the data type that we use
            break


with open("marks.txt","r") as marksFile:
    i = 0
    while True:
        i = i + 1
        line = marksFile.readline()
        if not line:
            break
        m1 = line.split(",")[0]
        m2 = line.split(",")[1]
        m3 = line.split(",")[2]
        print(f"Marks Of Student {i} are {m1},{m2},{m3}")

with open ("NewFile.txt","w") as file:
    line = ["Hello I am Aqeel \nNow I am working in python"]
    file.writelines(line)
        

with open("NewFile.txt","r") as Files:
    print(type(Files))
    Files.seek(10) #Move to that byte of files
    #Files.Seek() = Files.tell() tell->Give Information about seek
    print(Files.seek(10)) 
    print(Files.tell())#Tell About the seek function and tell current position
    print(Files.read());   #And Read All Byte After 5 byte 


with open("File.txt","a") as f:
    f.write("Good Morning")
    f.truncate(5) # -->Give Size for write the character -->Restrict the file that save how many chraracters

with open("File.txt","r") as f:
    print(f.read())



