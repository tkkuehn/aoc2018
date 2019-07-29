#!/usr/bin/python3

from pyparsing import nestedExpr, delimitedList, Word, Optional

contents = []
with open('./resources/test_input.txt', 'r') as f:
    contents = f.read().splitlines()

#regex = '(' + contents[0][1:-1] + ')'
regex = '(E(NESW|W|)|WE)'


list = nestedExpr('(', ')', content=delimitedList(Word('NSEW'), delim='|') + Optional('|')).parseString(regex).asList()

print('done parsing')

print(list)
        

