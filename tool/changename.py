#复制图片到本文件夹并重新命名
import os.path
import shutil


def changename(img_folder,new_img_folder,num):
    for img_name in os.listdir(img_folder):  # os.listdir()： 列出路径下所有的文件
        #os.path.join() 拼接文件路径
        src = os.path.join(img_folder, img_name)   #src：要修改的目录名
        dst = os.path.join(img_folder, img_name.split('_')[0] + '!.jpg')  # dst： 修改后的目录名      注意此处str(num)将num转化为字符串,继而拼接
        abc = os.path.join(new_img_folder, img_name)
        if not os.path.exists(dst):
            num = num+1
            shutil.copy(src,abc)    #复制图像
            os.rename(abc, dst)    #重命名 用dst替代src


def main():
    img_folder0 = 'D:\数据集RESIDE\OTS\OTS\deleted\GT' #图片的文件夹路径    直接放你的文件夹路径即可
    img_folder1 = 'D:\数据集RESIDE\OTS\OTS\deleted\clear'  # 图片的文件夹路径    直接放你的文件夹路径即可
    num=1
    changename(img_folder0,img_folder1,num)

if __name__=="__main__":
    main()
