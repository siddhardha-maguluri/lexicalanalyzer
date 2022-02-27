from operator import le
import re

# global variables 
fp_position = 0
token_found = True
lexeme = ''
token_type = ''
source_file = open('sample.scala')

def errorhandler(lexeme):
    print(f'error: {lexeme} not a valid token.')

def specialsymbol():
    global lexeme
    global fp_position
    global token_type
    global token_found

    c = source_file.read(1)
    if c =='\n' or c ==' ' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'Special Symbol'
        return (token_type, lexeme)

def constanttoken():
    global lexeme
    global fp_position
    global token_type
    global token_found

    c = source_file.read(1)
    if re.match('[0-9]', c):
        lexeme += c
        return constanttoken()
    else:
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = ''
        return (token_type, lexeme)

def idtoken():
    global lexeme
    global fp_position
    global token_type
    global token_found

    c = source_file.read(1)
    if re.match('[.a-z0-9]', c):
        lexeme += c
        return idtoken()
    elif c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme)

def ignorecomments():
    global source_file
    global fp_position

    count = 0
    while source_file.read(1) != '\n':
        count += 1
        continue
    fp_position = fp_position + count + 1
    return state0()

def state0():
    global lexeme
    global fp_position
    source_file.seek(fp_position)
    c = source_file.read(1)
    if c == 'p':
        lexeme += c
        return state1()
    elif c == 'i':
        lexeme += c
        return state24()
    elif c == ' ' or c == '\n':
        fp_position = fp_position + 1
        return state0()
    elif c == '#':
        return ignorecomments()
    elif c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        lexeme += c
        specialtoken = specialsymbol()
        return specialtoken
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token
    elif re.match('[0-9]', c):
        lexeme += c
        return constanttoken()

def state1():
    global lexeme
    c = source_file.read(1)
    if c == 'a':
        lexeme += c
        return state2()
    elif c == 'r':
        lexeme += c
        return state9()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif  c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        global fp_position
        global token_found
        global token_type
        
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme)

def state2():
    global lexeme
    c = source_file.read(1)
    if c == 'c':
        lexeme += c
        return state3()
    elif re.match('[a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token

def state3():
    global lexeme
    c = source_file.read(1)
    if c == 'k':
        lexeme += c
        return state4()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        global fp_position
        global token_found
        global token_type
        
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme)

def state4():
    global lexeme
    c = source_file.read(1)
    if c == 'a':
        lexeme += c
        return state5()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state5():
    global lexeme
    c = source_file.read(1)
    if c == 'g':
        lexeme += c
        return state6()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state6():
    global lexeme
    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state7()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state7():
    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state8():
    global lexeme
    global token_found
    global token_type
    global fp_position

    token_found = False
    fp_position = source_file.tell()
    fp_position = fp_position-1
    token_type = 'keyword'
    return (token_type, lexeme)

def state9():
    global lexeme
    c = source_file.read(1)
    if c == 'i':
        lexeme += c
        return state10()
    elif c == 'o':
        lexeme += c
        return state17()
    elif c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state10():
    global lexeme
    c = source_file.read(1)
    if c == 'v':
        lexeme += c
        return state11()
    elif c == 'n':
        lexeme += c
        return state15()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state11():
    global lexeme
    c = source_file.read(1)
    if c == 'a':
        lexeme += c
        return state12()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state12():
    global lexeme
    c = source_file.read(1)
    if c == 't':
        lexeme += c
        return state13()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state13():
    global lexeme
    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state14()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state14():
    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state15():
    global lexeme
    c = source_file.read(1)
    if c == 't':
        lexeme += c
        return state16()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state16():
    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state17():
    global lexeme
    c = source_file.read(1)
    if c == 't':
        lexeme += c
        return state18()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state18():
    global lexeme
    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state19()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state19():
    global lexeme
    c = source_file.read(1)
    if c == 'c':
        lexeme += c
        return state20()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state20():
    global lexeme
    c = source_file.read(1)
    if c == 't':
        lexeme += c
        return state21()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state21():
    global lexeme
    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state22()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state22():
    global lexeme
    c = source_file.read(1)
    if c == 'd':
        lexeme += c
        return state23()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state23():
    global lexeme
    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        global fp_position
        global token_found
        global token_type
        
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme)

def state24():
    global lexeme
    c = source_file.read(1)
    if c == 'm':
        lexeme += c
        return state25()
    elif c == 'f':
        lexeme += c
        return state30()
    elif c == 'n':
        lexeme += c
        return state31()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state25():
    global lexeme
    c = source_file.read(1)
    if c == 'p':
        lexeme += c
        return state26()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state26():
    global lexeme
    c = source_file.read(1)
    if c == 'o':
        lexeme += c
        return state27()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state27():
    global lexeme
    c = source_file.read(1)
    if c == 'r':
        lexeme += c
        return state28()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state28():
    global lexeme
    c = source_file.read(1)
    if c == 't':
        lexeme += c
        return state29()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state29():
    global lexeme
    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state30():
    global lexeme
    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state31():
    global lexeme
    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif c == 't':
        lexeme += c
        return state32()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token

def state32():
    global lexeme
    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[a-z]', c):
        lexeme += c
        token = idtoken()
        return token


# def state15():
#     global lexeme
#     global token_found
#     global token_type
#     global fp_position
    
#     token_found = False
#     fp_position = source_file.tell()
#     fp_position = fp_position-1
#     token_type = 'keyword'
#     return (token_type, lexeme)
    
def scanner():
    #source_file = open('sample.scala')
    global fp_position
    global lexeme
    global token_type
    global token_found
    token = state0()
    lexeme = ''
    token_type = ''
    token_found = True
    return token
           
def printtoken(token):
    if token :
        print(token[1]+ "\t\t\t\t\t"+token[0])

def isendofinput():
    file = open('sample.scala')
    file.seek(fp_position)
    eof = file.read(1)
    if eof == '':
        return True
    else:
        return False

def main():
    # read the file name from command line and print contents of the file to std output
    with open('sample.scala', encoding='utf-8') as source_file:
        source_code_as_string = source_file.read()
        print(source_code_as_string)

    print("Token\t\t\t\t\t" + "type\t\t\t\t\t" + "line#\t\t\t")
    
    # Call scanner to find tokens
    while not isendofinput(): 
        token = scanner()
        printtoken(token)
    
    print('All tokens are identified')

if __name__ == '__main__':
    main()



# doubts and questions 
# how many times do we need to call scanner function. 
# state 50 is identifier
#
#
#
#
#
#