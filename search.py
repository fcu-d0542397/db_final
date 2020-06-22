import linecache

# def get_line_context(file_path, line_number):
#         return linecache.getline(file_path, line_number).strip()

# print (get_line_context('./order.csv',86754))
# file = open('order.csv','r')
ret = []
number = []
studentid = 'D000006491'
search = 0
count = 0
def read(number):
        file = open('order.csv','r')
        for line in file.readlines()[number:number+10]:
                # print('ret[i]')
                temp=line.rstrip('\n')
                temp = temp.split(',')
                ret.append(temp)
        file.close()

# for i in range(50):
#         file = open('order.csv','r')
#         for line in file.readlines()[i:i+10]:
#                 # print('ret[i]')
#                 temp=line.rstrip('\n')
#                 temp = temp.split(',')
#                 ret.append(temp)
#         file.close()

while count < 3000:
        read(count)
        count = count+10
        for i in range(len(ret)):
                search = ret[i][0]
                if studentid == search:
                        number.append(ret[i])
        ret=[]
print(number)