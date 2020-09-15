show=""
cadena=input("Ingrese una cadena para convertirla a geringoso: ")
for c in cadena:
    if c.lower()=='a': #sdfasdf
        show=show+c+"pa"
    elif c.lower()=='e':
        show=show+c+"pe"
    elif c.lower()=='i':
        show=show+c+"pi"
    elif c.lower()=='o':
        show=show+c+"po"
    elif c.lower()=='u':
        show=show+c+"pu"    
    else:               
        show=show+c
print("La cadena queda:",show)