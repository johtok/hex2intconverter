import argparse
from hex_converter import is_valid_hex, hex_to_int, hex_to_bool

def main():
    parser = argparse.ArgumentParser(description='Convert a string of hex values to different data types')
    parser.add_argument('hex_values', type=str, help='String of hex values separated by spaces')
    parser.add_argument('--output-type', type=str, choices=['int', 'bool'], default='int', help='Specify the output type (int or bool)')
    args = parser.parse_args()

    hex_values = args.hex_values.split()
    hex_values = [value if value[:2]=="0x" else"0x"+value for
 value in hex_values]
    for hex_value in hex_values:
        if is_valid_hex(hex_value):
            try:
                if args.output_type == 'int':
                    int_value = hex_to_int(hex_value, size=4)  # Adjust size as needed for different integer sizes
                    print(f'Signed Int32: {int_value}')
                elif args.output_type == 'bool':
                    bool_value = hex_to_bool(hex_value)
                    print(f'Boolean: {bool_value}')
            except ValueError:
                print(f"Error: '{hex_value}' is not a valid hexadecimal value.")
        else:
            print(f"Error: '{hex_value}' is not a valid hexadecimal value.")

if __name__ == '__main__':
    main()
