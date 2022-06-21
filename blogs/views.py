import os
import re
import uuid
import logging
from datetime import datetime, timedelta
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Blog.settings import MEDIA_ROOT
from django.shortcuts import render, redirect
from blogs.forms import RegisterForm, LoginForm, ForgetPasswordForm
from blogs.models import BlogUser, Article, Tag, Navigation, Comment
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
logger = logging.getLogger("mydjango")

def blogIndex(request):
    logger.info("博客首页展示")
    articles = Article.objects.all()
    articlesCount = articles.count()
    # ManyToManyField
    if articles.exists():
        tagsE = articles[0].tags.all()
    today=datetime.now().date()
    yesterday=today+timedelta(days=-1)
    updateToday=Article.objects.filter(createTime__date__gt=yesterday)
    updateTodayCount=updateToday.count()
    # 进行分页，每页 10 条
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    navigationLink = Navigation.objects.all()[:18]
    popTags = Tag.objects.all()[:10]
    return render(request, "blog/index.html",locals())

def blogDetails(request):
    articleId = request.GET.get('id')
    logger.info("ID 为 %s 的""详情展示" % articleId)
    articles = Article.objects.all()
    articlesCount = articles.count()
    today=datetime.now().date()
    yesterday=today+timedelta(days=-1)
    updateToday=Article.objects.filter(createTime__date__gt=yesterday)
    updateTodayCount=updateToday.count()
    navigationLink = Navigation.objects.all()[:18]
    popTags = Tag.objects.all()[:10]
    articleDetail = Article.objects.get(id=articleId)
    articleDetail.articleViews += 1
    articleDetail.save()
    comments = Comment.objects.filter(blogId=articleId)
    return render(request, "blog/details.html",locals())

def toBlogCreation(request):
    articles = Article.objects.all()
    articlesCount = articles.count()
    today=datetime.now().date()
    yesterday=today+timedelta(days=-1)
    updateToday=Article.objects.filter(createTime__date__gt=yesterday)
    updateTodayCount=updateToday.count()
    return render(request, "blog/create.html",locals())

def blogCreation(request):
    authorId = request.session.get('userId')
    articles = Article.objects.all()
    articlesCount = articles.count()
    today=datetime.now().date()
    yesterday=today+timedelta(days=-1)
    updateToday=Article.objects.filter(createTime__date__gt=yesterday)
    updateTodayCoun=updateToday.count()
    if request.method == 'POST':
        articleTitle = request.POST.get('articleTitle')
        try:
            title = Article.objects.get(title=articleTitle)
            message = articleTitle + "已存在"
            return render(request, "blog/create.html", locals())
        except:
            print(articleTitle,"不存在")
    articleBody = request.POST.get('articleBody')
    articleTags = request.POST.get('articleTags')
    articleCover = request.FILES.get('articleCover')
    newActicle = Article()
    newActicle.title = articleTitle
    newActicle.author_id = authorId # 外键处理方式
    newActicle.body = articleBody
    tagsIdList = []
    if articleTags != "":
        articleTags = re.split(',|，',articleTags) # 每次能处理多个分隔符
        for articleTag in articleTags:
            tag = Tag.objects.filter(name=articleTag)
            if tag.exists():
                tagsIdList.append(tag[0].id)
            else:
                tag = Tag.objects.create(name=articleTag)
                tag.save()
                tagsIdList.append(tag.id)
    newActicle.articleCover = articleCover
    newActicle.save()
    newActicle.tags.set(tagsIdList)
    article = Article.objects.get(title=articleTitle)
    articleId = str(article.id)
    return redirect('/blog/blogDetails/?id='+ articleId)

def blogSearch(request):
    articles = Article.objects.all()
    articlesCount = articles.count()
    today=datetime.now().date()
    yesterday=today+timedelta(days=-1)
    updateToday=Article.objects.filter(createTime__date__gt=yesterday)
    updateTodayCount=updateToday.count()
    searchWord = request.GET.get('searchWord')
    searchResult = Article.objects.filter(title__contains=searchWord)
    searchResultCount = searchResult.count()
    return render(request, "blog/search.html",locals())

def popularTag(request):
    searchWord = request.GET.get('tag')
    if searchWord == None:
        searchWord = "所有标签"
        searchResult = Article.objects.all()
        searchResultCount = searchResult.count()
    else:
        searchResult = Article.objects.filter(tags__name=searchWord)
        searchResultCount = searchResult.count()
    articles = Article.objects.all()
    articlesCount = articles.count()
    today=datetime.now().date()
    yesterday=today+timedelta(days=-1)
    updateToday=Article.objects.filter(createTime__date__gt=yesterday)
    updateTodayCount=updateToday.count()
    navigationLink = Navigation.objects.all()[:18]
    popTags = Tag.objects.all()[:10]
    return render(request, "blog/search.html",locals())

