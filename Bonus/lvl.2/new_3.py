# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
#Написать ф-ию wave, которая будет принимать строку, 
#а возвращать список строк с такими же символами, но один из символов будет заглавным

st=input("Введите слово: ")
fin=[]
j=0
new_str=[]
while j < len(st):
    for i in st:
        new_str=list(st)
        new_str[j]=chr(ord(st[j])-32)
        fin.append(''.join(new_str))
        j+=1


print(fin)