lst1 = [10, 20, 30, 40, 50]
lst2 = [0, 2, 4]
# method 1
# res=[]
# for item in lst2:
#     res.append(lst1[item])

# print(res)

# method 2
for i in range(len(lst2)):
    lst2[i]=lst1[lst2[i]]
    

print(lst2)