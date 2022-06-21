from statistics import mode
from import_export import resources
from import_export.fields import Field
from blogs.models import Navigation

class NavigationResource(resources.ModelResource):
    # 自定义的列名
    id = Field(attribute='id', column_name='id')
    name = Field(attribute='name', column_name='name')
    website = Field(attribute='website',column_name=Navigation.website.field.verbose_name)
    class Meta:
        model = Navigation
        # fields是指定哪些字段需要导入
        fields = ["id",'name','website','is_show','joinTime','classify','describtions']
        # export_order是导出的字段顺序
        export_order = ['id','name','website','is_show','joinTime','describtions']
        # 导入排除字段
        # exclude = ['classify']
        # 设置主键，默认字段id
        # import_id_fields = ['id']
        # 导入数据时，若是该条数据未修改过，则会忽略
        skip_unchanged = True
        # 在导入预览页面中显示跳过的记录
        report_skipped = True
