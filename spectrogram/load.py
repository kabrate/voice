import os  

def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
        #print(root) #当前目录路径  
        #print(dirs) #当前路径下所有子目录  
        print(files) #当前路径下所有非目录子文件
 
# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        children = os.path.join('%s%s' % (filepath, allDir))
        
if __name__ == '__main__':
    filePath = "E:\\data\\true"
    #filePathI = "D:\\FileDemo\\Python\\pt.py"
    #eachFile(filePath)
    file_name(filePath)
    #readFile(filePath)
    #writeFile(filePathI)
