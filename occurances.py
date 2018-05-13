a_list=[2,8,3,2,3,1,2,9]
occur_dict={}
for i in a_list:
    print("Count for %s: " %i)
    print(a_list.count(i))
    x=a_list.count(i)
    occur_dict[i] = x
print("count of all values")
print(occur_dict)
