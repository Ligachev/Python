def print_formatted(number):
    i = 1
    while i <= number:
        strA = 'in'
        strB = 'oc'
        strC = 'he'
        strD = 'bi'
        integer = i
        hexadecimal = (hex(integer)[2:]).upper()
        octal = oct(integer)[2:]
        binary = bin(integer)[2:]
        strA=strA.replace('in', str(integer))
        strB=strB.replace('oc', str(octal))
        strC=strC.replace('he', str(hexadecimal))
        strD=strD.replace('bi', str(binary))
        if number <= 1:
            strA = ' ' + strA
            strB = ' ' + strB
            strC = ' ' + strC
            strD = ' ' + strD
        if 1< number <= 3:
            strA = ' ' + strA
            strB = '  ' + strB
            strC = '  ' + strC
            if len(strD) == 1: strD = '  ' + strD
            if len(strD) == 2: strD = ' ' + strD
        if 3 < number <= 7:
            strA = '  ' + strA
            strB = '   ' + strB
            strC = '   ' + strC
            if len(strD) == 1: strD = '   ' + strD
            if len(strD) == 2: strD = '  ' + strD
            if len(strD) == 3: strD = ' ' + strD
        if 7 < number <= 15:
            if len(strA) == 1: strA = '   ' + strA
            if len(strA) == 2: strA = '  ' + strA
            if len(strB) == 1: strB = '    ' + strB
            if len(strB) == 2: strB = '   ' + strB
            strC = '    ' + strC
            if len(strD) == 1: strD = '    ' + strD
            if len(strD) == 2: strD = '   ' + strD
            if len(strD) == 3: strD = '  ' + strD
            if len(strD) == 4: strD = ' ' + strD
        if 15 < number <= 31:
            if len(strA) == 1: strA = '    ' + strA
            if len(strA) == 2: strA = '   ' + strA
            if len(strB) == 1: strB = '     ' + strB
            if len(strB) == 2: strB = '    ' + strB
            if len(strC) == 1: strC = '     ' + strC
            if len(strC) == 2: strC = '    ' + strC
            if len(strD) == 1: strD = '     ' + strD
            if len(strD) == 2: strD = '    ' + strD
            if len(strD) == 3: strD = '   ' + strD
            if len(strD) == 4: strD = '  ' + strD
            if len(strD) == 5: strD = ' ' + strD
        if 31 < number <= 63:
            if len(strA) == 1: strA = '     ' + strA
            if len(strA) == 2: strA = '    ' + strA
            if len(strB) == 1: strB = '      ' + strB
            if len(strB) == 2: strB = '     ' + strB
            if len(strC) == 1: strC = '      ' + strC
            if len(strC) == 2: strC = '     ' + strC
            if len(strD) == 1: strD = '      ' + strD
            if len(strD) == 2: strD = '     ' + strD
            if len(strD) == 3: strD = '    ' + strD
            if len(strD) == 4: strD = '   ' + strD
            if len(strD) == 5: strD = '  ' + strD
            if len(strD) == 6: strD = ' ' + strD
        if 63 < number <= 99:
            if len(strA) == 1: strA = '      ' + strA
            if len(strA) == 2: strA = '     ' + strA
            if len(strB) == 1: strB = '       ' + strB
            if len(strB) == 2: strB = '      ' + strB
            if len(strB) == 3: strB = '     ' + strB
            if len(strC) == 1: strC = '       ' + strC
            if len(strC) == 2: strC = '      ' + strC
            if len(strC) == 3: strC = '     ' + strC
            if len(strD) == 1: strD = '       ' + strD
            if len(strD) == 2: strD = '      ' + strD
            if len(strD) == 3: strD = '     ' + strD
            if len(strD) == 4: strD = '    ' + strD
            if len(strD) == 5: strD = '   ' + strD
            if len(strD) == 6: strD = '  ' + strD
            if len(strD) == 7: strD = ' ' + strD
        i+=1
        print(strA+strB+strC+strD)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)