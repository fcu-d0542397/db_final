import csv
from search import searchStuID
code = input('請輸入功能：')
list_test = []
count = 0
size = 0
if code == '1':
    with open('DB_students.csv',newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            list_test.append([row[0],row[1]])
        list_test = list_test[1:-1]
        list_test.sort()
        file = open('order.csv','w+') 
        for i in range(len(list_test)):
            file.write(list_test[i][0])
            file.write(',')
            file.write(list_test[i][1])
            file.write(',')
            if i==len(list_test)-1:
                file.writelines("End")
            else:
                file.write(str(i+2))
                file.writelines("\n")
elif code == '2':
    print(searchStuID(count,size))