from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("HelloWorld")


def get_from_path(request, number):
    return HttpResponse(f"Число {number}")


def reg_meth(request, year):
    return HttpResponse(f"year = {year}")


def get_from_query(request):
    if request.GET:
        print(request.GET)
    return HttpResponse("Запрос с параметрами")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def raise_if_less_15(request, number):
    if number < 15:
        raise Http404()
    return HttpResponse(f"Число {number}")


def redirect_page(request):
    return redirect('home')
