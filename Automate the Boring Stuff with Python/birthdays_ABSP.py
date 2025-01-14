birthdays={'Patricio':'Feb 17','Daniela':'Mar 11','Santiago':'Mar 28','Constanza':'Apr 28'}
while True:
    print('Enter a name: (blank to quit)')
    name=input()
    if name=='':
        break
    if name in birthdays:
        print(birthdays[name]+' is the birthday of '+name)
    else:
        print('I do not have birthday information for '+name)
        print('What is their birthday?')
        bday=input()
        birthdays[name]=bday
        print('Birthday database updated.')
