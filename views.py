from django.http import HttpResponse
from django.shortcuts import render
import pyjokes as pj


def home(request):
    return render(request, 'home.html')


def neutral(request):
    neutral = ''
    neutral_joke = pj.get_joke(category='neutral')
    neutral = neutral_joke
    if neutral_joke:
        return render(request, 'neutral.html', {'neutral': neutral})
    return render(request, 'neutral.html')


def chuck(request):
    chuck = ''
    chuck_jokes = pj.get_joke(category='chuck')
    chuck = chuck_jokes
    if chuck_jokes:
        return render(request, 'chuck.html', {'chuck': chuck})

    return render(request, 'chuck.html')


def spanish(request):
    spanish = ''
    spanish_jokes = pj.get_joke(language='es')
    spanish = spanish_jokes
    if spanish_jokes:
        return render(request, 'spanish.html', {'spanish': spanish})

    return render(request, 'spanish.html')


def all(request):
    all = ''
    all_jokes = pj.get_joke(category='all')
    all = all_jokes
    if all_jokes:
        return render(request, 'all.html', {'all': all})

    return render(request, 'all.html')
