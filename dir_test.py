# import os
# import time
# def dirl():
#     size = 0
#     filescount=0
#     dirscount=0
#     for x in os.listdir('.'):       
#         timeStamp=os.path.getmtime(x)
#         timeArray=time.localtime(timeStamp)
#         timeP = time.strftime("%Y/%m/%d %H:%M",timeArray)

#         if os.path.isdir(x):
#             dirscount+=1    
#             print(timeP+'    <DIR>      '+x.lower())
#         if os.path.isfile(x):
#             filescount+=1
#             singlesize =os.path.getsize(x)
#             size += singlesize
#             print(timeP+'               '+str(singlesize)+' '+x.lower())
#     print('                 %s个文件      %d字节'%(filescount,size))
#     print('                 %s个目录       '%(dirscount))
# if __name__ == '__main__':
#     dirl()

# import os
# import time
# print(os.listdir('./__pycache__'))


import os
searchword= input('enert keyword:')
def searFile(dirname):
    dirlist=os.listdir(dirname) or []
    if len(dirlist)!=0:
        for x in dirlist:           
            join_dirname = os.path.join(dirname,x)
            if os.path.isfile(join_dirname):
                if x.find(searchword) != -1:
                    print(join_dirname)
            if os.path.isdir(join_dirname):         
                searFile(join_dirname)

if __name__ == '__main__':
    searFile('.')
    
