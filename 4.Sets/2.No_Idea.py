def happiness_counter(arr, set_A, set_B):
    count_happy = 0
    for i in arr:
        if i in set_A and i in set_B:
          continue
        if i in set_A and i not in set_B:
            count_happy+=1
        if i not in set_A and i in set_B:
            count_happy-=1
        else:
            continue
    return count_happy

n_m = list(map(int, input().split()))
arr = list(map(int, input().split()))
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

happy = happiness_counter(arr, set_A, set_B)
print(happy)