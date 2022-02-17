# coding:utf-8
"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

"""

    path()函数
        语法
            path(route,views,name=None)
            1.route: str类型，匹配请求路径
            2.views: 指定路径所对应的视图处理函数的名称
            3.name: 为地址起别名，在模板中起地址反向解析时使用
    
    path转换器
        语法： <转换器类型：自定义名>
        作用： 若转换器类型匹配到对应类型的数据，则将数据按照关键字传参的方式传递给视图函数
        例子： path('page/<int:page>', views.xxx)    
        类型：
            str匹配除了"/"之外的非空字符串
                "v1/users/<str:username>"匹配 v1/users/denglinfeng
            int匹配0或任何正整数
                "page/<int:page>"匹配 /page/100
            slug匹配任意由ascll字母或数字以及连字符和下划线组成的短标签
                "detail/<slug:sl>"匹配/detail/this-is-django
            path匹配非空字段，包括路径分隔符
                "v1/users/<path:ph>"匹配v1/goods/a/b/c
    
    re_path()函数
        在url的匹配过程中可以使用正则表达式进行精确匹配
        语法：
            re_path(reg,view,name=xxx)
            正则表达式： (?P<name>pattern)

"""

urlpatterns = [
    # path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('page/2003/', views.page_2003),  # http://127.0.0.1:8000/page/2003/
    path('page/<int:pg>', views.pagen_view),
    path('test_request', views.test_request)
]
