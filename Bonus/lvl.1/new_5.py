arr=(str(input('add numbers: '))).split(' ')
for x in range(len(arr)):
    arr[x]=int(arr[x])
i=1
while i < len(arr):
    for j in range(len(arr)-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1]=arr[j+1],arr[j]
    i+=1
print(arr)