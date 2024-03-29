a = int(input('a: '))
b = int(input('b: '))
max = int(input('Max: '))

def ProblemN(a,b,max):
    for i in range(0, max+1):
        Ans = (a*a*i) + b
        print(f'({a}x{a}x{i}) + {b} = {Ans}')

ProblemN(a, b, max)