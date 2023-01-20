## AKShare 安装

在Centos中执行`pip3 install akshare`进行安装。安装的时候可能会提示“pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.”，怎么解决？

多尝试几次就好了。

后面出现了“src/_imaging.c:75:20: fatal error: Python.h: No such file or directory”，看到官方网站上说AKShare只能支持Python3.7以上的版本，查看了本地系统是3.6，所以可能是因为Python版本不匹配导致。

于是参考[How to Install Latest Version Of Python 3 on CentOS 7](https://phoenixnap.com/kb/how-to-install-python-3-centos-7)去安装最新的Python：

首先安装一些开发供具：

```
sudo yum groupinstall "Development Tools" -y
sudo yum install gcc open-ssl-devel bzip2-devel libffi-devel -y
```

如果没有wget，那么先执行`sudo yum install wget -y`安装，因为要使用这个工具去下载Python源代码。官方推荐`3.8.13`的版本，所以我们直接下载这个版本：

```
wget https://www.python.org/ftp/python/3.8.13/Python-3.8.13.tgz
```

然后安装：

```
tar xzf Python-3.8.13.tgz
cd Python-3.8.13/
./configure --enable-optimizations
sudo make altinstall
```

当成功将Python 3.x升级到3.8.13版本之后发现之前的错误依然存在。于是不得不按照提示的“fatal error: Python.h: No such file or directory”错误重新搜索。

在[fatal error: Python.h: No such file or directory](https://stackoverflow.com/questions/21530577/fatal-error-python-h-no-such-file-or-directory)查找到答案，是因为没有安装好Python开发所需的头文件和静态库，于是执行如下命令安装：

```
sudo yum install python3-devel
```

重新执行`sudo pip3 install akshare`安装就成功了。


参考：

- [AKShare 安装指导](https://www.akshare.xyz/installation.html)
- [How to Install Latest Version Of Python 3 on CentOS 7](https://phoenixnap.com/kb/how-to-install-python-3-centos-7)
- [fatal error: Python.h: No such file or directory](https://stackoverflow.com/questions/21530577/fatal-error-python-h-no-such-file-or-directory)


## ModuleNotFoundError: No module named 'akshare'

测试akshare接口，发现了“ModuleNotFoundError: No module named 'akshare'”错误。为啥？明明前面已经安装成功了。

查找了akshare在哪里，发现在python 3.6目录下面。这可能是因为我先在旧的Python 3.6上安装了akshare，然后再升级了Python 3.8，当前运行使用的是Python 3.8，所以找不到这个库。

[root@VM-4-4-centos usr]# find . -name "akshare"
./local/lib/python3.6/site-packages/akshare

在将Python 3默认执行3.8版本之后，重新执行`pip3 install akshare  --upgrade`，完成即可。