
'''def salary(*args):
    total_sum = add(*args)
    average = total_sum/len(args)
    #print(average)
    return average

def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

def standard_deviation(*args):
    avg = average(*args)


salary(10, 20, 20)
'''
'''
def salary(**kwargs):
    for key, value in kwargs.items():
        if value >= 10000:
            print("You are rich man.")
        else:
            print("Hey dude, you seem to be poor.")

salary_amount = int(input("Enter your salary amount: "))
salary(amount=salary_amount)'''

# Write a function that check the value is odd or even
# and store the even value in even list and odd values in odd list

def CheckNumber(**kwargs):
    for key, value in kwargs.items():
        if value % 2 >= 0:
            print("This is even number.")
        else:
            print("This is odd number.")

user_value = int(input("Enter your number: "))

CheckNumber(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
