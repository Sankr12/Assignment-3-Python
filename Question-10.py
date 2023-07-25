# Write a python script to add two numbers 25(in octal) and 39 (in Hexadecimal) and display the result in binary format.

octal_number = "25"
number1 = int(octal_number,8)

hexadecimal_number = "39"
number2 = int(hexadecimal_number,16)

sum = number1 + number2

binary_number = bin(sum)[2:]

print("The binary representation of Octa 25 and Hexa 39 is:",binary_number)