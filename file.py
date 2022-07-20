f = open("test.txt", "a" )
f.write("now the file has more content 1 ")
f.close()

#open and read the file after appending 
f = open("test.txt", "r")

print(f.read())