x = "hello world!"
new_x = x[::-1]
print(new_x)

empty_string = ""
string = "hello world!"
for y in range (len(string) - 1, -1, -1):
    empty_string += string[y]
print (empty_string)