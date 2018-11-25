# coding=utf-8
# 允许带执行参数
import getopt
import sys
import os
print("start get UART log!")

# UART 设备路径
DEVICE_PATH = "/dev" 
DEVICE_UART_KEY_WORD = "tty"
#  系统参数
sysPara = []

# 默认参数 波特率 端口号
UARTbitrate = 115200
UARTport = "ttyUSB0"

# 打印所有入口参数
argv = sys.argv[1:]
print("argv:", argv)

def usage():
    print("-p   UART Port number")
    print("-b   UART bitrate Default value is 115200")

#   匹配文件并返回路径
def findfile(path, name):
    # 遍历目录
    for relpath, dirs, files in os.walk(path): 

        for filename in files:

            # 文件名包含name 且包含 UART关键字
            if (filename.find(name) != -1) and (filename.find(DEVICE_UART_KEY_WORD) != -1):
                full_path = os.path.join(path, relpath, filename)
                portPath = os.path.normpath(os.path.abspath(full_path))
                #print(portPath)
                return portPath

        print("Can't find UART! err!")
        sys.exit(1) 
# 获取系统参数并解析
def getSysPara():
    try:
        # 获取参数 带:表明必须带参数 如p: -p xx
        Para, args = getopt.getopt(argv, "hp:b:", ["help"])
        print('Para   :', Para)
        for o, a in Para:
            if o in ("-h", "--help"):
                usage()
                sys.exit(0)
            # 提取波特率    
            if o in ("-b"):
                UARTbitrate = a
                print("bitrate: ", UARTbitrate)

            # 提取端口号
            if o in ("-p"):
                #  for name in os.listdir("/dev"):
                #     print(name)
                UARTport = findfile(DEVICE_PATH, a)
                print("UARTportPath: ", UARTport)

    except getopt.GetoptError as err:
        print('ERROR:', err)
        sys.exit(1)

getSysPara()


