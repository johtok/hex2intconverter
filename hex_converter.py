import re

def is_valid_hex(hex_string):
    return bool(re.match(r'^0x[0-9a-fA-F]+$', hex_string))

def hex_to_int(hex_string, size, signed=True):
    int_value = int(hex_string, 16)
    if signed:
        return int_value if int_value < 1 << (size * 8 - 1) else int_value - (1 << (size * 8))
    else:
        return int_value

def hex_to_bool(hex_string):
    return bool(int(hex_string, 16))
