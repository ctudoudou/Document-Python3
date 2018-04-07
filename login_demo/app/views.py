from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def login(request):
    if request.POST:
        if request.POST['username'] == 'admin' and request.POST['password'] == 'admin':
            return HttpResponse('success')
        else:
            return HttpResponse('failed')

    return render(request, 'login.html')
