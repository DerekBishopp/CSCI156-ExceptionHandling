
__author__ = 'Derek'


def hopefully(ssnumber):

    try:
        x, y, z = ssnumber.split('-')
        if ssnumber == '078-05-1120':
            return 'invalid'
        if x == '000':
            return 'invalid'
        if y == '00':
            return 'invalid'
        if z == '0000':
            return 'invalid'
        if len(x) == 3 and len(y) == 2 and len(z) == 4:
            pass
        else:
            return 'invalid'
        x = int(x)
        if x == 666:
            return 'invalid'
        else:
            pass
        if x <= 899:
            pass
        else:
            return 'invalid'

    except ValueError:
        return 'invalid'



def SScheck():
    while hopefully(input('Input SS Number: ')) == 'invalid':
        print('Enter a Valid #SS')
        hopefully(input('Input SS Number: '))

SScheck()
