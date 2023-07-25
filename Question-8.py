# Write a python script to store a hexadecimal number 2F in a variable and print it in octal format

Hexa_number = "2F"

decimal_number = int(Hexa_number,16)

octal = oct(decimal_number)[2:]

print("The octal representation of 2F:",octal)