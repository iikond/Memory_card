from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint

q = Question('Как дела?', "Мне лень писать, поэтому...", "Крестики нолики", " две Миланы в домике", "Укатились даже шарики за ролики")
q = Question('В чём ходил лермонтов во время 3 мировой?', "Улы-улыбаемся","разгоняя тучки","Люди обзываются, что мы две почемучки")
q = Question('Почему почему называется почему?','Отпути, не путю, но кому я говорю','Не путю ведь я люблю свою лучшую подругу',"Отпути, не путю, но кому я говорю")

class Question:
    def __init__(self, Questions, rigth_answer, wrong1, wrong2, wrong3):
            self.qu = Questions
            self.right_ans = rigth_answer
            self.wr1 = wrong1
            self.wr2 = wrong2
            self.wr3 = wrong3

obj = Question(
    Questions = 'Ёedbc т`N~оGU `Fgа?',
    right_answer = 'Абракадабра',
    wrong1 = 'МАИНКРААААААААААААФТ',
    wrong2 = 'Что я пишу?',
    wrong3 = "С ДНЁМ РОЖДЕНИЯ!"
    )

def next_question():
    cur_question = randint(0, len(Questions) - 1)
    q = Questions[cur_question]
    ask(q)
def click_ok():
    show_result()
    show.right_ans

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroupBox.setExlusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroupBox.setExlusive

def start_test():
    btn_ok.text
    if btn_ok == "Следующий вопрос":
        show_question()
    elif btn_ok == 'Ответить':
        show_result()

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(obj:Question):
    shuffle(answers)#Перемешиваем кнопки
    answers[0].setText(obj.right_ans)
    answers[1].setText(obj.wr1)
    answers[2].setText(obj.wr2)
    answers[3].setText(obj.wr3)
    Questions.setText(next_question)
    right_answer.setText(rigth_answer)



ask(obj.Question)



app = QApplication([])
window = QWidget()
window.setWindowTitle("Memory Card")

btn_ok = QPushButton('Ответить')
question_label = QLabel('')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Алеуты')

AnsGroupBox = QGroupBox("Результаты теста")
#1b_result = QLabel('Прав ты или нет?')

kakoi_to_layout= QVBoxLayout()
#kakoi_to_layout.addWidget(1b_result, alignment=(Qt.AlignLeft | Qt.AlignTop))

setLayout(AnsGroupBox)


layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

layout2.addWidget(rbtn1)
layout2.addWidget(rbtn2)
layout3.addWidget(rbtn3)
layout3.addWidget(rbtn4)


layout1.addLayout(layout2)

RadioGroupBox.setLayout(layout1)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question_label, alignment = (Qt.AlignHCenter| Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=2)
layout_card.setSpacing(5)


window.setLayout(layout_card)
window.show()
app.exec()