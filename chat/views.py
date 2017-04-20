from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from myProject import settings

from .models import Chat

def chat(request):
    c = Chat.objects.all()
    return render(request, "chat/chat.html", {'home': 'active', 'chat': c})

def post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')

def messages(request):
    c = Chat.objects.all()
    return render(request, 'chat/messages.html', {'chat': c})