# blog_project

基于Django框架开发的个人博客

***

预览地址 http://haozhiqing.com

先放个首页图吧

![首页图](https://dzwonsemrish7.cloudfront.net/items/282V3v3a2T3N3O2v2d0c/Jietu20180329-201638.jpg?v=10611521)

***
## 如何部署
### 新建虚拟环境
> Virtualenv 是一个 Python 工具，使用它可以创建一个独立的 Python 环境。
输入
  `pip install virtualenv`
  `virtualenv C:\Users\hzq\Envs\env`
即可建立虚拟环境
使用此命令来激活虚拟环境
  `source blogproject_env/bin/activate`
安装软件必备运行库
  `pip install -r requirements`

### 迁移数据
> 数据库使用Django内置的SQlite,所以需要将设置好的数据库模型翻译为Django的数据表
运行以下这两个语句
  `python manage.py makemigrations`
  `python manage.py migrate`
  
### 创建 Admin 后台管理员账户
> 要想进入Django Admin 后台，首先需要创建一个超级管理员账户
  `python manage.py createsuperuser`
并按照提示输入邮箱、密码等属性
接下来进入http://127.0.0.1:8000/admin/ ，就进入了到了Django Admin 后台登录页面，输入刚才创建的管理员账户密码就可以登录到后台了。

### 首页视图 
部署好后进入项目根目录执行
  `python manage.py`
接下来进入 127.0.0.1:8000 即可访问
