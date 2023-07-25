# Write a python script to store an octal number 125 in a variable and print it in binary format.

octal_number = "125"

decimal_number = int(octal_number,8)

binary_number = bin(decimal_number)[2:]

print("The binary representation of octal number 125 is",binary_number)