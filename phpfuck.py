# PHPFuck: ([+.^])

import string
from argparse import ArgumentParser


class PHPFuck():
    def __init__(self):
        # simple constant
        arr_str = "([].[])"  # "ArrayArray"
        zero = "([]^[])"
        one = "([]^[[]])"

        # generate digits
        nums = [zero, one]
        for i in range(2, 10):
            if i % 2 == 0:
                nums.append(f"{nums[i//2]}+{nums[i//2]}")
            else:
                nums.append(f"{nums[i//2]}+{nums[i//2+1]}")

        # using "Array0123456789" & xor to generate printable ascii char
        self.char_mapping = {
            '\t': f'({nums[0]}.[])[{nums[0]}]^({nums[9]}.[])[{nums[0]}]',
            '\n': f'({nums[2]}.[])[{nums[0]}]^({nums[8]}.[])[{nums[0]}]',
            '\x0b': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[4]}]',
            '\x0c': f'({nums[4]}.[])[{nums[0]}]^({nums[8]}.[])[{nums[0]}]',
            '\r': f'({nums[4]}.[])[{nums[0]}]^({nums[9]}.[])[{nums[0]}]',
            ' ': f'({arr_str})[{nums[0]}]^({arr_str})[{nums[3]}]',
            '!': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[3]}]^({nums[2]}.[])[{nums[0]}]',
            '"': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[3]}]^({nums[1]}.[])[{nums[0]}]',
            '#': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[3]}]^({nums[0]}.[])[{nums[0]}]',
            '$': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[3]}]^({nums[7]}.[])[{nums[0]}]',
            '%': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[3]}]^({nums[6]}.[])[{nums[0]}]',
            '&': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[3]}]^({nums[5]}.[])[{nums[0]}]',
            "'": f'({arr_str})[{nums[1]}]^({arr_str})[{nums[3]}]^({nums[4]}.[])[{nums[0]}]',
            '(': f'({arr_str})[{nums[3]}]^({arr_str})[{nums[4]}]^({nums[0]}.[])[{nums[0]}]',
            ')': f'({arr_str})[{nums[3]}]^({arr_str})[{nums[4]}]^({nums[1]}.[])[{nums[0]}]',
            '*': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[3]}]^({nums[9]}.[])[{nums[0]}]',
            '+': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[3]}]^({nums[8]}.[])[{nums[0]}]',
            ',': f'({arr_str})[{nums[3]}]^({arr_str})[{nums[4]}]^({nums[4]}.[])[{nums[0]}]',
            '-': f'({arr_str})[{nums[3]}]^({arr_str})[{nums[4]}]^({nums[5]}.[])[{nums[0]}]',
            '.': f'({arr_str})[{nums[3]}]^({arr_str})[{nums[4]}]^({nums[6]}.[])[{nums[0]}]',
            '/': f'({arr_str})[{nums[3]}]^({arr_str})[{nums[4]}]^({nums[7]}.[])[{nums[0]}]',
            '0': f'({nums[0]}.[])[{nums[0]}]',
            '1': f'({nums[1]}.[])[{nums[0]}]',
            '2': f'({nums[2]}.[])[{nums[0]}]',
            '3': f'({nums[3]}.[])[{nums[0]}]',
            '4': f'({nums[4]}.[])[{nums[0]}]',
            '5': f'({nums[5]}.[])[{nums[0]}]',
            '6': f'({nums[6]}.[])[{nums[0]}]',
            '7': f'({nums[7]}.[])[{nums[0]}]',
            '8': f'({nums[8]}.[])[{nums[0]}]',
            '9': f'({nums[9]}.[])[{nums[0]}]',
            ':': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[4]}]^({nums[1]}.[])[{nums[0]}]',
            ';': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[4]}]^({nums[0]}.[])[{nums[0]}]',
            '<': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[4]}]^({nums[7]}.[])[{nums[0]}]',
            '=': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[4]}]^({nums[6]}.[])[{nums[0]}]',
            '>': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[4]}]^({nums[5]}.[])[{nums[0]}]',
            '?': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[4]}]^({nums[4]}.[])[{nums[0]}]',
            '@': f'({arr_str})[{nums[1]}]^({nums[2]}.[])[{nums[0]}]',
            'A': f'({arr_str})[{nums[0]}]',
            'B': f'({arr_str})[{nums[1]}]^({nums[0]}.[])[{nums[0]}]',
            'C': f'({arr_str})[{nums[1]}]^({nums[1]}.[])[{nums[0]}]',
            'D': f'({arr_str})[{nums[1]}]^({nums[6]}.[])[{nums[0]}]',
            'E': f'({arr_str})[{nums[1]}]^({nums[7]}.[])[{nums[0]}]',
            'F': f'({arr_str})[{nums[1]}]^({nums[4]}.[])[{nums[0]}]',
            'G': f'({arr_str})[{nums[1]}]^({nums[5]}.[])[{nums[0]}]',
            'H': f'({arr_str})[{nums[4]}]^({nums[1]}.[])[{nums[0]}]',
            'I': f'({arr_str})[{nums[4]}]^({nums[0]}.[])[{nums[0]}]',
            'J': f'({arr_str})[{nums[1]}]^({nums[8]}.[])[{nums[0]}]',
            'K': f'({arr_str})[{nums[1]}]^({nums[9]}.[])[{nums[0]}]',
            'L': f'({arr_str})[{nums[4]}]^({nums[5]}.[])[{nums[0]}]',
            'M': f'({arr_str})[{nums[4]}]^({nums[4]}.[])[{nums[0]}]',
            'N': f'({arr_str})[{nums[4]}]^({nums[7]}.[])[{nums[0]}]',
            'O': f'({arr_str})[{nums[4]}]^({nums[6]}.[])[{nums[0]}]',
            'P': f'({arr_str})[{nums[3]}]^({nums[1]}.[])[{nums[0]}]',
            'Q': f'({arr_str})[{nums[3]}]^({nums[0]}.[])[{nums[0]}]',
            'R': f'({arr_str})[{nums[3]}]^({nums[3]}.[])[{nums[0]}]',
            'S': f'({arr_str})[{nums[3]}]^({nums[2]}.[])[{nums[0]}]',
            'T': f'({arr_str})[{nums[3]}]^({nums[5]}.[])[{nums[0]}]',
            'U': f'({arr_str})[{nums[3]}]^({nums[4]}.[])[{nums[0]}]',
            'V': f'({arr_str})[{nums[3]}]^({nums[7]}.[])[{nums[0]}]',
            'W': f'({arr_str})[{nums[3]}]^({nums[6]}.[])[{nums[0]}]',
            'X': f'({arr_str})[{nums[3]}]^({nums[9]}.[])[{nums[0]}]',
            'Y': f'({arr_str})[{nums[3]}]^({nums[8]}.[])[{nums[0]}]',
            'Z': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[3]}]^({arr_str})[{nums[4]}]^({nums[0]}.[])[{nums[0]}]',
            '[': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[3]}]^({arr_str})[{nums[4]}]^({nums[1]}.[])[{nums[0]}]',
            '\\': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[3]}]^({arr_str})[{nums[4]}]^({nums[6]}.[])[{nums[0]}]',
            ']': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[3]}]^({arr_str})[{nums[4]}]^({nums[7]}.[])[{nums[0]}]',
            '^': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[3]}]^({arr_str})[{nums[4]}]^({nums[4]}.[])[{nums[0]}]',
            '_': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[3]}]^({arr_str})[{nums[4]}]^({nums[5]}.[])[{nums[0]}]',
            '`': f'({arr_str})[{nums[3]}]^({nums[0]}.[])[{nums[0]}]^({nums[1]}.[])[{nums[0]}]',
            'a': f'({arr_str})[{nums[3]}]',
            'b': f'({arr_str})[{nums[3]}]^({nums[0]}.[])[{nums[0]}]^({nums[3]}.[])[{nums[0]}]',
            'c': f'({arr_str})[{nums[3]}]^({nums[0]}.[])[{nums[0]}]^({nums[2]}.[])[{nums[0]}]',
            'd': f'({arr_str})[{nums[3]}]^({nums[0]}.[])[{nums[0]}]^({nums[5]}.[])[{nums[0]}]',
            'e': f'({arr_str})[{nums[3]}]^({nums[0]}.[])[{nums[0]}]^({nums[4]}.[])[{nums[0]}]',
            'f': f'({arr_str})[{nums[3]}]^({nums[0]}.[])[{nums[0]}]^({nums[7]}.[])[{nums[0]}]',
            'g': f'({arr_str})[{nums[3]}]^({nums[0]}.[])[{nums[0]}]^({nums[6]}.[])[{nums[0]}]',
            'h': f'({arr_str})[{nums[3]}]^({nums[0]}.[])[{nums[0]}]^({nums[9]}.[])[{nums[0]}]',
            'i': f'({arr_str})[{nums[3]}]^({nums[0]}.[])[{nums[0]}]^({nums[8]}.[])[{nums[0]}]',
            'j': f'({arr_str})[{nums[1]}]^({arr_str})[{nums[3]}]^({arr_str})[{nums[4]}]',
            'k': f'({arr_str})[{nums[3]}]^({nums[2]}.[])[{nums[0]}]^({nums[8]}.[])[{nums[0]}]',
            'l': f'({arr_str})[{nums[3]}]^({nums[4]}.[])[{nums[0]}]^({nums[9]}.[])[{nums[0]}]',
            'm': f'({arr_str})[{nums[3]}]^({nums[4]}.[])[{nums[0]}]^({nums[8]}.[])[{nums[0]}]',
            'n': f'({arr_str})[{nums[3]}]^({nums[6]}.[])[{nums[0]}]^({nums[9]}.[])[{nums[0]}]',
            'o': f'({arr_str})[{nums[3]}]^({nums[6]}.[])[{nums[0]}]^({nums[8]}.[])[{nums[0]}]',
            'p': f'({arr_str})[{nums[0]}]^({nums[1]}.[])[{nums[0]}]',
            'q': f'({arr_str})[{nums[0]}]^({nums[0]}.[])[{nums[0]}]',
            'r': f'({arr_str})[{nums[1]}]',
            's': f'({arr_str})[{nums[0]}]^({nums[2]}.[])[{nums[0]}]',
            't': f'({arr_str})[{nums[0]}]^({nums[5]}.[])[{nums[0]}]',
            'u': f'({arr_str})[{nums[0]}]^({nums[4]}.[])[{nums[0]}]',
            'v': f'({arr_str})[{nums[0]}]^({nums[7]}.[])[{nums[0]}]',
            'w': f'({arr_str})[{nums[0]}]^({nums[6]}.[])[{nums[0]}]',
            'x': f'({arr_str})[{nums[0]}]^({nums[9]}.[])[{nums[0]}]',
            'y': f'({arr_str})[{nums[4]}]',
            'z': f'({arr_str})[{nums[1]}]^({nums[0]}.[])[{nums[0]}]^({nums[8]}.[])[{nums[0]}]',
            '{': f'({arr_str})[{nums[1]}]^({nums[0]}.[])[{nums[0]}]^({nums[9]}.[])[{nums[0]}]',
            '|': f'({arr_str})[{nums[1]}]^({nums[6]}.[])[{nums[0]}]^({nums[8]}.[])[{nums[0]}]',
            '}': f'({arr_str})[{nums[1]}]^({nums[6]}.[])[{nums[0]}]^({nums[9]}.[])[{nums[0]}]',
            '~': f'({arr_str})[{nums[1]}]^({nums[4]}.[])[{nums[0]}]^({nums[8]}.[])[{nums[0]}]'
        }

    def encode(self, code):
        return '.'.join([f"({self.char_mapping[c]})" for c in code])

    def eval_code(self, code, mode="create_function"):
        if mode == 'create_function':
            create_function = self.encode("create_function")
            eval_code = f"({create_function})([].[]^[].[],{code})();"

        elif mode == 'assert':  # only support PHP < 7.1
            assert_func = self.encode('assert')
            eval_code = f"""
            ({assert_func})(
                ({self.encode('(function(){')}).
                ({code}).
                ({self.encode(';return 1;})()')})
            );
            """.replace('\n', '').replace(' ','')
        return eval_code


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("code", help="any string to encode.")
    parser.add_argument("-O", "--output-file", dest="file",
                        help="write encoded string into some file.")
    parser.add_argument("-P", "--plain-string", dest="plain", action='store_true',
                        help="encode as plain string (without eval it).")
    parser.add_argument("-E", "--eval", dest="eval", 
                        choices=['assert', 'create_function'], default='create_function',
                        help="choose eval mode. (`assert` mode only support PHP < 7.1)")
    args = parser.parse_args()

    code = args.code

    phpfuck = PHPFuck()

    encoded = phpfuck.encode(code)
    if args.eval and not args.plain:
        encoded = "<?php " + phpfuck.eval_code(encoded, args.eval) + " ?>"

    if args.file:
        open(args.file, 'w').write(encoded)
    else:
        print(encoded)

    print()
    if args.plain:
        print(f"Output as plain string, without eval it.")
    else:
        print(f"Using `{args.eval}` mode to eval.")
    print(len(encoded), "chars.")
