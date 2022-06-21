## Blog 博客项目

#### 介绍
Blog 采用django框架，simpleui后台管理界面，实现博客的相关功能

#### 软件架构
django框架，simpleui后台管理

##### [上一个版本](https://gitee.com/huang16/exampleSource/tree/master/BlogRoot)

##### [创建教程](https://gitee.com/huang16/exampleSource/tree/master/BlogRoot#%E5%88%9B%E5%BB%BA%E6%95%99%E7%A8%8B)

##### [使用说明](https://gitee.com/huang16/exampleSource/tree/master/BlogRoot#%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E)
1. 创建虚拟环境，启动环境
    PS D:>cd BlogWebsite
    PS D:\BlogWebsite> python -m venv venv
    PS D:\BlogWebsite> .\venv\Scripts\activate
2. 安装库文件
    (venv) PS D:\BlogWebsite> pip install -r .\requirement.txt
3. 数据库迁移文件
    (venv) PS D:\BlogWebsite> python .\manage.py makemigrations
    (venv) PS D:\BlogWebsite> python .\manage.py migrate
4. 创建超级用户
    (venv) PS D:\BlogWebsite> python .\manage.py createsuperuser
5. 启动项目
    (venv) PS D:\BlogWebsite> python .\manage.py runserver
