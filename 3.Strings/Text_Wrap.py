import textwrap

def wrap(string, max_width):
    text=''
    chars = ''
    for i in string:
        chars+=i
        text+=i
        if len(chars)==max_width:
            text+='\n'
            chars=''
            continue
    return text
   
string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)