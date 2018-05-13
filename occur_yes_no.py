a_list=[2,8,3,2,3,1,2,9]
occur_dict={}
flag=0

for i in a_list:
    x=a_list.count(i)
    if x > 1:
        flag=1
        occur_dict[i] = x
if flag==1:
    print(" it has duplicates , the duplicates are")
    print(occur_dict)
else:
    print(" no  duplicates")