def addComment(request):
    articles = Article.objects.all()
    articlesCount = articles.count()
    today=datetime.now().date()
    yesterday=today+timedelta(days=-1)
    updateToday=Article.objects.filter(createTime__date__gt=yesterday)
    updateTodayCount=updateToday.count()
    articleId = request.GET.get('id')
    commentContent = request.POST.get('commentContent')
    comment = Comment()
    comment.blogId_id = articleId
    comment.content = commentContent
    if request.session.get('username'):
        username = request.session.get('username')
        comment.commentUser = username
    # 管理员审核后才展示
    # comment.is_show = False
    comment.save()
    navigationLink = Navigation.objects.all()[:18]
    popTags = Tag.objects.all()[:10]
    # 博客详情信息
    articleDetail = Article.objects.get(id=articleId)
    # 博客评论信息
    comments = Comment.objects.filter(blogId=articleId)
    return render(request, "blog/details.html",locals())

def toRegister(request):
    articles = Article.objects.all()
    articlesCount = articles.count()
    today=datetime.now().date()
    yesterday=today+timedelta(days=-1)
    updateToday=Article.objects.filter(createTime__date__gt=yesterday)
    updateTodayCount=updateToday.count()
    navigationLink = Navigation.objects.all()[:18]
    popTags = Tag.objects.all()[:10]
    return render(request,"blog/register.html",locals())

def register(request):
    articles = Article.objects.all()
    articlesCount = articles.count()
    today=datetime.now().date()
    yesterday=today+timedelta(days=-1)
    updateToday=Article.objects.filter(createTime__date__gt=yesterday)
    updateTodayCount=updateToday.count()
    # 判断是否已登录
    if request.session.get('isLogin',None):
        print('You are logged in.')
        return redirect('/blog')
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        # message = "请检查填写的内容。"
        if registerForm.is_valid():
            username = registerForm.cleaned_data['username']
            password = registerForm.cleaned_data['password']
            re_password = registerForm.cleaned_data['re_password']
            email = registerForm.cleaned_data['email']
            if password != re_password:
                return render(request, "blog/register.html", locals())
            else:
                sameUser = BlogUser.objects.filter(username=username)
                if sameUser:
                    return render(request, "blog/register.html", locals())
                else:
                    newUser = BlogUser.objects.create()
                    newUser.username = username
                    newUser.password = password
                    newUser.email = email
                    newUser.save()
                    message = username + "注册成功"
                    return render(request, "blog/index.html", locals())
        else:
            message = "注册失败"
            return render(request, "blog/register.html", locals())
    if request.method == 'GET':
        registerForm = RegisterForm()
        message = "注册失败"
        return render(request, "blog/register.html", locals())

def toLogin(request):
    logger.info("去登录Blog账号")
    articles = Article.objects.all()
    articlesCount = articles.count()
    today=datetime.now().date()
    yesterday=today+timedelta(days=-1)
    updateToday=Article.objects.filter(createTime__date__gt=yesterday)
    updateTodayCount=updateToday.count()
    navigationLink = Navigation.objects.all()[:18]
    popTags = Tag.objects.all()[:10]
    return render(request,"blog/login.html",locals())

def login(request):
    articles = Article.objects.all()
    articlesCount = articles.count()
    today=datetime.now().date()
    yesterday=today+timedelta(days=-1)
    updateToday=Article.objects.filter(createTime__date__gt=yesterday)
    updateTodayCount=updateToday.count()
    # 判断是否已登录
    if request.session.get('isLogin',None):
        print('You are logged in.')
        logger.warning('You are logged in.')
        return redirect('/blog')
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        message = "请检查填写的内容！"
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']
            try:
                result = BlogUser.objects.get(username=username)
                if result.password == password:
                    request.session['isLogin']=True
                    request.session['userId'] = result.id
                    request.session['username'] = result.username
                    BlogUser.objects.filter(username=username).update(last_login=timezone.now())
                    message = "登录成功"
                    logger.info(message)
                    return redirect('/blog')
                else:
                    message = "登录失败"
                    logger.error(message)
                    return render(request, "blog/login.html", locals())
            except:
                message = username + " 用户不存在"
                logger.error(message)
                return render(request, "blog/login.html", locals())

def toLogout(request):
    if not request.session.get('isLogin',None):
        print("未登录Blog账号")
        return redirect('/blog')
    else:
        request.session.flush()
        print("已退出登录Blog账号")
    return blogIndex(request)

def toForgetPassword(request):
    articles = Article.objects.all()
    articlesCount = articles.count()
    today=datetime.now().date()
    yesterday=today+timedelta(days=-1)
    updateToday=Article.objects.filter(createTime__date__gt=yesterday)
    updateTodayCount=updateToday.count()
    navigationLink = Navigation.objects.all()[:18]
    popTags = Tag.objects.all()[:10]
    return render(request,"blog/forgetPassword.html",locals())

