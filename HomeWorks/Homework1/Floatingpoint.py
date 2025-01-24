a = 1.0
b =  1E16
c = -1E16

d = a+(b+c)
e = (a+b)+c

print('d =', d)
print('e =', e)

if d == e:
    print('Associative')
else:
    print('Non-associative')