try:
    file = open("fileHandling.txt","w+")
    n = file.write("This sentence was written to the file through write() function")
    print(n)
    print(file.readlines())
finally:
    file.close()
