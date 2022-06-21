import os
import xlwt
from openpyxl import Workbook
from django.http import StreamingHttpResponse
from Blog.settings import MEDIA_ROOT
from django.contrib import admin
from blogs import models
from blogs.resources import NavigationResource
from blogs.models import BlogUser, Article, Tag, Navigation, Comment
from import_export.admin import ImportExportModelAdmin,ExportMixin,ImportMixin
from django.utils.safestring import mark_safe
from django.utils.html import format_html

@admin.register(BlogUser)
class BlogUserAdmin(admin.ModelAdmin):
    list_per_page = 15
    fieldsets = (
        (None, {"fields": ["username", "password",'avatart']}),
        ("Personal info", {"fields": ["birth", "sex", "phone", "email"]}),
        ("Permissions", {"fields": ["is_staff", "is_active"]}),
        ("Important dates", {"fields": ["last_login", "date_joined"]}),
    )

    list_display = (
        "id",
        "username",
        'avatart',
        'avatartImg',
        "birth",
        "sex",
        "phone",
        "email",
        "last_login",
        "is_staff",
        "is_active",
        "date_joined",
    )
    list_filter = ("is_staff", "is_active")
    list_display_links = ["id", "username"]
    list_editable = ["phone", "sex", "email"]
    search_fields = ("username", "email")
    ordering = ("id",)
    def avatartImg(self, obj):
        if obj.avatart:
            href = obj.avatart.url
            src = obj.avatart.url 
            image_html = (
                '<a href="%s" target="_blank"><img src="%s" width="40px" height="40px"></a>'
                % (href, src)
            )
            return mark_safe(image_html)
        else:
            return "等待上传"
    avatartImg.short_description = "头像"
    
    actions = ["saveExcel"]
    def saveExcel(self,request,queryset):
        print("queryset:",queryset)
        for query in queryset:
            print(query)
        wb = Workbook()
        ws = wb.create_sheet(title="BlogUser",index=0)
        ws = wb.active
        columnName = ["id","username","avatart","birth","sex","phone","email","last_login","is_staff","is_active","date_joined"]
        ws.append(columnName)
        ws.sheet_properties.tabColor = '1072BA'
        rows = []
        for query in queryset:
            row = []
            row.append(query.id)
            row.append(query.username)
            row.append(str(query.avatart))
            row.append(query.birth)
            row.append(query.sex)
            row.append(query.phone)
            row.append(query.email)
            row.append(str(query.last_login))
            row.append(query.is_staff)
            row.append(query.is_active)
            row.append(str(query.date_joined))
            rows.append(row)
        for row in rows:
            ws.append(row)
        filename = "Blog.xlsx"
        filepath =  os.path.join(MEDIA_ROOT,'export')
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        filePathName = os.path.join(filepath,filename)
        print("储存路径",filepath,filePathName)
        wb.save("%s" %(filePathName))

        def file_iterator(filename,chuck_size=512):
            with open(filename,"rb") as f:
                while True:
                    c = f.read(chuck_size)
                    if c:
                        yield c
                    else:
                        break

        response = StreamingHttpResponse(file_iterator(filePathName))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
        return response
    saveExcel.short_description = "导出Excel"

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','articleViews','is_Top','is_show','show_tags','image','createTime','updateTime','articleCover']
    fieldsets = (
        (None,{'fields':['articleCover','title','body','tags','author','articleViews','createTime','updateTime']}),
        ('高级',{
        'fields':['is_Top','is_show'],
        'classes':('collapse',)
        }),
        )
    readonly_fields = ["createTime", "updateTime"]
    list_display_links = ["title"]
    list_filter = ["is_show", "createTime"]
    search_fields = ["title"]
    ordering = ['is_Top','-createTime']
    ordering = ['id']

    def image(self, obj):
        if obj.articleCover:
            href = obj.articleCover.url
            src = obj.articleCover.url
            imgName = obj.title
            image_html = (
                '<a href="%s" target="_blank" title="%s"><img src="%s" alt="%s" width="40px" height="40px"></a>'
                % (href, imgName, src, imgName)
            )
            return mark_safe(image_html)
        else:
            return "等待上传"
    image.short_description = "封面"

    def show_tags(self, obj):
        tag_list = []
        tags = obj.tags.all()
        if tags:
            for tag in tags:
                tag_list.append(tag.name)
            return ','.join(tag_list)
        else:
            return format_html('<span style="color:red;">无标签</span>')

    show_tags.short_description = 'Tags'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_per_page = 20
    fieldsets = (
        (None, {"fields":  ["blogId","commentUser","is_show"]}),
        ("Comment info", {"fields":  ["content"]}),
        ("Comment dates", {"fields":  ["createTime"]}),
    )

    list_display = ["id","commentUser","createTime","blogId","is_show","content"]
    list_filter = ["createTime"]
    search_fields = ["commentUser"]
    readonly_fields = ["createTime"]
    list_editable = ["is_show"]
    ordering = ["id"]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id",'name']
    list_display_links = ["name"]

# class NavigationAdmin(admin.ModelAdmin):
class NavigationAdmin(ImportExportModelAdmin):# 导出导入
# class NavigationAdmin(ExportMixin,admin.ModelAdmin): # 只导出，不导入
# class NavigationAdmin(ImportMixin,admin.ModelAdmin): # 只导入，不导出
    list_per_page = 40
    list_display = ["id",'name','website','is_show','joinTime','classify','describtions']
    list_display_links = ["name"]
    readonly_fields = ['joinTime']
    list_editable = ['is_show','classify']
    ordering = ['id']
    resource_class = NavigationResource
admin.site.register(Navigation,NavigationAdmin)