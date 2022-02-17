from django.http import HttpResponse


"""
    视图函数
    专门负责接收浏览器请求，并通过http response对象返回响应的函数
    此函数可以接受浏览器请求，并根据业务逻辑返回响应的响应内容给浏览器
    语法：
        def xxx_view(request[, 其他参数....])
            return HttpResponse对象
"""


def page_2003(request):
    html = "<h1>这是第一个页面<h1>"
    return HttpResponse(html)


def pagen_view(request, pg):
    html = "<h1>这是第%s个页面<h1>"%(pg)
    return HttpResponse(html)


def test_request(request):
    # http://127.0.0.1:5000/test_request?a=1&b=1
    print("path info is ", request.path_info)
    print("method is ", request.method)
    print("querystring ", request.GET)
    return HttpResponse("test request ok")
