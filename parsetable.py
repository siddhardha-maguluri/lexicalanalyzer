import pandas as pd

def create_parse_table():
    df = pd.DataFrame(index=['<scala>','<packages>','<imports>', '<scala-body>', 
                         '<subbody>', '<modifier>','<subbody-tail>','<tail-type>',
                         '<block>', '<stmts>', '<stmt>', '<dcl>', '<dcl-tail>',
                         '<ids>', '<more-ids>', '<type>', '<asmt>', '<if>', '<while>',
                         '<case>', '<in>', '<out>', '<return>', '<expr>', '<arith-expr>',
                         '<arith>', '<bool-expr>', '<bool>'
                        ],
                  columns=['id', 'Constant', 'package', 'import', 'abstract', 'final', 
                           'sealed', 'private', 'protected', 'class', 'object', 'val', 
                           'def', '<=', 'if', 'else', 'while', 'case', '=>', 'in', 
                           'print', 'return', 'not', 'true', 'false', 'and', 'or', 
                           'int', 'real', 'bool', ';', '{', '}', '(', ')', ':', ',', 
                           '=', '+', '*', '@','"'])

    df.loc['<scala>']['package'] = 1
    df.loc['<scala>']['import'] = 1
    df.loc['<scala>']['"'] = 1
    df.loc['<scala>']['abstract'] = 1
    df.loc['<scala>']['final'] = 1
    df.loc['<scala>']['sealed'] = 1
    df.loc['<scala>']['private'] = 1
    df.loc['<scala>']['protected'] = 1

    df.loc['<packages>']['package'] = 2

    df.loc['<packages>']['import'] = 3
    df.loc['<packages>']['"'] = 3
    df.loc['<packages>']['abstract'] = 3
    df.loc['<packages>']['final'] = 3
    df.loc['<packages>']['sealed'] = 3
    df.loc['<packages>']['private'] = 3
    df.loc['<packages>']['protected'] = 3

    df.loc['<imports>']['import'] = 4

    df.loc['<imports>']['"'] = 5
    df.loc['<imports>']['abstract'] = 5
    df.loc['<imports>']['final'] = 5
    df.loc['<imports>']['sealed'] = 5
    df.loc['<imports>']['private'] = 5
    df.loc['<imports>']['protected'] = 5

    df.loc['<scala-body>']['abstract'] = 6
    df.loc['<scala-body>']['final'] = 6
    df.loc['<scala-body>']['sealed'] = 6
    df.loc['<scala-body>']['private'] = 6
    df.loc['<scala-body>']['protected'] = 6

    df.loc['<scala-body>']['"'] = 7

    df.loc['<subbody>']['abstract'] = 8
    df.loc['<subbody>']['final'] = 8
    df.loc['<subbody>']['sealed'] = 8
    df.loc['<subbody>']['private'] = 8
    df.loc['<subbody>']['protected'] = 8

    df.loc['<modifier>']['abstract'] = 9
    df.loc['<modifier>']['final'] = 10
    df.loc['<modifier>']['sealed'] = 11
    df.loc['<modifier>']['private'] = 12
    df.loc['<modifier>']['protected'] = 13
    
    df.loc['<subbody-tail>']['class'] = 14
    df.loc['<subbody-tail>']['object'] = 14

    df.loc['<tail-type>']['class'] = 15
    df.loc['<tail-type>']['object'] = 16

    df.loc['<block>']['{'] = 17

    df.loc['<stmts>']['val'] = 18
    df.loc['<stmts>']['def'] = 18
    df.loc['<stmts>']['id'] = 18
    df.loc['<stmts>']['if'] = 18
    df.loc['<stmts>']['while'] = 18
    df.loc['<stmts>']['case'] = 18
    df.loc['<stmts>']['in'] = 18
    df.loc['<stmts>'][''] = 18
    df.loc['<stmts>']['print'] = 18
    df.loc['<stmts>']['return'] = 18
    df.loc['<stmts>']['{'] = 18

    df.loc['<stmts>']['}'] = 19

    df.loc['<stmt>']['val'] = 20
    df.loc['<stmt>']['def'] = 20

    df.loc['<stmt>']['id'] = 21
    df.loc['<stmt>']['if'] = 22
    df.loc['<stmt>']['while'] = 23
    df.loc['<stmt>']['case'] = 24
    df.loc['<stmt>']['in'] = 25
    df.loc['<stmt>']['print'] = 26
    df.loc['<stmt>']['return'] = 27
    df.loc['<stmt>']['{'] = 28

    df.loc['<dcl>']['val'] = 29
    df.loc['<dcl>']['def'] = 30

    df.loc['<dcl-tail>']['id'] = 31
    df.loc['<ids>']['id'] = 32

    df.loc['<more-ids>'][','] = 33
    df.loc['<more-ids>'][':'] = 34
    df.loc['<more-ids>'][')'] = 34

    df.loc['<type>']['int'] = 35
    df.loc['<type>']['real'] = 36
    df.loc['<type>']['bool'] = 37

    df.loc['<asmt>']['id'] = 38

    df.loc['<if>']['if'] = 39

    df.loc['<while>']['while'] = 40

    df.loc['<case>']['case'] = 41

    df.loc['<in>']['in'] = 42

    df.loc['<out>']['print'] = 43

    df.loc['<return>']['return'] = 44

    df.loc['<expr>']['id'] = 45
    df.loc['<expr>']['Constant'] = 45
    df.loc['<expr>']['('] = 45

    df.loc['<expr>']['not'] = 46
    df.loc['<expr>']['true'] = 46
    df.loc['<expr>']['false'] = 46
    df.loc['<expr>']['@'] = 46

    df.loc['<arith-expr>']['id'] = 47
    df.loc['<arith-expr>']['Constant'] = 48
    df.loc['<arith-expr>']['('] = 49

    df.loc['<arith>']['+'] = 50
    df.loc['<arith>']['*'] = 51
    df.loc['<arith>'][';'] = 52
    df.loc['<arith>'][')'] = 52
    df.loc['<arith>']['=>'] = 52
    df.loc['<arith>']['id'] = 52
    df.loc['<arith>']['Constant'] = 52
    df.loc['<arith>']['('] = 52

    df.loc['<bool-expr>']['not'] = 53
    df.loc['<bool-expr>']['true'] = 54
    df.loc['<bool-expr>']['false'] = 55
    df.loc['<bool-expr>']['@'] = 56

    df.loc['<bool>']['and'] = 57
    df.loc['<bool>']['or'] = 58
    df.loc['<bool>'][';'] = 59
    df.loc['<bool>'][')'] = 59
    df.loc['<bool>']['=>'] = 59
 
    return df
