import re

# global variables 
fp_position = 0
line_count = 1
token_found = True
lexeme = ''
token_type = ''
look_ahead = ''
SYM_TAB = {}
source_file = open('sample.scala')

def printtoken(token):
    '''
    Takes a token that is returned from a scanner function and prints it to std output.
    '''
    if token:
        print ("{0:30} {1:30} {2}".format(token[1],token[0],token[2]))

def BookKeeper(lexeme):
    if lexeme in SYM_TAB.keys():
        return True
    else: 
        return False

def tokenerrorhandler(lexeme):
    global line_count
    return ("not a valid token. Error at the line number", lexeme, str(line_count))


def specialsymbol():
    '''
    Function to identify a special symbol of the program as a token.
    '''
    global lexeme
    global fp_position
    global token_type
    global token_found
    global line_count
    
    fp_position = source_file.tell()
    token_found = False
    token_type = 'Special Symbol'
    return (token_type, lexeme, str(line_count))


def constanttoken():
    '''
    Function to identify a constant in the input program as a token.
    '''
    global lexeme
    global fp_position
    global token_type
    global token_found

    c = source_file.read(1)
    if re.match('[0-9]', c):
        lexeme += c
        return constanttoken()
    elif re.match('[.]', c):
        lexeme += c
        return validateconstanttoken()
    elif c== ' 'or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'Constant'
        return (token_type, lexeme, str(line_count))
    else:
        lexeme += c
        fp_position = source_file.tell()
        return tokenerrorhandler(lexeme)
        

def validateconstanttoken():
    global lexeme
    global fp_position
    global token_type
    global token_found
    global look_ahead

    c = source_file.read(1)
    if re.match('[0-9]', c):
        lexeme += c
        return validateconstanttoken()
    elif c == ' 'or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'Constant'
        return (token_type, lexeme, str(line_count))
    elif re.match('[.]',c):
        lexeme += c
        look_ahead = source_file.read(1)
        while look_ahead not in [' ', ';', '{', '}', '(', ')', ':', ',', '=', '+', '*', '@']:
            lexeme += look_ahead
            look_ahead = source_file.read(1)
        fp_position = source_file.tell()
        fp_position = fp_position -1
        return tokenerrorhandler(lexeme)
    else:
        lexeme += c
        return tokenerrorhandler(lexeme)


def idtoken():
    '''
     Function to identify an identifier in the input program as a token.
    '''
    global lexeme
    global fp_position
    global token_type
    global token_found
    global line_count

    c = source_file.read(1)
    if re.match('[.a-z0-9]', c):
        lexeme += c
        return idtoken()
    elif c == ' 'or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme,str(line_count))
    else:
        lexeme += c
        return tokenerrorhandler(lexeme)

# to ignore commnents
def ignorecomments():
    global source_file
    global fp_position
    global line_count

    count = 0
    while source_file.read(1) != '\n':
        count += 1
        continue
    fp_position = fp_position + count + 1
    return state0()


def state0():
    global lexeme
    global line_count
    global fp_position

    source_file.seek(fp_position)
    c = source_file.read(1)
    if c == 'p':
        lexeme += c
        return state1()
    elif c == 'i':
        lexeme += c
        return state24()
    elif c == 'a':
        lexeme += c
        return state33()
    elif c == 'f':
        lexeme += c
        return state43()
    elif c == 's':
        lexeme += c
        return state52()
    elif c == 'c':
        lexeme += c
        return state58()
    elif c == 'o':
        lexeme += c
        return state66()
    elif c == 'v':
        lexeme += c
        return state73()
    elif c == 'd':
        lexeme += c
        return state76()
    elif c == 'e':
        lexeme += c
        return state79()
    elif c == 'w':
        lexeme += c
        return state83()
    elif c == 'r':
        lexeme += c
        return state88()
    elif c == 'n':
        lexeme += c
        return state96()
    elif c == 't':
        lexeme += c
        return state99()
    elif c == 'b':
        lexeme += c
        return state103()
    elif c == '<':
        lexeme += c
        return state107()
    elif c == '=':
        lexeme += c
        return state109()
    elif c == ' ':
        fp_position = fp_position + 1
        return state0()
    elif c == '\n':
        fp_position = fp_position + 1
        source_file.seek(fp_position)
        c = source_file.read(1)
        if c == '\n':
            fp_position = fp_position + 1
            line_count += 1
            return state0()
        else:
            line_count += 1
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
        token = constanttoken()
        return token

