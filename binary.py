binary_str = "1010"
integer = int(binary_str, 2)  # Convert binary to integer
print(integer)
integer = 10
binary = format(integer, 'b')  # '1010'
print(binary)
num = 10
binary = bin(num)  # Returns '0b1010'
binary_str = bin(num)[2:]  # Removes '0b' -> '1010'
print(binary_str)  # Output: '1010'
num = -10
binary_str = '-' + bin(-num)[2:] if num < 0 else bin(num)[2:]
print(binary_str)  # Output: '-1010'


