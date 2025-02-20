# # # x = int(input("Please enter the number: "))
# # # if x < 0:
# # #     x = 0
# # #     print('Negative is changed to zero', x)

# # # elif x == 0:
# # #     print("Integer is already zero")

# # # elif x == 1:
# # #     print("integer is one")


# # # # for statements
# # # list1 = ['cat', 'dog', 'elephant']

# # # for priyanshu in list1:
# # #     print(priyanshu, len(priyanshu))

# # # sample collection as dict
# # users = {
# #     "abhigyan" : "active",
# #     "manisha" : "inactive",
# #     "sabhrant" : "active"
# # }
# # print(type(users))
# # print(users)
# # for user, status in users.copy().items():
# #     if status == 'inactive':
# #         del users[user]
# # print(users)
# # active_users = {}

# # for user, status in users.items():
# #     if status == "active":
# #         active_users[user] = status

# # print(users)
# # print(active_users)


# # # range function 

# # for i in range(0, 22):
# #     print(i)

# # a = list(range(0, 22, 2))
# # type(a)

# # a = ["Marry", "has", "a", "little", "lamb"]
# # a[1]
# # for i in range(len(a)): #range(5)
# #     print(i, a[i])

# # break & continue 

# for num in range(1, 6):
#     if num == 3:
#         break
#     print(num)

# """The continue statement"""

# for i in range(1, 6):
#     if i == 4:
#         continue
#     print(i)

# contd to new class