#open and read
myfile = open("fruits.txt")
print(myfile.read())

# to be able to print the content from the file multiple times it needs to be stored in a variable
myfile = open("fruits.txt")
content = myfile.read()
print(content)
print(content)

#to close the file from the memor
#you cannot read the file multiple times after its closed
myfile = open("fruits.txt")
content = myfile.read()
myfile.close()

print(content)


##################################
#a better way with "with" manager
# with method apply the close method implicity
with open("fruits.txt") as myfile:
  content = myfile.read()

print(content)


################################
#Diferent paths
with open("file/fruits.txt") as myfile:
  content = myfile.read()

print(content)
print("done")