def forgetPassword(request):
    articles = Article.objects.all()
    articlesCount = articles.count()
    today=datetime.now().date()
    yesterday=today+timedelta(days=-1)
    updateToday=Article.objects.filter(createTime__date__gt=yesterday)
    updateTodayCount=updateToday.count()
    navigationLink = Navigation.objects.all()[:18]
    popTags = Tag.objects.all()[:10]

    if request.method == 'POST':
        forgetPasswordForm = ForgetPasswordForm(request.POST)
        message = "请检查填写的内容！"
        if forgetPasswordForm.is_valid():
            username = forgetPasswordForm.cleaned_data['username']
            password = forgetPasswordForm.cleaned_data['password']
            re_password = forgetPasswordForm.cleaned_data['re_password']
            email = forgetPasswordForm.cleaned_data['email']
            if password != re_password:
                message = username + "两次输入的密码不同"
                return render(request, "blog/forgetPassword.html", locals())
            else:
                blogUser = BlogUser.objects.get(username=username,email=email)
                blogUser.password = password
                blogUser.save()
                message = username + "密码修改成功"
                return render(request, "blog/login.html", locals())

def toPersonal(request):
    blogUserId = request.session.get("userId")
    articles = Article.objects.all()
    articlesCount = articles.count()
    today=datetime.now().date()
    yesterday=today+timedelta(days=-1)
    updateToday=Article.objects.filter(createTime__date__gt=yesterday)
    updateTodayCount=updateToday.count()
    navigationLink = Navigation.objects.all()[:18]
    popTags = Tag.objects.all()[:10]
    blogUser = BlogUser.objects.get(id=blogUserId)
    return render(request, "blog/personal.html", locals())

def updateBlogUser(request):
    articles = Article.objects.all()
    articlesCount = articles.count()
    today=datetime.now().date()
    yesterday=today+timedelta(days=-1)
    updateToday=Article.objects.filter(createTime__date__gt=yesterday)
    updateTodayCount=updateToday.count()
    blogUserId = request.GET.get('id')
    if request.method == "POST":
        blogUser = BlogUser.objects.get(id=blogUserId)
        data = request.POST
        password = data.get('password')
        email = data.get('email')
        phone = data.get('phone')
        birth = data.get('birth')
        sex = data.get('sex')
        if birth == '':
            birth = None
        blogUser.password = password
        blogUser.email = email
        blogUser.phone = phone
        blogUser.birth = birth
        blogUser.sex = sex
        blogUser.save()
        blogUser=BlogUser.objects.get(id=blogUserId)

    return render(request, "blog/personal.html", locals())

def updateHeader(request):
    articles = Article.objects.all()
    articlesCount = articles.count()
    today=datetime.now().date()
    yesterday=today+timedelta(days=-1)
    updateToday=Article.objects.filter(createTime__date__gt=yesterday)
    updateTodayCount=updateToday.count()
    blogUserId = request.session.get('userId')
    uploadImg = request.FILES.get('uploadImg')
    blogUser = BlogUser.objects.get(id=blogUserId)
    blogUser.avatart = uploadImg
    blogUser.save()
    return render(request, "blog/personal.html", locals())

def toNavigation(request):
    articles = Article.objects.all()
    articlesCount = articles.count()
    today=datetime.now().date()
    yesterday=today+timedelta(days=-1)
    updateToday=Article.objects.filter(createTime__date__gt=yesterday)
    updateTodayCount=updateToday.count()
    navigationLink = Navigation.objects.all()[:18]
    popTags = Tag.objects.all()[:10]
    navigations = Navigation.objects.all()
    navigationsCount = navigations.count()
    return render(request, "blog/navigation.html", locals())

@csrf_exempt
def uploadFile(request):
    upload = request.FILES.get('upload')
    uid = ''.join(str(uuid.uuid4()).split('-'))
    names = str(upload.name).split('.')
    names[0] = uid
    imageName = '.'.join(names)
    path = os.path.join(MEDIA_ROOT,'upload',)
    if not os.path.exists(path):
        os.makedirs(path)
    new_path = os.path.join(MEDIA_ROOT,'upload',imageName)
    with open(new_path,'wb+') as f:
        for chunk in upload.chunks():
            f.write(chunk)
    filename = imageName
    print(filename,'filename')
    url = '/mdeia/upload/'+filename
    retdata = {
        'url':url,
        'uploaded':'1',
        'filename':filename
    }
    return JsonResponse(retdata)

def page_not_found(request,exception,template_name='blog/404.html'):
 return render(request,template_name)
 
def server_error(request):
 return render(request,'blog/500.html')