from django.shortcuts import render

# Create your views here.


def test_tree(request):

    return render(request, 'tree.html')


def test_static(request):

    return render(request, 'test_static.html')