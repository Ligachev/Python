def mutate_string(string, position, character):
    li=list(string)
    li[position]=character
    string=''.join(li)
    return string

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)

#abracadabra
#5 k