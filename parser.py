non_terminals = ['STATEMENT', 'KONDISI', 'AKSI', 'OPERATOR', 'VARIABLE']
terminals     = ['if', 'else', 'true', 'false', 'x', 'y', ':', '>=', '<=', '=']

parse_table = {}

parse_table[('STATEMENT', 'if')] = ['if', 'KONDISI', ':', "AKSI", "else", ":", "AKSI" ]
parse_table[('STATEMENT', 'else')] = ['error']
parse_table[('STATEMENT', 'true')] = ['error']
parse_table[('STATEMENT', 'false')] = ['error']
parse_table[('STATEMENT', 'x')] = ['error']
parse_table[('STATEMENT', 'y')] = ['error']
parse_table[('STATEMENT', ':')] = ['error']
parse_table[('STATEMENT', '>=')] = ['error']
parse_table[('STATEMENT', '<=')] = ['error']
parse_table[('STATEMENT', '=')] = ['error']
parse_table[("STATEMENT", "EOS")] = ["error"]

parse_table[('KONDISI', 'if')] = ['error']
parse_table[('KONDISI', 'else')] = ['error']
parse_table[('KONDISI', 'true')] = ['true']
parse_table[('KONDISI', 'false')] = ['false']
parse_table[('KONDISI', 'x')] = ['VARIABLE', 'OPERATOR', 'VARIABLE']
parse_table[('KONDISI', 'y')] = ['VARIABLE', 'OPERATOR', 'VARIABLE']
parse_table[('KONDISI', ':')] = ['error']
parse_table[('KONDISI', '>=')] = ['error']
parse_table[('KONDISI', '<=')] = ['error']
parse_table[('KONDISI', '=')] = ['error']
parse_table[('KONDISI', "EOS")] = ["error"]

parse_table[('AKSI', 'if')] = ['error']
parse_table[('AKSI', 'else')] = ['error']
parse_table[('AKSI', 'true')] = ['error']
parse_table[('AKSI', 'false')] = ['error']
parse_table[('AKSI', 'x')] = ['VARIABLE', '=', 'VARIABLE']
parse_table[('AKSI', 'y')] = ['VARIABLE', '=', 'VARIABLE']
parse_table[('AKSI', ':')] = ['error']
parse_table[('AKSI', '>=')] = ['error']
parse_table[('AKSI', '<=')] = ['error']
parse_table[('AKSI', '=')] = ['error']
parse_table[('AKSI', "EOS")] = ["error"]

parse_table[('OPERATOR', 'if')] = ['error']
parse_table[('OPERATOR', 'else')] = ['error']
parse_table[('OPERATOR', 'true')] = ['error']
parse_table[('OPERATOR', 'false')] = ['error']
parse_table[('OPERATOR', 'x')] = ['error']
parse_table[('OPERATOR', 'y')] = ['error']
parse_table[('OPERATOR', ':')] = ['error']
parse_table[('OPERATOR', '>=')] = ['>=']
parse_table[('OPERATOR', '<=')] = ['<=']
parse_table[('OPERATOR', '=')] = ['error']
parse_table[('OPERATOR', "EOS")] = ["error"]

parse_table[('VARIABLE', 'if')] = ['error']
parse_table[('VARIABLE', 'else')] = ['error']
parse_table[('VARIABLE', 'true')] = ['error']
parse_table[('VARIABLE', 'false')] = ['error']
parse_table[('VARIABLE', 'x')] = ['x']
parse_table[('VARIABLE', 'y')] = ['y']
parse_table[('VARIABLE', ':')] = ['error']
parse_table[('VARIABLE', '>=')] = ['error']
parse_table[('VARIABLE', '<=')] = ['error']
parse_table[('VARIABLE', '=')] = ['error']
parse_table[('VARIABLE', "EOS")] = ["error"]


# Input Kalimat
print("========= PARSER =========")
print("Masukkan Token :")
no_of_lines = 5
lines = ""
for i in range(no_of_lines):
    lines+=input()+"\n"
print("==========================")
input_string = lines.lower().split()
input_string.append('EOS')

# stack initialization
stack = []
stack.append('#')
stack.append('STATEMENT')

# input reading initialization
idx_string = 0
symbol = input_string[idx_string]

# parsing process
while (len(stack) > 0):
    top = stack[len(stack)-1]
    print('top - ', top)
    print('symbol - ', symbol)
    if top in terminals:
        print('top adalah simbol terminal')
        if top == symbol:
            stack.pop()
            idx_string = idx_string + 1
            symbol = input_string[idx_string]
            if symbol == "EOS":
                print('isi stack:', stack)
                stack.pop()
        else:
            print("Error")
            break
    elif top in non_terminals:
        print('top adalah simbol non-terminal')
        if parse_table[(top, symbol)][0] != "error":
            stack.pop()
            symbols_to_be_pushed = parse_table[(top, symbol)]
            for i in range(len(symbols_to_be_pushed) - 1, -1, -1):
                stack.append(symbols_to_be_pushed[i])
        else:
            print("Error")
            break
    else:
        print("Error")
        break
    print('isi stack', stack)
    print()

# kesimpulan
# print()
if symbol == "EOS" and len(stack) == 0:
    print('Input string', input_string, '', 'diterima, sesuai Grammar')
    input_string.remove('EOS')
    for i in range(len(input_string)):
        print(input_string[i], " [ VALID ]")

else:
    print('Error, input string', input_string,
          'tidak diterima, tidak sesuai grammar')