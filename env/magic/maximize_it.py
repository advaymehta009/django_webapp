# Enter your code here. Read input from STDIN. Print output to STDOUT
'''f(x) = x**2
k list s
ith list -> N(i) elements
s = sum of f(x1)+f(x2)+....%M
'''
import itertools

'''
ll = [0 for i in range(9)]
for element in itertools.product(*somelists):
    for i in range(9):
        ll[i] = list(element)
'''

def square(x):
    return x*x


k, m = map(int, input().split())
#print(k)
#print(m)

ll = [0 for i in range(k)]
for i in range(k):
    l = list(map(int, input().split()))
    squares = list(map(square,l))
    ll[i] = squares

llc = [0 for i in range(k**2)]

a = itertools.product(for i in range(9): llc[i] ):
    
#print(ll)
#print(max(ll[1]))
#print(max(ll[0]))
print(llc)

'''sump = 0
for i in range(k):
    sump += (max(ll[i]))'''
