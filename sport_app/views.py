from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from .models import SportSection, Coach, TrainingSystem, Location
from django.http import Http404, HttpResponseRedirect


def index(request):
    o = get_list_or_404(SportSection.objects)

    return render(request, 'index.html', {"sport_section": o})


def detail(request, article_id):
    try:
        a = SportSection.objects.get(id=article_id)
    except:
        raise Http404('The article is not found')

    return render(request, 'detail.html', {'article': a})


def trainingSystemView(request):
    o = get_list_or_404(TrainingSystem.objects)
    return render(request, 'trainingSystem.html', {"system": o})


def coachView(request):
    o = get_list_or_404(Coach.objects)
    return render(request, 'coach.html', {"coach": o})  # создай страницу coaches.html


def detail(request, article_id):
    try:
        a = SportSection.objects.get(id=article_id)
    except:
        raise Http404('The article is not found')

    return render(request, 'detail.html', {'article': a})


def search(request):
    try:
        if request.method == "POST":
            search_request = request.POST.get("search_field")
            if len(search_request) > 0:
                search_res = SportSection.objects.filter(name__contains=search_request) + SportSection.objects.filter(
                    info__contains=search_request)
            return render(request, "sport_app/index.html", {"search_res": search_res, "empty_res": "No resuslts"})
    except:
        return render(request, "sport_app/index.html", {"empty_res": "No results"})


def trainingSystemView(request):
    o = get_list_or_404(TrainingSystem.objects)
    return render(request, 'trainingSystem.html', {"system": o})


def coachView(request):
    o = get_list_or_404(Coach.objects)
    return render(request, 'coach.html', {"coach": o})  # создай страницу coaches.html


def test(request):
    return HttpResponse("Hello test")


class RegistrationView(FormView):
    form_class = UserCreationForm
    success_url = '/login'

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
        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        # if self.request.session.test_cookie_worked():
        #     self.request.session.delete_test_cookie()
        return super(LoginView, self).form_valid(form)

    # def get_success_url(self):
    #     import ipdb; ipdb.set_trace()
    #     redirect_to = self.request.GET.get(self.redirect_field_name)
    #     if not is_safe_url(url=redirect_to, host=self.request.get_host()):
    #         redirect_to = self.success_url
    #     return redirect_to


def logout1(request):
    logout(request)
    return render(request, 'index.html', {})


def mainpage(request):
    return render(request, 'mainpage.html', {})
