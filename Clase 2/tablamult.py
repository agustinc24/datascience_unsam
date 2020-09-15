""" @author: Agustin"""

#.................TABLA DE MULTIPLICAR.....................
print('   ',end='')
for z in range(10):
    print(f'{z:>4d}',end='')

print('\n---------------------------------------------')

for a,fi in enumerate(range(0,10)):
    print(a,':',end='')
    valor=0
    print(f'{valor:>4d}',end='') 
    for fila in range(0,9) :
        valor +=fi
        print(f'{valor:>4d}',end='')
    print()
    
