#复制图片到新的文件夹并重新命名
import os  # os是用来切换路径和创建文件夹的。
import shutil  # shutil 是用来复制黏贴文件的


def rename(path,new_path,i):
    for item in os.listdir(path):
        if item.endswith('!.jpg') :
            src = os.path.join(os.path.abspath(path), item)
            dst = os.path.join(os.path.abspath(new_path),item)
            new_name = os.path.join(os.path.abspath(new_path),item.split('!')[0] + '.jpg')
            #复制图像
            shutil.copy(src,dst)
            #重命名
            os.rename(dst, new_name)
            i += 1

            print(src)
            print(new_name)


def main():
    img_folder0 = 'D:\数据集RESIDE\OTS\OTS\deleted\GT'  # 图片的文件夹路径    直接放你的文件夹路径即可
    img_folder1 = 'D:\数据集RESIDE\OTS\OTS\deleted\clear'  # 图片的文件夹路径    直接放你的文件夹路径即可
    num = 1
    rename(img_folder0, img_folder1, num)

if __name__ == "__main__":
    main()

