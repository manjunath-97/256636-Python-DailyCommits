'''
You have been asked to make a special book categorization program, which assigns each book a special code based on its title.
The code is equal to the first letter of the book, followed by the number of characters in the title.
For example, for the book "Harry Potter", the code would be: H12, as it contains 12 characters (including the space).

Note: Recall the readlines() method, which returns a list containing the lines of the file.
Also, remember that all lines, except the last one, contain a \n at the end, which should not be included in the character count.
'''

file = open("books.txt", "r")

#your code goes here
lines = file.readlines()
for i in range(len(lines)-1):
    print(lines[i][0],len(lines[i])-1,sep="",end="\n")
print(lines[len(lines)-1][0],len(lines[len(lines)-1]),sep="")


file.close()