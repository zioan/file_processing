# to append to the file "a" (not overwrite)
#you cannot read the file since is only "a" (appending)
with open("file/fruits.txt", "a") as myfile:
  myfile.write("\nNew Item")
  
#to be able to append and read -> "a+"
#you get an empty line because the cursor is at the end of the file
#in order to read the file -> .seek(0)
with open("file/fruits.txt", "a+") as myfile:
  myfile.write("\nAnother Item")
  myfile.seek(0)
  content = myfile.read()
print(content)

#exercise 1
#read and append to another file
with open("file/first.txt", "r") as first:
  first_content = first.read()
with open("file/fruits.txt", "a") as fruits:
  fruits.write(first_content)

#exercise 2
#modify the content of a file (duplicate the content in the file 2 more times)
with open("data.txt", "a+") as data:
  data.seek(0)
  original_data = data.read()
  data.write(original_data)
  data.write(original_data)
  