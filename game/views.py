from random import sample
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .forms import QuestionForm, AnswerForm
from .models import Question, Statistic, Topic, Answer, Best_score, UserPicture
import logging

# Create your views here.

logger = logging.getLogger('thor')

def get_client_ip(request):
    get_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if get_ip:
        ip = get_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    """Redirect to index page."""
    if str(request.user) == 'AnonymousUser':
        client_ip = get_client_ip(request)
        logger.error('Access from {}'.format(client_ip))
    return HttpResponseRedirect(reverse("game:index"))


def page404(request, exception):
    """Redirect to 404 page."""
    client_ip = get_client_ip(request)
    logger.error('response status code 404 from {}'.format(client_ip))
    return render(request, 'game/404.html')

def views_logout(request):
    """User logout and redirect to homepage."""
    user = request.user
    client_ip = get_client_ip(request)
    logger.info('Logout from {}'.format(user))
    logout(request)
    return redirect("game:home")

def home_page(request, error: str=''):
    user = request.user
    """Redirect to homepage."""
    if str(request.user) == 'AnonymousUser':
        client_ip = get_client_ip(request)
        logger.error('Access from {}'.format(client_ip))
    else:
        logger.info('Access from {}'.format(user))
    topic = Topic.objects.all()
    all_best_score = Best_score.objects.order_by('-value')
    return render(request, 'game/home.html', {'all_topic': topic, 'best': all_best_score, 'number': range(1, 11), 'super_user': error})

@login_required
def form_page(request):
    """Redirect to Add Question Form page."""
    user = request.user
    if str(request.user) == 'AnonymousUser':
        client_ip = get_client_ip(request)
        logger.error('Try to access from {}'.format(client_ip))
    logger.info('Access from {}'.format(user))
    form = QuestionForm()
    context = {'form': form}
    return render(request, 'game/form.html', context)

@login_required
def statistic_page(request):
    user = request.user
    client_ip = get_client_ip(request)
    if str(request.user) == 'AnonymousUser':
        logger.error('Try to access from {}'.format(client_ip))
    logger.info('Access from {}'.format(user))
    statistic = get_object_or_404(Statistic, user=request.user)
    picture = get_object_or_404(UserPicture, user=request.user)
    score_for_user = Best_score.objects.filter(user=request.user)
    return render(request, 'game/statistic.html', {'stat': statistic,'pic': picture, 'user_score': score_for_user})

def how_to_play_page(request):
    user = request.user
    client_ip = get_client_ip(request)
    if str(request.user) == 'AnonymousUser':
        logger.error('Try to access from {}'.format(client_ip))
    logger.info('Access from {}'.format(user))
    return render(request, 'game/howto.html')
    

@login_required
def topic_page(request):
    """Redirect to Select Topic page."""
    user = request.user
    client_ip = get_client_ip(request)
    if str(request.user) == 'AnonymousUser':
        logger.error('Try to access from {}'.format(client_ip))
    logger.info('Access from {}'.format(user))
    topic = Topic.objects.all()
    return render(request, 'game/topic.html', {'topic':topic})


def question_difficulty(value: Question, topic_id: int, difficulty: str):
    """Return list of Question with filtered topic_id and difficulty."""
    return [q for q in value.objects.filter(topic_id=topic_id, difficulty=difficulty)]

def sample_question(value: Question, topic_id: int, diff: str, no_of_question: int):
    """
        Return a list of shuffled 'no_of_question' Question(s)
        with filtered topic_id and difficulty.
    """
    each_question_diff = question_difficulty(value, topic_id, diff)
    try:
        shuffle = sample(each_question_diff, no_of_question)
    except ValueError:
        shuffle = sample(each_question_diff, len(each_question_diff))
    return shuffle


def random_question_list(value, topic_id: int):
    """
        Return a list of all 10 (or less) shuffled Question(s)
        with filtered topic_id.
    """
    question_list = []
    for diff in ['easy', 'normal', 'hard']:
        shuffle = sample_question(value, topic_id, diff, 3)
        question_list += shuffle
    question_list += sample_question(value, topic_id, 'extreme', 1)
    return question_list

def create_answer_box(value: str):
    """Replace '[[__|__]]' with input tag.
    Return the formatted value."""
    while ']]' in value:
        start = value.find('[[')
        mid = value.find('|')
        end = value.find(']]')
        ans_length = mid - start - 2
        box_length = ans_length
        if box_length < 1:
            box_length = 1
        hint = value[mid+1:end]
        replacement = str(AnswerForm(ans_length=ans_length,
                                     box_length=str(box_length)+"ch", hint=hint))
        value = value[:start] + replacement + value[end+2:]
    return value

