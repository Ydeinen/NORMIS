from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QButtonGroup, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
from random import shuffle, randint
from PyQt5.QtGui import *

class question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    
def show_result():   
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():   
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения


def ask(q: question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.score += 1
        print('Рейтинг:',(window.score/window.total*100), '%')
    else:
        show_correct('Неверно!!!!')
        print('Рейтинг:',(window.score/window.total*100), '%')


def test():
    if btn_OK.text() == 'Ответить':
        show_result()
    else:
        show_question()


def next_question():
    window.total += 1
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)


def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()


question_list = []
question_list.append(question('ТЕБЕ НРАВИТСЯМОЯ ПРОГРАМА', 'ДА', 'НЕТ', 'нЕт', 'НеТ'))
question_list.append(question('Год распада СССР', '1991', '1992', '1993', '1949'))
question_list.append(question('Что идёт после бесконечности', '1', '2 бесконечности', '3 * бесконечности', 'бесконечности * бесконечности'))
question_list.append(question('Что лучше?', '༼ つ ◕_◕ ༽つ', '🐱‍👤', '🪑', '☄☄☄'))
question_list.append(question('10¹⁰', '10000000000', 'хз', 'бесконечность', 'ПОМОГИТЕ'))
question_list.append(question('6/2 сколько целых', '3', '1 6/567', '6', '2'))
question_list.append(question('2+2', '4', '1', '3', 'хз'))


app = QApplication([])
window = QWidget()

window.setWindowTitle('Memo Card')
window.resize(400,200)
window.score = 0
window.total = 0
lb_Question = QLabel('В каком году появильсь мемы?') # текст вопроса
lb_Question.setStyleSheet('background-color: mediumSpringGreen')
lb_Question.setFont(QFont("Times", 20, QFont.Bold))

btn_OK = QPushButton('Ответить') # кнопка ответа
btn_OK.setStyleSheet('background-color: mediumSpringGreen')
btn_OK.setFont(QFont("Times", 20, QFont.Bold))
RadioGroupBox = QGroupBox("Варианты ответов") 

rbtn_1 = QRadioButton('1976')
rbtn_1.setStyleSheet('Font: 14pt DarkTurquoise')
rbtn_2 = QRadioButton('2077')
rbtn_2.setStyleSheet('Font: 14pt DarkTurquoise')
rbtn_3 = QRadioButton('10000000 до н.э.')
rbtn_3.setStyleSheet('Font: 14pt DarkTurquoise')
rbtn_4 = QRadioButton('0')
rbtn_4.setStyleSheet('Font: 14pt DarkTurquoise')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке

RadioGroupBox.setLayout(layout_ans1)

# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=3) # кнопка должна быть большой
layout_line3.addStretch(1)

# Теперь созданные строки разместим друг под другом:
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=7)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

window.setLayout(layout_card)
btn_OK.clicked.connect(click_OK)
next_question()
window.show()
app.exec_()
