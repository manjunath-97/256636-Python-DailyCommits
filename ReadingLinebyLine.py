file = open("fileHandling.txt","r")

#lines = file.readlines()
#print(lines)
#print()
for line in file:
    print(line,end=" ")
file.close()