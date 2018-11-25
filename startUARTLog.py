# coding=utf-8
# 允许带执行参数
import getopt
import sys
print("start get UART log!")


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
            if o in ("-b"):
                UARTbitrate = a
                print("bitrate: ", UARTbitrate)
    except getopt.GetoptError as err:
        print('ERROR:', err)
        sys.exit(1)

getSysPara()


