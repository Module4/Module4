from django.http import HttpResponse
from django.shortcuts import render


def lesson_4(request):
    return HttpResponse('Домашка по 4 занятию')
