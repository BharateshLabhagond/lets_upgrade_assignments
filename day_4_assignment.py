#Write a Python function that takes in a list of numbers and returns the sum of the squares of all the numbers in the list.

demo_list = [1,2,0,9,3,4,7,6]

def fun():
    sumOfList = 0
    for i in demo_list:
        sumOfList += i**2
    return sumOfList

print("result is : ",fun())