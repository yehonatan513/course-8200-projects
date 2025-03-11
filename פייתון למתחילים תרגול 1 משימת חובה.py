#תרגיל 1
numbers = [3, 5, 2, 8, 1, 9, 4,]
max = numbers[1]
for i in range(len(numbers)):
    if numbers[i] >= max:
        max = numbers[i]
print(max)

# #תרגיל 2
# def only_even (original_list):
#     copied_list = original_list.copy()
#     for i in range(len(original_list)):
#         if original_list[i] % 2 != 0:
#             copied_list.pop(i)
#     return copied_list
# # list = (input("enter list: "))
# # print(only_even(list))

#תרגיל 3
test_list = [1, 2, 3, 4, 5]
checking = True
for x in range(len(test_list)):
    if test_list[x] > test_list[x+1]:
        checking = False
print(checking)

#תרגיל 4
empty_string = ""
string = "1234"
for y in range (len(string) - 1, -1, -1):
    empty_string += string[y]
print (empty_string)

#תרגיל 5
string1 = "i want to be a python maker"
vowels = string1.count("a") + string1.count("e") + string1.count("i") + string1.count("o") + string1.count("u")
print (vowels)