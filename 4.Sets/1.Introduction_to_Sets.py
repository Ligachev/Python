def average(array):
    array = set(array)
    j = 0
    for i in array:
        j+=i
    return j / len(array)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)