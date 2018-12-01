## 运行环境
Python 3.x

## 配置依赖库
```
pip install pyserial
```

## 调用说明
```
python3 startUARTLog.py -b xxx -p xxx &
其中 
-b 波特率 默认115200 
-p 串口名称 支持模糊查找  树莓派下输入USBx MacOS下输入usbserial-x
& 表示后台运行
```
## log说明目录
```
./UART_Log log保存目录
命名方式：串口名称+创建时间.csv
log带有时间戳，精确到ms
```
