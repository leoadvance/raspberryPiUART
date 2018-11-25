## 运行环境
Python 3.x

## 配置依赖库
```
pip install pyserial
```

## 调用说明
```
python3 startUARTLog.py -b xxx -p xxx
其中 
-b 波特率 默认115200 
-p 串口名称 支持模糊查找  树莓派下输入USBx MacOS下输入usbserial-x
```