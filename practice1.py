def my_devide(num1: int, num2: int)->int:
    quotient = num1 // num2
    remainder = num1 % num2
    return quotient, remainder

print(my_devide(10,3))


def my_diagonal(num1:int)->int:
    diagonal = (num1 * (num1 - 3)) // 2

    return diagonal

print(my_diagonal(5))


def my_rounding(num1: float) -> int:
    if (num1>=0):
        rounding = int(num1 + 0.5)
    else: rounding = int(num1 - 0.5)
    return rounding

print(my_rounding(4.4))

#name seperator
my_name = input("please input your full name: ")
def name_seperator(my_name):
    name1, _, _ = my_name.partition(" ")
    _, _, name2 = my_name.rpartition(" ")
    return name1, name2


name1, name2 = name_seperator(my_name)

print("first name is " + name1)
print("last name is " + name2)


#gender age distinguisher
from datetime import date

today = date.today
today = today.strftime("%Y%m%d")

def q3(my_number): 
    birthnum = my_number[:5]
    gendernum = my_number[-1]
    if gendernum == [1, 3]:
        gender = "male"
    elif gendernum == [2, 4]:
        gender = "female"
    else: print("gender num error..")

    


    return gender, 



my_number = input("input your personal numbers: ")
q3(my_number)
print("gender : " + gender)
print("age : " + age)