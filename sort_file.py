from pathlib import Path
import shutil
import os
print('功能：整理指定目录下文件（无后缀文件不参与归类），同类型文件将整理到同一文件夹中——from Fishquito7')

pathname = input('请输入路径：')
try:
    folder = list(Path(pathname).iterdir())
except:
    print('路径错误')
    os.system('pause')
    exit()
sfx = []
for file in folder:
    sfx.append(file.suffix)
new_lst = []
for i in sfx:
    if i not in new_lst and i != '':
        new_lst.append(i)

if new_lst == []:
    print('当前目录文件已归类')
    os.system('pause')
    exit()

print('当前目录文件未归类文件类型有：', *new_lst, '将创建文件夹进行整理')
a = input('是否继续？(y/n)\n')
if a == 'y':
    for f in new_lst:
        Path(f[1:]).mkdir(exist_ok=True)
        for file in folder:
            if file.suffix != '' and file.suffix == f:
                shutil.move(file, f[1:])
    print('已整理')
    os.system('pause')

elif a == 'n':
    print('已取消')
    os.system('pause')
else:
    print('输入错误,即将退出')
    os.system('pause')



    


