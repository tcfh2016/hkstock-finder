## ModuleNotFoundError: No module named 'akshare'

测试akshare接口，发现了“ModuleNotFoundError: No module named 'akshare'”错误。为啥？明明前面已经安装成功了。

查找了akshare在哪里，发现在python 3.6目录下面。这可能是因为我先在旧的Python 3.6上安装了akshare，然后再升级了Python 3.8，当前运行使用的是Python 3.8，所以找不到这个库。

[root@VM-4-4-centos usr]# find . -name "akshare"
./local/lib/python3.6/site-packages/akshare

在将Python 3默认执行3.8版本之后，重新执行`pip3 install akshare  --upgrade`，完成即可。