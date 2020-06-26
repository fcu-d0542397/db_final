import linecache
import csv
import sys
import fileinput

code = input('請輸入功能：')
studentid = 'D0999983'
course = '2133'
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
        global lineCount
        lineCount = countLine()
        smallest = 'z'
        temp = '0'
        smallestPosition = 0
        for i in range(lineCount):
                read = linecache.getline('order.csv',i+1)
                read=read.rstrip('\n')
                temp = read.split(',')
                if temp[0] < smallest:
                        smallest = temp[0]
                        smallestPosition = i + 1
        return smallestPosition
                
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
        preLine = ['0','0','0']
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
                        for line in fileinput.input("order.csv", inplace=True):
                                line = line.replace(preLine[0]+','+preLine[1]+','+preLine[2], preLine[0]+','+preLine[1]+','+str(lineCount+1))
                                sys.stdout.write(line)
                        break
                else:
                        if compare[2]!='End':
                                first = int(compare[2])
                                preLine = compare
                        else: 
                                with open('order.csv','a+',newline='') as fd:
                                        newData = [inputStuid,inputCourse,'End']
                                        csvWriter = csv.writer(fd)
                                        csvWriter.writerow(newData)
                                        rows = csv.reader(fd)
                                for line in fileinput.input("order.csv", inplace=True,backup="",bufsize=1):
                                        line = line.replace(compare[0]+','+compare[1]+','+compare[2], preLine[0]+','+preLine[1]+','+str(lineCount+1))
                                        sys.stdout.write(line)
                                break
elif code == '4':
        first = start
        inputStuid = 'D000003506'
        inputCourse = '2171'
        preLine = ['0','0','0']
        # print(fileinput.input("order.csv", inplace=True).readline()) 
        while True:
                compare = insertData(first)
                # if (compare[0] == inputStuid) & (compare[1] == inputCourse):
                #         if preLine == ['0','0','0']:
                #                 for line in fileinput.input("order.csv",inplace=False,backup="",bufsize=1024):
                #                         line = line.replace(compare[0]+','+compare[1]+','+compare[2],'')
                #                         sys.stdout.write(line)
                #                         break
                #         else: 
                                 
                
                                  


        # for line in fileinput.input("order.csv", inplace=True):
        #         line = line.replace(compare[0]+','+compare[1]+','+compare[2], compare[0]+','+preLine[1]+','+str(lineCount+1))
        #         sys.stdout.write(line)


