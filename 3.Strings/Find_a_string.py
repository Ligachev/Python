def count_substring(a, b):
    coun = 0
    for i in range(len(a)):
        if a[i:len(b)+i]==b:
            coun+=1
    return coun

string = input().strip()
sub_string = input().strip()
count = count_substring(string, sub_string)
print(count)