a_list=[2,8,3,2,3,1,2,9]
dup_dict={}
count=0

for num in a_list:
    if num in dup_dict:
        count=1
        break
    else:
       count=0
if count == 1:
        print( "it has duplicates")
