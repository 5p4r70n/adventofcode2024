#Similarity 


with open('input.txt', 'r') as f:
    data=f.read()

dataList1=[]
dataList2=[]


for i in data.split('\n'):
    # print(i)
    dataList1.append(int(i.split('   ')[0]))
    dataList2.append(int(i.split('   ')[1]))

dataMap={i:0 for i in dataList1}

for i in dataList2:
    if i in dataMap:
        dataMap[i]=dataMap[i]+1

finalvalue=0

for i in dataList1:
    finalvalue+=dataMap[i]*i

print(finalvalue)