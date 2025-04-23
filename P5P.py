def is_valid_part(part):
    try:
        i_part = int(part)
        if part[0] == '0' and not i_part == 0:
            return False
        return 0 <= i_part < 256
    except ValueError as e:
        return False

def is_vali_ip(ip:str):
    parts = ip.split('.')
    if len(parts) != 4: return False
    for part in parts:
        if not is_valid_part(part): return False
    return True

print(is_vali_ip('192.168.1.1'))
print(is_vali_ip('192.168.1.256'))
print(is_vali_ip('192.168.1.01'))
print(is_vali_ip('192.168.1.1.1'))
print(is_vali_ip('192.168.1.1.1.1'))

