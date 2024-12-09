
with open('input.txt', 'r') as f:
    data=f.read()

dataList1=[]
dataList2=[]


for i in data.split('\n'):
    # print(i)
    dataList1.append(int(i.split('   ')[0]))
    dataList2.append(int(i.split('   ')[1]))


dataList1=sorted(dataList1)
dataList2=sorted(dataList2)


finalvalue=0

for i,j in zip(dataList1,dataList2):

    print(i,j)

    if i>=j:
        finalvalue = finalvalue + (i-j)
    else:
        finalvalue = finalvalue + (j-i)    

print(finalvalue)