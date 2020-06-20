import linecache

# def get_line_context(file_path, line_number):
#         return linecache.getline(file_path, line_number).strip()

# print (get_line_context('./order.csv',86754))
file = open('order.csv','r')
ret = []
for line in file.readlines()[0:100]:
        temp=line.rstrip('\n')
        temp = temp.split(',')
        ret.append(temp)
print(ret[0][0])