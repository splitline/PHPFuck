class PHPFuck {
    constructor() {
        const arrString = "[].[]"; // "ArrayArray"
        const zero = "([]^[])";
        const one = "([]^[[]])";

        // generate digits
        const nums = [zero, one];
        for (let i = 2; i < 10; ++i) {
            nums.push(Array(i).fill(nums[1]).join('+'));
        }

        this.nums = nums;

        this.charMapping = {
            "0": `${nums[0]}.[][[]]`,
            "1": `${nums[1]}.[][[]]`,
            "2": `${nums[2]}.[][[]]`,
            "3": `(${arrString})[${nums[0]}]^(${arrString})[${nums[1]}]`,
            "4": `${nums[4]}.[][[]]`,
            "5": `${nums[5]}.[][[]]`,
            "6": `${nums[6]}.[][[]]`,
            "7": `${nums[7]}.[][[]]`,
            "8": `(${arrString})[${nums[0]}]^(${arrString})[${nums[4]}]`,
            "9": `${nums[2]}.[][[]]^(${arrString})[${nums[1]}]^(${arrString})[${nums[4]}]`,
            "a": `(${arrString})[${nums[3]}]`,
            "b": `${nums[1]}.[][[]]^${nums[2]}.[][[]]^(${arrString})[${nums[3]}]`,
            "c": `${nums[0]}.[][[]]^${nums[2]}.[][[]]^(${arrString})[${nums[3]}]`,
            "d": `${nums[1]}.[][[]]^${nums[4]}.[][[]]^(${arrString})[${nums[3]}]`,
            "e": `${nums[0]}.[][[]]^${nums[4]}.[][[]]^(${arrString})[${nums[3]}]`,
            "f": `${nums[4]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[1]}]^(${arrString})[${nums[3]}]`,
            "g": `${nums[2]}.[][[]]^${nums[4]}.[][[]]^(${arrString})[${nums[3]}]`,
            "h": `${nums[1]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "i": `${nums[0]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "j": `(${arrString})[${nums[1]}]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "k": `${nums[2]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "l": `${nums[5]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "m": `${nums[4]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "n": `${nums[0]}.[][[]]^${nums[4]}.[][[]]^(${arrString})[${nums[1]}]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "o": `${nums[6]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "p": `${nums[1]}.[][[]]^(${arrString})[${nums[0]}]`,
            "q": `${nums[0]}.[][[]]^(${arrString})[${nums[0]}]`,
            "r": `(${arrString})[${nums[1]}]`,
            "s": `${nums[2]}.[][[]]^(${arrString})[${nums[0]}]`,
            "t": `${nums[5]}.[][[]]^(${arrString})[${nums[0]}]`,
            "u": `${nums[4]}.[][[]]^(${arrString})[${nums[0]}]`,
            "v": `${nums[0]}.[][[]]^${nums[4]}.[][[]]^(${arrString})[${nums[1]}]`,
            "w": `${nums[6]}.[][[]]^(${arrString})[${nums[0]}]`,
            "x": `${nums[0]}.[][[]]^${nums[1]}.[][[]]^(${arrString})[${nums[4]}]`,
            "y": `(${arrString})[${nums[4]}]`,
            "z": `${nums[1]}.[][[]]^${nums[2]}.[][[]]^(${arrString})[${nums[4]}]`,
            "A": `(${arrString})[${nums[0]}]`,
            "B": `${nums[0]}.[][[]]^(${arrString})[${nums[1]}]`,
            "C": `${nums[1]}.[][[]]^(${arrString})[${nums[1]}]`,
            "D": `${nums[1]}.[][[]]^${nums[4]}.[][[]]^(${arrString})[${nums[0]}]`,
            "E": `${nums[0]}.[][[]]^${nums[4]}.[][[]]^(${arrString})[${nums[0]}]`,
            "F": `${nums[4]}.[][[]]^(${arrString})[${nums[1]}]`,
            "G": `${nums[5]}.[][[]]^(${arrString})[${nums[1]}]`,
            "H": `${nums[1]}.[][[]]^(${arrString})[${nums[4]}]`,
            "I": `${nums[0]}.[][[]]^(${arrString})[${nums[4]}]`,
            "J": `(${arrString})[${nums[0]}]^(${arrString})[${nums[1]}]^(${arrString})[${nums[4]}]`,
            "K": `${nums[2]}.[][[]]^(${arrString})[${nums[4]}]`,
            "L": `${nums[5]}.[][[]]^(${arrString})[${nums[4]}]`,
            "M": `${nums[4]}.[][[]]^(${arrString})[${nums[4]}]`,
            "N": `${nums[7]}.[][[]]^(${arrString})[${nums[4]}]`,
            "O": `${nums[6]}.[][[]]^(${arrString})[${nums[4]}]`,
            "P": `${nums[1]}.[][[]]^(${arrString})[${nums[3]}]`,
            "Q": `${nums[0]}.[][[]]^(${arrString})[${nums[3]}]`,
            "R": `(${arrString})[${nums[0]}]^(${arrString})[${nums[1]}]^(${arrString})[${nums[3]}]`,
            "S": `${nums[2]}.[][[]]^(${arrString})[${nums[3]}]`,
            "T": `${nums[5]}.[][[]]^(${arrString})[${nums[3]}]`,
            "U": `${nums[4]}.[][[]]^(${arrString})[${nums[3]}]`,
            "V": `${nums[7]}.[][[]]^(${arrString})[${nums[3]}]`,
            "W": `${nums[6]}.[][[]]^(${arrString})[${nums[3]}]`,
            "X": `${nums[2]}.[][[]]^(${arrString})[${nums[1]}]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "Y": `(${arrString})[${nums[0]}]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "Z": `${nums[0]}.[][[]]^(${arrString})[${nums[1]}]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "!": `${nums[2]}.[][[]]^(${arrString})[${nums[1]}]^(${arrString})[${nums[3]}]`,
            "\"": `${nums[1]}.[][[]]^(${arrString})[${nums[1]}]^(${arrString})[${nums[3]}]`,
            "#": `${nums[0]}.[][[]]^(${arrString})[${nums[1]}]^(${arrString})[${nums[3]}]`,
            "$": `${nums[0]}.[][[]]^${nums[4]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[3]}]`,
            "%": `${nums[1]}.[][[]]^${nums[4]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[3]}]`,
            "&": `${nums[5]}.[][[]]^(${arrString})[${nums[1]}]^(${arrString})[${nums[3]}]`,
            "'": `${nums[4]}.[][[]]^(${arrString})[${nums[1]}]^(${arrString})[${nums[3]}]`,
            "(": `${nums[0]}.[][[]]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            ")": `${nums[1]}.[][[]]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "*": `${nums[2]}.[][[]]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "+": `(${arrString})[${nums[0]}]^(${arrString})[${nums[1]}]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            ",": `${nums[4]}.[][[]]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "-": `${nums[5]}.[][[]]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            ".": `${nums[6]}.[][[]]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "/": `${nums[7]}.[][[]]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            ":": `${nums[1]}.[][[]]^(${arrString})[${nums[1]}]^(${arrString})[${nums[4]}]`,
            ";": `${nums[0]}.[][[]]^(${arrString})[${nums[1]}]^(${arrString})[${nums[4]}]`,
            "<": `${nums[0]}.[][[]]^${nums[4]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[4]}]`,
            "=": `${nums[1]}.[][[]]^${nums[4]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[4]}]`,
            ">": `${nums[5]}.[][[]]^(${arrString})[${nums[1]}]^(${arrString})[${nums[4]}]`,
            "?": `${nums[4]}.[][[]]^(${arrString})[${nums[1]}]^(${arrString})[${nums[4]}]`,
            "@": `${nums[2]}.[][[]]^(${arrString})[${nums[1]}]`,
            "[": `${nums[1]}.[][[]]^(${arrString})[${nums[1]}]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "\\": `${nums[1]}.[][[]]^${nums[4]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "]": `${nums[0]}.[][[]]^${nums[4]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "^": `${nums[4]}.[][[]]^(${arrString})[${nums[1]}]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "_": `${nums[5]}.[][[]]^(${arrString})[${nums[1]}]^(${arrString})[${nums[3]}]^(${arrString})[${nums[4]}]`,
            "`": `${nums[0]}.[][[]]^${nums[1]}.[][[]]^(${arrString})[${nums[3]}]`,
            "{": `${nums[0]}.[][[]]^${nums[2]}.[][[]]^(${arrString})[${nums[4]}]`,
            "|": `${nums[1]}.[][[]]^${nums[4]}.[][[]]^(${arrString})[${nums[4]}]`,
            "}": `${nums[0]}.[][[]]^${nums[4]}.[][[]]^(${arrString})[${nums[4]}]`,
            "~": `${nums[4]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[1]}]^(${arrString})[${nums[4]}]`,
            " ": `(${arrString})[${nums[0]}]^(${arrString})[${nums[3]}]`,
            "\t": `${nums[1]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[4]}]`,
            "\n": `${nums[2]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[4]}]`,
            "\r": `${nums[5]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[4]}]`,
            "\u000b": `(${arrString})[${nums[1]}]^(${arrString})[${nums[4]}]`,
            "\f": `${nums[4]}.[][[]]^(${arrString})[${nums[0]}]^(${arrString})[${nums[4]}]`
        };
    }

    encode(code, evalMode) {
        const cleanCode = code => code.replace(/ |\n/g, '');
        const basicEncode = code => {
            const fixMissingChar = char => `(${basicEncode('mb_chr')})(${basicEncode(char.codePointAt().toString())})`;
            return [...code].map(char => `(${this.charMapping[char] || fixMissingChar(char)})`).join('.');
        }

        if (evalMode === 'create_function') code = code.replace(/"/g, '""');

        code = basicEncode(code);

        let evalCode = '';
        switch (evalMode) {
            case 'create_function':
                const create_function = basicEncode("create_function");
                const str_getcsv = basicEncode("str_getcsv");
                const comma = basicEncode(",");
                const quote = basicEncode('"');

                evalCode = `
                (${create_function})(
                    ...(${str_getcsv})(${comma}.${quote}.(${code}).${quote})
                )()`;
                break;
            case 'assert':
                const assert_func = basicEncode('assert');
                const prefix = basicEncode('(function(){');
                const postfix = basicEncode(';return 1;})()');
                evalCode = `
                (${assert_func})(
                    (${prefix}).(${code}).(${postfix})
                )`;
            default:
                return code;
                break;
        }

        return '<?php ' + cleanCode(evalCode) + ' ?>';
    }
}