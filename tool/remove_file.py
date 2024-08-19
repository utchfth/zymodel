# 删除图片
import os  # 导入模块


def delete_files():  # 定义函数名称
    for item in os.listdir(path):
        if item.endswith('!.jpg') or item.endswith('!.jpg.jpg'):
            os.remove(os.path.join(os.path.abspath(path), item))  # 删除符合条件的文件
            print("{} deleted.".format(item))  ##输出提示


if __name__ == '__main__':
    path = r'D:\数据集RESIDE\OTS\OTS\deleted\GT'  # 运行程序前，记得修改主文件夹路径！
    delete_files()  # 调用定义的函数，注意名称与定义的函数名一致
