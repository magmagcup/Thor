from selenium import webdriver
from django.test import LiveServerTestCase, Client
from django.contrib.auth.models import User
from game.models import Topic, Question, Answer
from game.forms import AnswerForm

def create_topic(topic_name):
    topic = Topic.objects.create(topic_name=topic_name)
    return topic

def create_answer_box(value):
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

def assign_answer(value, question_id, topic_id):
    start = value.find('[[')
    mid = value.find('|')
    end = value.find(']]')
    Answer.objects.create(question_id=question_id, topic_id=topic_id,
                    answer_text=value[start+2:mid], hint_text=value[mid+1:end])

def fill_question(topic):
    for i in range(1, 4):
        for j in ['easy', 'normal', 'hard']:
            raw_text = f"[[{i}|hint {i}]]"
            q = Question.objects.create(
                question_title=str(i),
                question_text=create_answer_box(raw_text),
                difficulty=j,
                topic_id=topic)
            assign_answer(raw_text, q.id, topic)
    raw_ex_text = "[[last|hint last]]"
    ex_ques = Question.objects.create(
        question_title="last",
        question_text=create_answer_box(raw_ex_text),
        difficulty='extreme', topic_id=topic)
    assign_answer(raw_ex_text, ex_ques.id, topic)
    

class MainGameTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(
            executable_path="D:/Download/chromedriver_win32/chromedriver.exe")
        self.username = "admin007"
        self.password = "notimetodie"
        self.client = Client()
        self.user = User.objects.create_user(
            self.username, password=self.password)
        super(MainGameTest, self).setUp()
    
    def tearDown(self):
        self.browser.quit()
        super(MainGameTest, self).tearDown()
    
    def test_topic_found(self):
        self.topic = create_topic("test_topic")
        self.client.force_login(self.user)
        fill_question(self.topic.id)
        self.browser.get(self.live_server_url + '/game/topic')
        topic = self.browser.find_element_by_id(f"t-{self.topic.id}")
        self.assertEqual(topic.text, 'test_topic')
