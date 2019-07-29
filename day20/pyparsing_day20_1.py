#!/usr/bin/python3

from pyparsing import nestedExpr, delimitedList, Word, Optional, ZeroOrMore

contents = []
with open('./resources/test_input.txt', 'r') as f:
    contents = f.read().splitlines()

#regex = contents[0][1:-1]
regex = 'W(N(NESW|W)|WE|)S'

dir_seq = Word('NESW|')
contents = delimitedList(dir_seq, delim='|')
group = nestedExpr('(', ')', content=dir_seq)

expr = ZeroOrMore(dir_seq) & ZeroOrMore(group)

#parsed = nestedExpr('(', ')', content=delimitedList(Word('NSEW'), delim='|') + Optional('|')).parseString(regex).asList()

parsed = expr.parseString(regex).asList()

print('done parsing')

print(parsed)
        

