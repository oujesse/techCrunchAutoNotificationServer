from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import UserKeywords, Keywords
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    currentKeywords = []
    articlesAndWords = []
    if request.user.is_active:
        currentKeywords = request.user.userkeywords.kw.words
        articlesAndWords = zip(request.user.userkeywords.kw.articles, request.user.userkeywords.kw.matchedWords)
    return render(request, 'index.html', {'currentKeywords': currentKeywords, 'articlesAndWords': articlesAndWords})


def enterKeyword(request):
    kw = request.user.userkeywords.kw
    if request.method == 'POST':
        kw.words.append(request.POST.get("inputkeyword"))
        kw.save()
        return HttpResponseRedirect('/newsNotification/')
    return HttpResponse('u failed sorry')

def removeKeyword(request):
    kw = request.user.userkeywords.kw
    if request.method == 'POST':
        if request.POST.get("deletekeyword") in kw.words:
            kw.words.remove(request.POST.get("deletekeyword"))
            kw.save()
            return HttpResponseRedirect('/newsNotification/')
    return HttpResponse('u failed sorry')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            kw = Keywords(words=[], articles=[], matchedWords=[])
            kw.save()
            UserKeywords(kw=kw, user=user).save()
            login(request, user)
            return redirect('/newsNotification/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
