def ip_to_binary(ip):
    binary_ip = '.'.join(format(int(octet), '08b') for octet in ip.split('.'))
    return binary_ip

# Example usage
ip_address = "255.168.1.1"
binary_representation = ip_to_binary(ip_address)
print(f"IP Address: {ip_address}")
print(f"Binary Representation: {binary_representation}")

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

binary_number = "101101"
decimal_representation = binary_to_decimal(binary_number)
print(f"Binary Number: {binary_number}")
print(f"Decimal Representation: {decimal_representation}")

binary_number = "1010"
decimal_representation = binary_to_decimal(binary_number)
print(f"Your number is: {binary_number}")
print(f"Your number in decimal is: {decimal_representation}")

binary_number = "11111111"
decimal_representation = binary_to_decimal(binary_number)
print(binary_to_decimal("11111111"))  # 255
print(f"Your number in decimal is: {decimal_representation}")

binary_number = "00000001"
decimal_representation = binary_to_decimal(binary_number)
print(binary_to_decimal("1"))
print(f"Your number in decimal is: {decimal_representation}")
