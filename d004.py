print('====DESAFIO=4====')
valor=input('escolha algum caractere ou número= ')
print('{} é um número? '.format(valor))
print(valor.isnumeric())
print('É um caractere de alfabeto?',valor.isalpha())
print('É um número? ',valor.isnumeric())
print('É composto apenas por espaços?',valor.isspace())
print('É um número decimal? ',valor.isdecimal()) 
print('É um caractere composto apenas por letras minúsculas?',valor.islower())
print('É um caractere composto apenas por letras maiúsculas? ',valor.isupper())      



#==================================
