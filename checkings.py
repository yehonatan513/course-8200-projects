def bin_to_dec (c):
    dec1 = 0
    for i in range (len(c)):
        dec1 += int(c[-1 -i]) * (2 ** i)
    return dec1
z = bin_to_dec ("1011")
print(z)