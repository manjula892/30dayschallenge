# Writing to a file
file = open("sample.txt", "w")
file.write("Hello Manju\nWelcome to Python!")
file.close()

# Reading from the file
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()