def question_page_resources(topic_id):
    questions = random_question_list(Question, topic_id)
    q_title = [q.question_title for q in questions]
    q_text = []
    for q in questions:
        boxed_question = create_answer_box(q.question_text)
        q_text.append(boxed_question)
    q_diff = [q.difficulty for q in questions]
    ans, hint = [], []
    for question in questions:
        answer_set = list(Answer.objects.filter(
            question_id=question.id, topic_id=topic_id))
        ans.append([a.answer_text for a in answer_set])
        hint.append([a.hint_text for a in answer_set])
    resources = {"title": q_title, "text": q_text,
                 "diff": q_diff, "answer": ans, "hint": hint}
    return resources

@login_required
def question_page(request, topic_id):
    """Redirect to the Game page."""
    user = request.user
    client_ip = get_client_ip(request)
    if str(request.user) == 'AnonymousUser':
        logger.error('Access from {}'.format(client_ip))
    logger.info('Access from {}'.format(user))
    resources = question_page_resources(topic_id)
    get_best_score(request, topic_id)
    return render(request, 'game/game.html', {
        'q_title': resources["title"], 'q_text': resources["text"],
        'answer': resources["answer"], 'hint': resources["hint"],
        'q_diff': resources["diff"], 'topic_id': topic_id})

def assign_answer(value, question_id, topic_id):
    """From 'value', Save string inside '[[__|__]]' as Answer."""
    last_box_mark = 0
    while ']]' in value:
        start = value.find('[[', last_box_mark)
        if start < last_box_mark:
            break
        mid = value.find('|', last_box_mark)
        end = value.find(']]', last_box_mark)
        answer = Answer(question_id=question_id, topic_id=topic_id,
                        answer_text=value[start+2:mid], hint_text=value[mid+1:end])
        answer.save()
        last_box_mark = end + 1

@login_required
def get_stat(request):
    """Create statistic for each player include score"""
    name = request.user
    logger.info("Check player {} info".format(name))
    user_id = request.user.id
    status = True
    check_id = Statistic.objects.filter(user_id=user_id)
    if check_id:
        status = False
        logger.error("{} stat is already exist".format(name))
    if User.is_authenticated and status:
        logger.info("Create stat for {}".format(name))
        user = User.objects.get(pk=user_id)
        stat = Statistic(user=user)
        stat.save()
    try:
        next_page = request.GET['next']
        return HttpResponseRedirect(next_page)
    except:
        return redirect('game:home')

@login_required
def preview_form(request):
    """Reidrect to Form Preview page."""
    name = request.user
    logger.info("Create question from {}".format(name))
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            topic = Topic.objects.get(pk=int(form.data.get('topic')))
            title = form.data.get('question_title')
            raw_question = form.data.get('question_text')
            difficulty = form.data.get('difficulty')
            question = Question(topic=topic,
                                question_title=title,
                                question_text=raw_question,
                                difficulty=difficulty)
            question.save()
            assign_answer(raw_question, question.id, topic.id)
            return render(request, "game/preview_form.html", {'question': question})

@login_required
def discard_form(request, question_id):
    """Discard the Question Form."""
    name = request.user
    logger.info("Delete a question from {}".format(name))
    check = Question.objects.filter(pk=question_id)
    if check:
        question = Question.objects.get(pk=question_id)
        question.delete()
        return redirect("game:form")
    return preview_form(request.POST)

@login_required
def receive_score(request, topic_id):
    """Save highscore to User profile when the game finished."""
    user_id = request.user.id
    topic = get_object_or_404(Topic, pk=topic_id)
    profile = Best_score.objects.get(user=user_id, key=topic.topic_name)
    check_key = Best_score.objects.filter(key=topic.topic_name, user=user_id)
    if check_key:
        try:
            score = request.GET.get('result_score')
            logger.info("Player receive {} score".format(score))
            if int(profile.value) < int(score):
                profile.value = int(score)
                profile.save()
        except:
            client_ip = get_client_ip(request)
            logger.error("Error from end point".format(client_ip))
    return redirect("game:home")


def get_best_score(request, topic_id):
    """Create best score obj"""
    name = request.user
    logger.info("Check best score of {}".format(name))
    user_id = request.user.id
    topic = get_object_or_404(Topic, pk=topic_id)
    get_user = User.objects.get(pk=user_id)
    check_key = Best_score.objects.filter(key=topic.topic_name, user=user_id)
    if not check_key:
        logger.info("Create best score for {}".format(name))
        s = Best_score(user=get_user, key=topic.topic_name, value=0)
        s.save()
    else:
        logger.error("Best score of {} is already exist".format(name))

def edit_form(request, question_id):
    name = request.user
    logger.info("{} want to edit form".format(name))
    if request.method == "GET":
        question = Question.objects.get(pk=question_id)
        topic = Topic.objects.get(pk=question.topic_id)
        form = QuestionForm(instance=question)
        logger.info("question {} is deleted".format(question.question_title))
        question.delete()
        return render(request, "game/form.html", {"question_id":question_id, "form":form})
