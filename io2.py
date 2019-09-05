myfile = open('test.txt')
print(myfile.read())
print(myfile.read())
myfile.seek(0)
print(myfile.read())  
myfile.seek(0)
print(myfile.readlines())
#file = open("/home/dxchange/Desktop/apps")
#print(file.read())
myfile.close()
#file.close()
with open("test.txt") as new_file:
	content = new_file.read()
	print(content)

with open("test.txt", mode = 'r') as myfile:
	content = myfile.read()
	print(content)
with open("file.txt",mode='r') as f:
	print(f.read())

with open("file.txt",mode='a') as f:
	f.write('\nfour on forth')
	
with open("sdkjdsk.txt",mode='w') as f:
	f.write('i created this file')

