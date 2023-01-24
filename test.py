# i = 5
# j =7
# k = 3
#
# if i < j:
#     if j < k:
#         i = j
#     else:
#         j = k
# else:
#     if j > k:
#         j = i
#     else:
#         i = k
# print(i, j, k)

# x = 10
# if x == 10:
#     print(x)
# else:
#    print(-x)
# x, y, z = 3, 5, 7
# b1, b2, b3, b4 = True, False, x == 3, y < 3
# print(not (not b1 or not b2 or not b3))

for first in '12':
    # this line to complete the values for
    for second in '23':
        print(first+second)

# should_continue = True
# while should_continue:
#     for i in range(0, 8):
#         print("*")
#     should_continue = False

# x, y, z = 3, 5, 7
# print(x <= y)

# x1 = eval(input('Entry x1? '))
# print('x1 =', x1, ' type:', type(x1))

# value = eval(input("please enter an integer"))
# if value > 0:
#     if value <= 10:
# print("in range")
# print("Done")

# entry = input("enter number to sum : ")
# while entry >= 0:
#     entry = eval(input())
#     if entry >= 0:
#         sum += entry
# print("sum = ", sum)

# sum = 0
# for i in range(1, -1, -1):
#     print(i)
# #     sum += i
# print(sum)
# def get_input():
#     global arg1, arg2
#     arg1 = float(input("Enter arg #1: "))
#     arg2 = float(input("Enter arg #2: "))
#     result = arg1 - arg2
#     print(result)
    #result = arg1 + arg2

#
# def main():
#     menu = input("==S)dd - Q)uit ==")
#     done = False
#     while not done:
#         choice = menu
#         if choice == "S":
#             get_input()
#         elif choice == "Q":
#             done = True
#
# main()