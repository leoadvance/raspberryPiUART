# coding=utf-8
# 允许带执行参数
import getopt
import sys
import os
# 时间
import time
import serial
from datetime import datetime


# UART 设备路径
DEVICE_PATH = "/dev" 
DEVICE_UART_KEY_WORD = "tty"
DIR_NAME = "./UART_Log"

class UartClass:
    def __init__(self):
        # 赋值默认名称和波特率
        self.bitrate = 115200
        self.device_name = "no_device"
        self.device_path = "null"


#  系统参数
sysPara = []


# 打印所有入口参数
argv = sys.argv[1:]
#print("argv:", argv)

def usage():
    print("-p   UART Port number")
    print("-b   UART bitrate Default value is 115200")

#   匹配文件并返回路径 path 待比较路径 name 设备名 
#   函数返回设备类路径和设备名
def findfile(path:dict(type = str, help = "路径名称"), name:str):
    # 遍历目录
    for relpath, dirs, files in os.walk(path): 
        for device_name in files:
            # 文件名包含name 且包含 UART关键字
            if (device_name.find(name) != -1) and (device_name.find(DEVICE_UART_KEY_WORD) != -1):
                full_path = os.path.join(path, relpath, device_name)
                device_path = os.path.normpath(os.path.abspath(full_path))
                #print(portPath)
                return device_path, device_name

        print("Can't find uart device! err!")
        sys.exit(1) 
        
# 获取系统参数并解析
def getSysPara():
    # 声明临时实例
    _uart_tmp = UartClass();
    try:
        # 获取参数 带:表明必须带参数 如p: -p xx
        Para, args = getopt.getopt(argv, "hp:b:", ["help"])
        # print('Para   :', Para)
        for o, a in Para:
            if o in ("-h", "--help"):
                usage()
                sys.exit(0)
            # 提取波特率    
            if o in ("-b"):
                _uart_tmp.bitrate = a
                #print("uart bitrate: ", _uart_tmp.bitrate)

            # 提取端口号
            if o in ("-p"):
                #  for name in os.listdir("/dev"):
                #     print(name)
                _uart_tmp.device_path, _uart_tmp.device_name = findfile(DEVICE_PATH, a)

                # 显示函数参数类型
                #print(findfile.__annotations__)
                #print("uart device path: ", _uart_tmp.device_name)
        # 未配置设备时停止程序        
        if _uart_tmp.device_name == "no_device":
            print("Serial port not configured！")
            sys.exit("uart cfg err!")

        return (_uart_tmp)

    except getopt.GetoptError as err:
        print('ERROR:', err)
        sys.exit(1)

# 打开串口
def open_UART(uart_para:UartClass()):
    uart_handle = serial.Serial(port = uart_para.device_path, baudrate = uart_para.bitrate)
    return(uart_handle)

# 创建log文件 
def log_file_create(uart_para:UartClass()):
    # 判断目录是否存在
    if os.path.isdir(DIR_NAME) == False:
        os.mkdir(DIR_NAME)
        print("目录不存在，创建目录:" + DIR_NAME)

    # 新建logfile 串口名+创建时间
    time_str = datetime.now().strftime("_%Y-%m-%d_%Hh%Mm%Ss")
    #print(time_str)
    return(open(DIR_NAME + "/" + uart_para.device_name + time_str + ".csv", "w"))

# 主函数
def main():
    # 声明实例
    _uart = UartClass()
    #print(_uart.device_name)
    #print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    # 解析串口波特率以及设备名
    _uart = getSysPara()
    print("start get UART log!")
    print("The directory to save the log is \"./UART_Log\"!")
    print("uart bitrate: ", _uart.bitrate)
    print("uart device path: ", _uart.device_path)
    #print("uart device name: ", _uart.device_name)

    # 打开log文件和串口
    log_file = log_file_create(_uart)
    uart_handle = open_UART(_uart)

    while(1):
        # 等待接收一行数据
        read_data = uart_handle.readline()
        # if ((read_data.decode('gb2312') != "\n") or (read_data.decode('gb2312') != "\r")):
        #if (read_data.decode('gb2312') != "\n"):
        log_date = datetime.now().strftime("%Y-%m-%d,")
        log_time = datetime.now().strftime("%H:%M:%S.%f")[:-3] + ","
        print("read_data: " + read_data.decode('gb2312') + log_date + log_time)

        # 以GB2312编码方式记录log到csv
        log_file.writelines(log_date + log_time + read_data.decode("gb2312"))
        log_file.flush()
    

if __name__ == '__main__':
    main()
    



