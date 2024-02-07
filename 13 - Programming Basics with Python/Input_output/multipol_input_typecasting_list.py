
user_inpur = input("Enter multipol student roll no : ")

print(user_inpur)

user_input_split = user_inpur.split()

print(user_input_split)

user_input_map = map(int, user_input_split)
studentList = list(user_input_map)

for value in studentList:
    print(value)


print(studentList)