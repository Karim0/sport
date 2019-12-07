from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.http import Http404, HttpResponseRedirect
from django.db.models import Q

# def registerMemberShip(request, section_id):
#     render()


def addComment(request, article_id):
    print(13)
    try:
        txt = request.POST.get("comments_text")
        comment = Comment()
        comment.comment = txt
        comment.conn_id = article_id
        comment.typeComment = TypeComment.objects.get(id=0)
        current_user = request.user
        comment.user = current_user
        comment.save()
        return render(request, "detail.html", {"article": SportSection.objects.get(id=article_id)})
    except:
        return HttpResponse("No such articles")


def showComment(request, article_id):
    try:
        print(1)
        comments = Comment.objects.filter(conn_id=SportSection.objects.get(id=article_id))
        print(2)
        return comments
    except:
        return "No comments yet"


def index(request):
    o = SportSection.objects.all()
    for i in o:
        i.info = i.info[0:250]

    return render(request, 'index.html', {"sport_section": o})


def detail(request, article_id):
    try:
        a = SportSection.objects.get(id=article_id)
    except:
        raise Http404('The article is not found')
    comments = Comment.objects.filter(conn_id=article_id)
    print("1312312")
    print(comments)

    if request.method == 'POST':
        print("ewkere")
        try:
            txt = request.POST.get("comments_text")
            print(request.POST)
            comment = Comment(comment=txt, conn_id=SportSection.objects.get(pk=article_id),
                              user=User.objects.get(username=request.POST["username"]))
            print("14")
            comment.save()
        except:
            print('the comments cannot be added')
    return render(request, "detail.html", {"article": a, "comments": comments})


def showComments(request, article_id):
    try:
        comments = Comment.objects.filter(conn_id=article_id)
        return comments
    except:
        return "No comments yet"


def trainingSystemView(request):
    o = TrainingSystem.objects.all()
    for i in o:
        i.info = i.info[0:250]
    return render(request, 'trainingSystem.html', {"system": o})


def coachView(request):
    o = Coach.objects.all()
    for i in o:
        i.info = i.info[0:250]
    return render(request, 'coach.html', {"coach": o})  # создай страницу coaches.html

def search(request):
    try:
        if request.method == "POST":
            search_request = request.POST.get("search_field")
            if len(search_request) > 0:
                search_res = SportSection.objects.filter(
                    Q(info__contains=search_request) | Q(name__contains=search_request))
        return render(request, "search.html", {"search_res": search_res, "empty_res": "No resuslts"})
    except:
        return render(request, "search.html", {"empty_res": "No results"})


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
