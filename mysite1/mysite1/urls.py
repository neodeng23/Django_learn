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
from django.urls import include, path, reverse
from . import views

"""
    URL出现位置：
        1.模板（html）中
            <a href='url'>超链接</a>
        2.视图函数中 302跳转
            HttpResponseRedirect('url')
            
        书写规范
            1.绝对地址
            2.相对地址
                1./开头的相对地址，浏览器会把当前地址栏的协议，ip和端口号加上这个地址，作为最终访问地址
                2.没有/开头的相对地址，浏览器会根据当前url的最后一个/之前的内容，加上该相对地址，作为最终访问地址
                {% url '别名' %}
                {% url '别名' '参数值1' '参数2' %}
                ex:
                {% url 'pagen' '400' %}
                {% url 'person' age='18' name='dlf' %}

    path()函数
        语法
            path(route,views,name=None)
            1.route: str类型，匹配请求路径
            2.views: 指定路径所对应的视图处理函数的名称
            3.name: 为地址起别名，在模板中起地址反向解析时使用
                反向解析是指在视图或模板中，用path定义的名称来动态查找或计算出相应的路由
                根据path中的name=”关键词“传参给url确定了个唯一确定的名字，在模板或视图中，可以通过这个名字反向推断出此url的信息
                可以调用用reverse方法进行反向解析，将别名转换为url
                    reverse("别名", args=[], kwargs={})
    
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
    path('test_request', views.test_request),
    path('test_get_post', views.test_get_post),
    path('test_html1', views.test_html_1),
    path('test_html2', views.test_html_2),
    path('test_if_for', views.test_if_for),
    path('base_index', views.base_view, name="base"),
    path('music_index/<int:nm>', views.music_view, name='ms'),
    path('sport_index', views.sport_view),

    path('music/', include('music.urls')),  # 将应用中的子路由添加到主路由中

]
