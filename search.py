import linecache
import csv

code = input('請輸入功能：')
studentid = 'D099989583'
course = '1316'
search = 0
start = 0
lineCount = 0
studentCourse = []
courseList = []
def countLine():
        count = 1
        while True:
                read = linecache.getline('order.csv',count)
                if read == '':
                        count = count - 1
                        return count
                count = count + 1
def findMin():
        lineCount = countLine()
        smallest = 'z'
        temp = '0'
        for i in range(lineCount):
                read = linecache.getline('order.csv',i+1)
                read=read.rstrip('\n')
                temp = read.split(',')
                if temp[0] < smallest:
                        smallest = temp[2]
        return int(smallest)
                
def searchStuID(count):
        read = linecache.getline('order.csv',count)
        read=read.rstrip('\n')
        temp = read.split(',')
        if temp[0] == studentid:
                studentCourse.append([temp[0],temp[1]])
        return temp[2]
def searchCourseID(count):
        read = linecache.getline('order.csv',count)
        read=read.rstrip('\n')
        temp = read.split(',')
        if temp[1] == course:
                courseList.append([temp[0],temp[1]])
        return temp[2]
def insertData(count):
        read = linecache.getline('order.csv',count)
        read = read.rstrip('\n')
        temp = read.split(',')
        return temp
        

start = findMin()
if code == '1':
        first = start
        while True:
                endFlag = searchStuID(first)
                if endFlag=='End':
                        break
                else:
                        first =int(endFlag)
        # print(studentCourse)
        for i in range(len(studentCourse)):
                print('StudentID: '+studentCourse[i][0]+' Course: '+studentCourse[i][1])
elif code == '2':
        first = start
        while True:
                endFlag = searchCourseID(first)
                if endFlag=='End':
                        break
                else:
                        first = int(endFlag)
        for i in range(len(courseList)):
                print('StudentID: '+courseList[i][0]+' Course: '+courseList[i][1])
elif code == '3':
        preLine = [0,0,0]
        first = start
        inputStuid = input('請輸入插入學號：')
        inputCourse = input('請輸入插入課號：')
        while True:
                compare = insertData(first)
                if compare[0] > inputStuid:
                        with open('order.csv','a+',newline='') as fd:
                                newData = [inputStuid,inputCourse,preLine[2]]
                                csvWriter = csv.writer(fd)
                                csvWriter.writerow(newData)
                                rows = csv.reader(fd)
                                for row in rows:
                                        if preLine[2]!='End':
                                                row[int(preLine[2])-1] = [preLine[0],preLine[1],lineCount+1]
                                csvWriter.writerow(row)
                        break
                else:
                        # print(compare[2])
                        if compare[2]!='End':
                                first = int(compare[2])
                                preLine = compare
                        else: int(preLine[2])+2
