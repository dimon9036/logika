from PyQt5.QtWidgets import(QPushButton, QRadioButton, QLabel, QSpinBox, QGroupBox, QButtonGroup, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import Qt

btn_menu = QPushButton("Меню")
btn_rest = QPushButton("Відпочити")
spin = QSpinBox()
spin.setValue(30)

quest_lb = QLabel("Яблуко")
rbGroupBox = QGroupBox("Варіанти відповіді")
btn_ok = QPushButton("Відповісти")

rb1 = QRadioButton("Apple")
rb2 = QRadioButton("Dog")
rb3 = QRadioButton("Mac")
rb4 = QRadioButton("Sun")

main_box_line = QHBoxLayout()
box_line1 = QVBoxLayout()
box_line2 = QVBoxLayout()
box_line1.addWidget(rb1)
box_line2.addWidget(rb2)
box_line1.addWidget(rb3)
box_line2.addWidget(rb4)
main_box_line.addLayout(box_line1)
main_box_line.addLayout(box_line2)
rbGroupBox.setLayout(main_box_line)

ansGroupBox = QGroupBox("Результати теста")
main_box2_line = QVBoxLayout()
result_1b = QLabel("Правильно")
right_ans_lb = QLabel("Apple")
main_box2_line.addWidget(result_1b)
main_box2_line.addWidget(right_ans_lb)
ansGroupBox.setLayout(main_box2_line)
ansGroupBox.hide()

main_line_quiz = QVBoxLayout()
line1_quiz = QHBoxLayout()

line1_quiz.addWidget(btn_menu)
line1_quiz.addWidget(btn_rest)
line1_quiz.addWidget(spin)
line1_quiz.addWidget(QLabel("Хвилин"))

main_line_quiz.addLayout(line1_quiz, stretch=1)
main_line_quiz.addWidget(quest_lb, alignment=Qt.AlignCenter, stretch=1)
main_line_quiz.addWidget(rbGroupBox, stretch=5)
main_line_quiz.addWidget(btn_ok, stretch=1)
main_line_quiz.addLayout(line1_quiz)


