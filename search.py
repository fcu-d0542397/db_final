import linecache
code = input('請輸入功能：')
studentid = 'D099989583'
course = '1316'
search = 0
start = 1
studentCourse = []
courseList = []
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
if code == '1':
        while True:
                endFlag = searchStuID(start)
                if endFlag=='End':
                        break
                else:
                        start =int(endFlag)
        print(studentCourse)
        start = 1
elif code == '2':
        while True:
                endFlag = searchCourseID(start)
                if endFlag=='End':
                        break
                else:
                        start =int(endFlag)
        print(len(courseList))
        start = 1


# def read(number):
#         file = open('order.csv','r')
#         ret = []
#         for line in file.readlines()[number:number+100]:
#                 # print('ret[i]')
#                 temp=line.rstrip('\n')
#                 temp = temp.split(',')
#                 ret.append(temp)
#         file.close()
#         return ret
# def searchStuID(count,size):
#         ret = []
#         number = []
#         while count < size:
#                 ret = read(count)
#                 # print(ret)
#                 count = count + 100
#                 for i in range(len(ret)):
#                         print(ret[i])
#                         search = ret[i][0]
#                         if studentid == search:
#                                 number.append(ret[i])
#                 ret=[]
#         print(number)
#         return number
        
# print(searchStuID(count,3000))