#.find(), .count()
#Find shows us the first appear of a caracter in the string
#count shows us the number of caracter like the parameter
#string = 'asddwqdqlwwwwwl'
#print(string.find('l'))
#print(string.count( 'l'))

while True:

    string = str(input('Type something: '))

   #if string.upper().count('EXIT') > 0: fooling with te leanguage
    if string.upper() == 'EXIT':
        break
    if string.count('_') > 0:
        print('Not Good!')
    else:
        print('Good')