def state1():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

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
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state2():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'c':
        lexeme += c
        return state3()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state3():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'k':
        lexeme += c
        return state4()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state4():
    global lexeme
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'a':
        lexeme += c
        return state5()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state5():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'g':
        lexeme += c
        return state6()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state6():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state7()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state7():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state8():
    global lexeme
    global token_found
    global token_type
    global fp_position
    global line_count

    token_found = False
    fp_position = source_file.tell()
    fp_position = fp_position-1
    token_type = 'keyword'
    return (token_type, lexeme, str(line_count))

def state9():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'i':
        lexeme += c
        return state10()
    elif c == 'o':
        lexeme += c
        return state17()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state10():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'v':
        lexeme += c
        return state11()
    elif c == 'n':
        lexeme += c
        return state15()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state11():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'a':
        lexeme += c
        return state12()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state12():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 't':
        lexeme += c
        return state13()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state13():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state14()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state14():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state15():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 't':
        lexeme += c
        return state16()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state16():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state17():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 't':
        lexeme += c
        return state18()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state18():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state19()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state19():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'c':
        lexeme += c
        return state20()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state20():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 't':
        lexeme += c
        return state21()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state21():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state22()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state22():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'd':
        lexeme += c
        return state23()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state23():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state24():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

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
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state25():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'p':
        lexeme += c
        return state26()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state26():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'o':
        lexeme += c
        return state27()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state27():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'r':
        lexeme += c
        return state28()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state28():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 't':
        lexeme += c
        return state29()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state29():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state30():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state31():
    global lexeme
    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif c == 't':
        lexeme += c
        return state32()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token

def state32():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state33():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'b':
        lexeme += c
        return state34()
    elif c == 'n':
        lexeme += c
        return state41()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state34():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 's':
        lexeme += c
        return state35()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state35():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 't':
        lexeme += c
        return state36()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state36():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'r':
        lexeme += c
        return state37()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state37():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'a':
        lexeme += c
        return state38()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state38():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'c':
        lexeme += c
        return state39()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state39():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 't':
        lexeme += c
        return state40()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state40():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state41():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'd':
        lexeme += c
        return state42()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state42():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state43():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'i':
        lexeme += c
        return state44()
    elif c == 'a':
        lexeme += c
        return state48()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state44():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'n':
        lexeme += c
        return state45()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state45():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'a':
        lexeme += c
        return state46()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state46():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'l':
        lexeme += c
        return state47()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state47():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state48():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'l':
        lexeme += c
        return state49()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state49():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 's':
        lexeme += c
        return state50()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state50():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state51()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state51():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state52():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state53()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state53():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'a':
        lexeme += c
        return state54()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state54():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'l':
        lexeme += c
        return state55()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state55():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state56()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state56():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'd':
        lexeme += c
        return state57()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state57():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state58():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'l':
        lexeme += c
        return state59()
    elif c == 'a':
        lexeme += c
        return state63()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state59():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'a':
        lexeme += c
        return state60()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state60():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 's':
        lexeme += c
        return state61()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state61():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 's':
        lexeme += c
        return state62()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state62():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)
    

