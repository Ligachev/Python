count_eng_stud = int(input())
eng_stud = set(map(int, input().split()))
count_fra_stud = int(input())
fra_stud = set(map(int, input().split()))

students = eng_stud - fra_stud
print(len(students))