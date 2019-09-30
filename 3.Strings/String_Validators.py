s=input()
boolean=[]
for i in range(len(s)):
    if s[i].isalnum() is True:
        boolean.append(True)
    else:
        boolean.append(False)
print(any(boolean))
boolean=[]

for i in range(len(s)):
    if s[i].isalpha() is True:
        boolean.append(True)
    else:
        boolean.append(False)
print(any(boolean))
boolean=[]

for i in range(len(s)):
    if s[i].isdigit() is True:
        boolean.append(True)
    else:
        boolean.append(False)
print(any(boolean))
boolean=[]

for i in range(len(s)):
    if s[i].islower() is True:
        boolean.append(True)
    else:
        boolean.append(False)
print(any(boolean))
boolean=[]

for i in range(len(s)):
    if s[i].isupper() is True:
        boolean.append(True)
    else:
        boolean.append(False)
print(any(boolean))
boolean=[]




    #
    #
    # if s[i].isalnum() is True:
    #     print(True)
    # else:
    #     print(False)
    # if s[i].isalpha() is True:
    #     print(True)
    # else:
    #     print(False)
    # if s[i].isdigit() is True:
    #     print(True)
    # else:
    #     print(False)
    # if s[i].islower() is True:
    #     print(True)
    # else:
    #     print(False)
    # if s[i].isupper() is True:
    #     print(True)
    # else:
    #     print(False)