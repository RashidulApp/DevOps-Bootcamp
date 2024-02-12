
file = open("demo.txt", 'w')

file.write("Hello world \n")
file.write("01725179849")
file.close()

read = open("demo.txt", "r")

print(read.read())

