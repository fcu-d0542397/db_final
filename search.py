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
        linecache.clearcache()
        linecache.cache = {}
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
        linecache.clearcache()
        linecache.cache = {}
        for i in range(lineCount):
                read = linecache.getline('order.csv',i+1)
                read=read.rstrip('\n')
                temp = read.split(',')
                if temp[0] < smallest:
                        smallest = temp[0]
                        smallestPosition = i + 1
        return smallestPosition

def findMax():
        global lineCount
        lineCount = countLine()
        max = '0'
        temp = '0'
        maxPosition = 0
        linecache.clearcache()
        linecache.cache = {}
        for i in range(lineCount):
                read = linecache.getline('order.csv',i+1)
                read=read.rstrip('\n')
                temp = read.split(',')
                if temp[0] >= max:
                        max = temp[0]
                        maxPosition = i + 1
        return maxPosition
                
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
print(findMax())
if code == '1':
        first = start
        while True:
                endFlag = searchStuID(first)
                if endFlag=='End':
                        break
                else:
                        first = int(endFlag)
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
        preLine = ['0','0',str(start)]
        first = start
        inputStuid = input('請輸入插入學號：')
        inputCourse = input('請輸入插入課號：')
        while True:
                compare = insertData(first)
                if compare[0] > inputStuid:
                        with open('order.csv','a+',newline='') as fd:
                                # print(compare[0])
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
        inputStuid = input('請輸入刪除學號：')
        inputCourse = input('請輸入刪除課號：')
        preLine = ['0','0',str(start)]
        fix = 0
        # print(fileinput.input("order.csv", inplace=True).readline()) 
        while True:
                compare = insertData(first)
                if (compare[0] == inputStuid) & (compare[1] == inputCourse):
                        f = open('order.csv','r',buffering=1)
                        flist = f.readlines()
                        flist[int(preLine[2])-1]=''
                        f = open('order.csv','w',buffering=1)
                        f.writelines(flist)
                        f.close()
                        if(compare[2] == 'End'):
                                f = open('order.csv','r',buffering=1)
                                flist = f.readlines()
                                end = findMax()
                                newEnd =  insertData(end)
                                flist[end-1] = newEnd[0]+','+newEnd[1]+','+'End\n'
                                f = open('order.csv','w',buffering=1)
                                f.writelines(flist)
                        else:
                                fix = int(compare[2])
                                lineCount = lineCount - 1
                        break
                else:
                        if compare[2]!='End':
                                first = int(compare[2])
                                preLine = compare
                        else: 
                                print('找不到資料')
                                break

        if fix != 0:
                f = open('order.csv','r',buffering=1)
                flist = f.readlines()
                linecache.clearcache()
                linecache.cache = {}
                for i in range(lineCount):
                        compare = insertData(i + 1)
                        if (compare[2] != 'End'):
                                if (int(compare[2]) > fix ):
                                        flist[i] = compare[0]+','+compare[1]+','+str(int(compare[2])-1)+'\n'
                f = open('order.csv','w',buffering=1)
                f.writelines(flist)
                f.close()



                                 
                
                                  


        # for line in fileinput.input("order.csv", inplace=True):
        #         line = line.replace(compare[0]+','+compare[1]+','+compare[2], compare[0]+','+preLine[1]+','+str(lineCount+1))
        #         sys.stdout.write(line)


