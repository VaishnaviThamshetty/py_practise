a_list=[2,8,3,2,3,1,2,9]
dup_dict={}

for num in a_list:
    if num in dup_dict:
        dup_dict[num] = dup_dict[num] + 1
    else:
       dup_dict[num] = 1
for num in dup_dict:
    if dup_dict[num] > 1:
        print( "number" ,num, " occurance", dup_dict[num])

