#59. copy 1 file content in to another file(Take the source and destination file path from the user)
source=input("enter file to copy:")
destination=input("enter the file to be copyed:")
print(source)
fp=open(source,"r")
data=fp.read()
wf=open(destination,"w")
wf.write(data)
fp.close()
wf.close()
