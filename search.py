import linecache
number = []
studentid = 'D000006491'
search = 0
count = 0
def read(number):
        file = open('order.csv','r')
        ret = []
        for line in file.readlines()[number:number+100]:
                # print('ret[i]')
                temp=line.rstrip('\n')
                temp = temp.split(',')
                ret.append(temp)
        file.close()
        return ret
def searchStuID(count,size):
        ret = []
        number = []
        while count < size:
                ret=read(count)
                # print(ret)
                count = count+100
                for i in range(len(ret)):
                        search = ret[i][0]
                        if studentid == search:
                                number.append(ret[i])
                                # print(ret[i])
                ret=[]
        print(number)
        return number
        
# print(searchStuID(count,3000))

