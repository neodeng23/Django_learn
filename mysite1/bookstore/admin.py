from django.contrib import admin
from .models import Book


# Register your models here.


class BookManager(admin.ModelAdmin):
    # 列表页面显示哪些字段的列
    list_display = ['id', 'title', 'pub', 'price']

    # 控制list_display中的字段，哪些可以链接到修改页
    list_display_links = ['title']

    # 添加右侧过滤器
    list_filter = ['pub']

    # 添加搜索框[模糊查询]
    search_fields = ['title']

    # 添加可在列表页编辑的字段
    list_editable = ['price']


admin.site.register(Book, BookManager)
