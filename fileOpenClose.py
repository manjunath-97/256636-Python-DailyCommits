file = open("fileHandling.txt","r")

#should do something afterwards
#content = file.read()
#print(content)

print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())

file.close()