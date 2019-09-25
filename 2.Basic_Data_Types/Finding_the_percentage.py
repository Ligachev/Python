students=[]
stud_key = []
stud_value = []
stud_assess = {}
n=int(input('Укажите колличество учеников: '))
for k in range(n):
    students.append(input('Введите имя и оценки ученика: ').split(' '))
for i in students:
    stud_key.append(i.pop(0))
    o=0
    for j in i:
        o+=float(j)
    stud_value.append(o/3)
stud_assess=dict(zip(stud_key, stud_value))

print(format(stud_assess.get(input('Назовите ученика: ')),'.2f'))
