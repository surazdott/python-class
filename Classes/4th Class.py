student_marks = {"arjun":0, "suraj":1, "prakash":10, "raju":-2}
'''
# Update
student_marks["raju"] = 90
a = student_marks["raju"]
print(student_marks.keys())

# Create
student_marks["pandey"] = 10
print(student_marks)

# Values
print(student_marks.values())

# Complicated Data Structure
student_marks = {"arjun":[1, 2, 3], "suraj":1, "prakash":10, "raju":-2}
print(student_marks["arjun"][0])

# Nested Dictionary
my_info = {"name":'suraj', "phone":1010, "address":{"city":'bhaktapur', "tole":'kamalbinayak'}}
print(my_info["address"])

'''
'''
a = input("Enter first number: ")
b = input("Enter second number: ")
print('The sum of' + a + b + 'is' + str(int(a)+ int(b)))
'''
'''
a = range(3, 22, 2)
print(list(a))
'''

student_marks = {"Arjun":99, "Suraj":90, "Prakash":80}
name = input("Enter name: ")
print("Your score is " + str(student_marks[name]))