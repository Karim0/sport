from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from .models import SportSection, Coach, TrainingSystem, Location
from django.http import Http404, HttpResponseRedirect


def index(request):
    # if request.user.is_authenticated:
    #     ctx = {"name": "123"}
    #     return render(request, 'index.html', ctx)
    # else:
    o = get_list_or_404(SportSection.objects)

    return render(request, 'index.html', {"sport_section": o})


def detail(request, article_id):
    try:
        a = SportSection.objects.get(id = article_id)
    except:
        raise Http404('The article is not found')

    return render(request, 'detail.html', {'article': a})


def trainingSystemView(request):
    o = get_list_or_404(TrainingSystem.objects)
    return render(request, 'trainingSystem.html', {"system": o})


def coachView(request):
    o = get_list_or_404(Coach.objects)
    return render(request, 'coach.html', {"coach": o})   # создай страницу coaches.html


def test(request):
    return HttpResponse("Hello test")


class RegistrationView(FormView):
    form_class = UserCreationForm
    success_url = '/'

    template_name = 'registration.html'

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationView, self).form_invalid(form)


class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = '/'

    template_name = 'login.html'

    def form_valid(self, form):
        authenticate(self.request)
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


def logout1(request):
    logout(request)
    return render(request, 'index.html', {})


