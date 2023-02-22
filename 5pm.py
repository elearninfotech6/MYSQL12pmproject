def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b


print('Welcome to Arth Operations')
print('List of Operations:')
print('1.Add')
print('2.Sub')
print('3.Mul')

choice=input('Enter Your Choice from Above: ')

m=int(input('Enter First Value: '))
n=int(input('Enter Second Value: '))

if choice=='1':
    print(add(m,n))
elif choice=='2':
    print(sub(m,n))
    
    











