def greet (lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet1 = greet('en')
greet2 = greet('es')
greet3 = greet('fr')

print(greet1, greet2, greet3)