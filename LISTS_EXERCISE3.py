#EXERCISE3: Batch Student Grade File Processor
openfile = open("talaba","r")
file_read=openfile.readline()

list2=file_read.split()
lastname=list2[0]
firstname=list2[1]
username=lastname[:7]+firstname[0]
print(username.lower())





