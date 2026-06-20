from pathlib import Path
import shutil
import os

def get_path():
    pathname = input("请输入路径：")
    base_folder = Path(pathname)
    return base_folder


def get_suffix(base_folder):
    sfx = []
    adv_sfx = []
    try:
        for file in base_folder.iterdir():
            if file.is_file() and file.suffix != "":
                sfx.append(file.suffix.lower())
        for s in sfx:
            if s not in adv_sfx:
                adv_sfx.append(s)
        return adv_sfx
    except:
        print("路径不合法或者不存在")
        os.system("pause")
        exit()

def organize_files(base_folder, adv_sfx):
    for suffix in adv_sfx:
        folder_name = suffix[1:]
        target_folder = base_folder / folder_name
        target_folder.mkdir(exist_ok=True)
        for file in base_folder.iterdir():
            if file.is_file() and file.suffix.lower() == suffix and file.suffix.lower() != 'lnk':
                shutil.move(file, target_folder)
                print(file.name, "已移动到", target_folder)

def main():
    print("欢迎使用文件整理工具——by Fishquito7\n指定目录的同类型文件将被归类到同一文件夹中\n注意：无后缀文件不参与归类")
    print('友情提示：不要在桌面用啊！')
    base_folder = get_path()
    adv_sfx = get_suffix(base_folder)
    if adv_sfx == []:
        print("当前目录文件已归类")
        os.system("pause")
        exit()
    ask = input("是否开始整理？(y/n)：\n")
    if ask != "y":
        os.system("pause")
        exit()
    organize_files(base_folder, adv_sfx)
    print("已整理")
    os.system("pause")

if __name__ == "__main__":
    main()


            
