group = int(input())
rooms = list(map(int, input().split()))
room = {}
for i in rooms:
    if i not in room:
        room[i]=1
    else:
        room[i]+=1
room = list(room.items())
for i,j in room:
    if j > 1:
        continue
    else:
        print(i)

'''Более медленные варианты'''
# group = int(input())
# rooms = list(map(int, input().split()))
# i = 0
# while len(rooms) >= 1:
#     room = rooms[i]
#     if rooms.count(rooms[i]) > 1:
#         while room in rooms:
#             rooms.remove(room)
#         continue
#     else:
#         print(room)
#         break
'''или'''
# group = int(input())
# rooms = list(map(int, input().split()))
# room = set(rooms)
# for i in room:
#     if rooms.count(i) > 1:
#         continue
#     if rooms.count(i) == 1:
#         print(i)