def state63():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 's':
        lexeme += c
        return state64()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state64():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state65()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state65():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state66():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'b':
        lexeme += c
        return state67()
    elif c == 'r':
        lexeme += c
        return state72()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state67():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'j':
        lexeme += c
        return state68()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state68():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state69()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state69():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'c':
        lexeme += c
        return state70()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state70():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 't':
        lexeme += c
        return state71()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state71():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state72():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state73():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'a':
        lexeme += c
        return state74()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state74():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'l':
        lexeme += c
        return state75()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state75():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state76():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state77()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state77():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'f':
        lexeme += c
        return state78()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state78():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state79():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'l':
        lexeme += c
        return state80()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state80():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 's':
        lexeme += c
        return state81()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state81():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state82()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state82():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state83():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'h':
        lexeme += c
        return state84()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state84():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'i':
        lexeme += c
        return state85()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state85():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'l':
        lexeme += c
        return state86()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state86():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state87()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state87():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state88():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state89()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state89():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 't':
        lexeme += c
        return state90()
    elif c == 'a':
        lexeme += c
        return state94()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state90():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'u':
        lexeme += c
        return state91()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state91():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'r':
        lexeme += c
        return state92()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state92():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'n':
        lexeme += c
        return state93()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state93():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state94():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'l':
        lexeme += c
        return state95()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state95():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state96():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'o':
        lexeme += c
        return state97()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state97():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 't':
        lexeme += c
        return state98()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state98():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state99():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'r':
        lexeme += c
        return state100()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state100():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'u':
        lexeme += c
        return state101()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state101():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'e':
        lexeme += c
        return state102()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state102():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state103():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'o':
        lexeme += c
        return state104()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state104():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'o':
        lexeme += c
        return state105()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state105():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == 'l':
        lexeme += c
        return state106()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        token_type = 'id'
        return (token_type, lexeme, str(line_count))
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state106():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state107():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == '=':
        lexeme += c
        return state108()
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return specialsymbol()
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state108():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)

def state109():
    global lexeme
    global line_count
    global fp_position
    global token_found
    global token_type

    c = source_file.read(1)
    if c == '>':
        lexeme += c
        return state110()
    elif c == ' ' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return specialsymbol()
    elif c == '\n': 
        fp_position = source_file.tell()
        fp_position = fp_position - 1
        token_found = False
        line_count += 1
        token_type = 'id'
        return (token_type, lexeme, str(line_count))

def state110():
    global lexeme

    c = source_file.read(1)
    if c == ' ' or c == '\n' or c == '#' or c == ';' or c == '{' or c == '}' or c == '(' or  c == ')' or c == ':' or c == ',' or c ==  "=" or c == '+' or c == '*' or c == '@':
        return state8()
    elif re.match('[.a-z0-9]', c):
        lexeme += c
        token = idtoken()
        return token
    else:
        lexeme +=c
        tokenerrorhandler(lexeme)
    
# a function to read the sequence of characters and returns a token
def scanner():
    global fp_position
    global lexeme
    global token_type
    global token_found
    token = state0()
    if BookKeeper(lexeme):
        pass
    else:
        if token_type in ['id', 'Constant']:
            SYM_TAB[lexeme] = token_type
    lexeme = ''
    token_type = ''
    token_found = True
    return token

# checking whether we reached the end of file      
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
    print('--------------------- Source Program -----------------------')
    with open('sample.scala', encoding='utf-8') as source_file:
        source_code_as_string = source_file.read()
        print(source_code_as_string)
    
    print('----------------------- Lex Output ------------------------')
    print("{0:30}{1:30}{2}".format('Token','Type','Line#'))
    
    # Call scanner to find tokens
    while not isendofinput(): 
        token = scanner()
        if token:
            printtoken(token)

    # Print the contents of the symbol table
    print('--------------------- Symbol Table -----------------------')
    for tokenkey, tokenvalue in SYM_TAB.items():
        print("|{0:15}   |  {1:>15}   |".format(tokenkey, tokenvalue))
    
if __name__ == '__main__':
    main()