####将pip源设为国内源

windows
1. 打开文件资源管理器
2. 地址栏上输入%appdata%
3. 在这里面创建一个新的文件夹 pip
4. 在pip文件夹里面新建一个文件 pip.ini
内容写如下
[global]
timeout = 6000
index-url = https://mirrors.aliyun.com/pypi/simple/
trusted-host = mirrors.aliyun.com
