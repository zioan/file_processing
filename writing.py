# read
with open("file/fruits.txt", "r") as myfile:
  content = myfile.read()

print(content)

# write
# the "w" (write) method create the file and the content, if there is an existing file with the same name it will be overwriting
with open("file/vegetables.txt", "w") as myfile:
  myfile.write("Tomato")

# write multiple lines (\n)
with open("file/vegetables.txt", "w") as myfile:
  myfile.write("Tomato\nCucumber\nOnion\n")
  myfile.write("Garlic")

# exercise 1
# read the first 90 characters from a file

#with open("bear.txt") as myfile:
#    content = myfile.read()
#    new_content = content[0:90]
#print(new_content)

#exercise 2
#define a function that takes 2 arguments, a single string character and a filepath and returns the number of occurrences on that character in the file
def find (x, path):
  with open(str(path)) as myfile:
    content = myfile.read()
    occurrences = content.count(x)
  return occurrences


print(find("o", "file/vegetables.txt"))

#exercise 3
with open("file/new.txt", "w") as file2:
  file2.write("snail")

#exercise 4
#read the first 30 characters from a file and write them in another file
with open("fruits.txt") as fruits_file:
  fruits_content =fruits_file.read()
  fruits_extract = fruits_content[0:30]
with open("file/first.txt", "w") as first_file:
  first_file.write(fruits_extract)
