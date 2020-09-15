frase = "todos somos programadores"
palabras = frase.split()
show=""
for palabra in palabras:
    if palabra[-1].lower() == 'o':
        show += palabra[:-1].lower() + 'e' + ' '
    elif palabra[-2] == 'o':
        show += palabra[:-2].lower() + 'e' + palabra[-1].lower() + ' '
    else:
        show+=palabra.lower()+' '
print(show.strip())