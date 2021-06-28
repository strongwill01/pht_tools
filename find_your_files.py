import os
import sys

'''
指定目录下查找文件名中包含指定字符的文件
'''

sourceDir = 'TODO 你的文件路径'
findWord = '.so'
count = 0


def search(path, word):
    for fileName in os.listdir(path):
        fp = os.path.join(path, fileName)
        if 'lib_jni' in fp or 'build' in fp:  # 过滤条件
            continue

        if os.path.isfile(fp) and word in fileName:  # 匹配条件
            global count
            count += 1
            # print(fp) # 输出全路径
            print(f'{count}、{fileName}')
        elif os.path.isdir(fp):
            search(fp, word)


if __name__ == '__main__':
    print(f'hello,find your files:')
    search(sourceDir, findWord)
    print(f'共包含：{count}个文件')
