from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm
from .models import Question, Statistic
# Create your views here.

def index(request):
    #redirect players to the homepage index
    return HttpResponseRedirect(reverse("game:index"))

def form_page(request):
    return render(request, 'game/form.html')

def page404(request, exception):
    return render(request, 'game/404.html')

def views_logout(request):
    logout(request)
    return redirect("game:home")

def home_page(request):
    return render(request, 'game/home.html')

def statistic_page(request):
    statistic = Statistic.objects.all()
    return render(request, 'game/statistic.html', {'stat':statistic})


@login_required
def get_stat(request):
    """Create statistic for each player include score"""
    user_id = request.user.id
    status = True
    check_id = Statistic.objects.filter(user_id=user_id)
    for check in check_id:
        print("check.id =  ", check)
        if check.user_id == user_id:
            status = False
    if User.is_authenticated and status == True:
        user = User.objects.get(pk=user_id)
        stat = Statistic(user=user)
        stat.save()
    return redirect('game:home')

def get(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            title = form.data.get('title')
            question = form.data.get('question')
            answer = form.data.get('answer')
            hint = form.data.get('hint')
            q = Question(question_title=title, question_text=question, question_answer=answer, answer_hint=hint)
            q.save()
            return redirect("game:home")

        else:
            form = QuestionForm()
    context = {'form': form}
    return render(request, 'game/home.html', context)



# def get_reply( prompt_msg ):
#       reply = input( prompt_msg )
#       return reply.lower( )
 
# # use the method
# reply = get_reply( "Do you like Python?" )
# if reply == "yes":
#     print("Good! So do I.")
# else:
#     print('Sorry. Try Javascript instead.')

