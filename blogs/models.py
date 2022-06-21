from django.db import models
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField

# 博客用户
class BlogUser(models.Model):
    gender = (("male", "男"),("female", "女"),)

    username = models.CharField(
        verbose_name="username",
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    password = models.CharField(verbose_name="password", max_length=150)
    avatart=models.FileField(verbose_name="avatart image",upload_to='images/Avatart/%Y/%m/%d',blank=True,null=True)
    birth = models.DateField(verbose_name="birth", blank=True, null=True)
    sex = models.CharField(verbose_name="sex", max_length=20, choices=gender, blank=True)
    email = models.EmailField(verbose_name="email address", blank=True)
    phone = models.CharField(verbose_name="phone", max_length=11, blank=True)
    last_login = models.DateTimeField(verbose_name="last_login", default=now)
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as active. "
        "Unselect this instead of deleting accounts.",
    )
    date_joined = models.DateTimeField(verbose_name="date joined", default=now)

    class Meta:
        db_table = "blogUser"
        verbose_name = "账户"
        verbose_name_plural = "账户"

    def __str__(self) -> str:
        return self.username

# 博客文章
class Article(models.Model):
    articleCover = models.FileField(verbose_name="封面", upload_to='images/Article/%Y/%m/%d')
    title = models.CharField(verbose_name="标题",max_length=200,unique=True)
    # body = models.TextField(verbose_name="正文")
    body = RichTextUploadingField(verbose_name="正文",blank=True,null=True)
    tags = models.ManyToManyField("Tag", verbose_name="标签", blank=True)
    author = models.ForeignKey("BlogUser", verbose_name="作者", on_delete=models.SET_NULL, null=True)
    articleViews = models.PositiveIntegerField(verbose_name="访问量",default=0)
    is_Top = models.BooleanField(verbose_name="是否置顶",default=False)
    is_show = models.BooleanField(verbose_name="是否展示",default=True)
    createTime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updateTime = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        db_table = "article"
        verbose_name = "文章"
        verbose_name_plural = "文章"

    def __str__(self) -> str:
        return self.title

# 博客评论
class Comment(models.Model):
    content = RichTextUploadingField(verbose_name="评论内容")
    commentUser = models.CharField(verbose_name='评论人',max_length=150,default="nobody",blank=True,null=True)
    blogId = models.ForeignKey("Article",verbose_name="博客id",on_delete=models.CASCADE)
    createTime = models.DateTimeField(verbose_name="评论时间", auto_now_add=True)
    is_show = models.BooleanField(verbose_name="是否展示",default=True)

    class Meta:
        db_table = "comment"
        verbose_name = "评论"
        verbose_name_plural = "评论"

# 标签
class Tag(models.Model):
    name = models.CharField(verbose_name='标签',max_length=50,unique=True)

    class Meta:
        db_table = "tags"
        verbose_name = "标签"
        verbose_name_plural = "标签"
    
    def __str__(self) -> str:
        return self.name

# 导航表
class Navigation(models.Model):
    choice = (('navigation','导航'),('film','影视'),('music','音乐'),('picture','图片'),('entertainment','娱乐'),
    ('programming','编程'),('learning','学习'),('game','游戏'),('download','下载'),('tips','小技巧'),('other','其他'))
    name = models.CharField(verbose_name="websitName",max_length=200)
    website = models.URLField(verbose_name="website")
    joinTime = models.DateTimeField(verbose_name="joinTime", auto_now_add=True)
    classify = models.CharField(verbose_name="classify",max_length=100,choices = choice, blank=True,null=True)
    is_show = models.BooleanField(verbose_name="isShow",default=True)
    describtions = models.TextField(verbose_name="describtions",blank=True,null=True)

    class Meta:
        db_table = "navigation"
        verbose_name = "导航"
        verbose_name_plural = "导航"

    def __str__(self) -> str:
        return self.name
