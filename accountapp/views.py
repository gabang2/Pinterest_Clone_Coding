from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld

def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        NewHelloWorld = HelloWorld()
        NewHelloWorld.text = temp
        NewHelloWorld.save()

        HelloWorld_list = HelloWorld.objects.all

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        HelloWorld_list = HelloWorld.objects.all
        return render(request, 'accountapp/hello_world.html', context={'hello_world_input': HelloWorld_list})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm #기본적인 userform을 제공해준다.
    success_url = reverse_lazy('accountapp:hello_world') #reverse는 함수형, reverse_lazy는 class에서 사욯한다.
    template_name = 'accountapp/create.html'