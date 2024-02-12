

with open("simple.txt", 'r') as file:
    data = file.readline()
    for eachline in data:
       word =  eachline.split()
       print(word)



'''

file = open("simple.txt", 'r')
print(file.read())
for each in file:
    print(each)

'''
