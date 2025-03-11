def dec_to_bin (a,b):
    bin1 = ""
    for i in range(b + 1):
        if a < (2 ** (b -i)):
            bin1 += "0"
        elif a >= (2 ** (b - i)):
            bin1 += "1"
            a -= (2 ** (b - i))
    return bin1

def bin_to_dec (c):
    dec1 = 0
    for i in range (len(c) + 1):
        dec1 += (c[-1 -i] * (2 ** i))
    return dec1
dec = input("enter positive number please: ")
# if dec <= 0 :
#     print("you need to enter a positive number! try again.")
sibits = input("how many sibits? ")
bin = dec_to_bin(int(dec), int(sibits))
print(bin)