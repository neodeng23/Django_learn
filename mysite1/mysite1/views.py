from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

"""
    视图函数
    专门负责接收浏览器请求，并通过http response对象返回响应的函数
    此函数可以接受浏览器请求，并根据业务逻辑返回响应的响应内容给浏览器
    语法：
        def xxx_view(request[, 其他参数....])
            return HttpResponse对象
    通过request.method区分具体的请求动作
        if request.mothod == "GET":
            xxx
        elif request.mothod == "POST":
            xxx
"""

POST_FORM = '''
<form method='post' action='/test_get_post'>
    姓名:<input type="text" name="username">
    <input type='submit' value="提交">
</form>
'''


def page_2003(request):
    html = "<h1>这是第一个页面<h1>"
    return HttpResponse(html)


def pagen_view(request, pg):
    html = "<h1>这是第%s个页面<h1>" % (pg)
    return HttpResponse(html)


def test_request(request):
    # http://127.0.0.1:5000/test_request?a=1&b=1
    # print("path info is ", request.path_info)
    # print("method is ", request.method)
    # print("querystring ", request.GET)
    # print("Full path is  ", request.get_full_path())
    # print("Full message head ", request.META)
    print("remote addr ", request.META['REMOTE_ADDR'])
    return HttpResponse("test request ok")


def test_redirect(request):
    return HttpResponseRedirect("page/2003/")  # 跳转


def test_get_post(request):
    if request.method == "GET":
        print(request.GET.get("a", "no a"))  # 如果a不存在则取第二个参数为默认值
        # print(request.GET.getlist("a"))   # 如果参数是列表
        return HttpResponse(POST_FORM)
    elif request.method == "POST":
        print('uname is', request.POST['username'])
        return HttpResponse("post is ok")
    else:
        return HttpResponse("method is not correct")


def test_html_1(request):
    t = loader.get_template('test_html.html')
    html = t.render()
    return HttpResponse(html)


def test_html_2(request):
    dic = {"username": "dlf", "age": "29"}
    return render(request, 'test_html.html', dic)


def test_if_for(request):
    dic = {}
    dic['x'] = 10
    return render(request, 'test_if_for.html', dic)


def base_view(request):
    lst = ["a", "b"]
    return render(request, 'base.html', locals())


def music_view(request, nm):

    return render(request, 'music.html')


def sport_view(request):

    return render(request, 'sport.html')






