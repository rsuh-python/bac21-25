import sys
from PyQt5.QtWidgets import QMainWindow, QDialog, QGridLayout, QLineEdit, QAction, QApplication, \
    QLabel, QHBoxLayout, QVBoxLayout, QDockWidget, QMessageBox, QPushButton, QGroupBox, QRadioButton, QButtonGroup, \
    QCheckBox, QSpinBox, QProgressBar, QWidget, QComboBox
from PyQt5.QtGui import QPixmap, QFont, QIcon, QCursor
from PyQt5.QtCore import Qt

class Window1(QMainWindow): # Создаем класс от родителя QMainWindow - это будет наше первое окно.
    def __init__(self):
        super().__init__() # Наследуем методы и атрибуты класса QMainWindow.
        self.initUI()

    def initUI(self): # Основная функция для построения нашего окна.
        self.setWindowTitle("PyQt5 для студентов РГГУ :)") # Называем наше окошко. Оно будет высвечиваться в верхней полосе.
        self.resize(800, 300) # Назначаем размер окна. Оно будет растягиваться само, если добавлять туда большие элементы.
        self.setWindowIcon(QIcon('icon.png')) # Назначаем логотип для окна.
        self.w = None # В эту переменную мы поместим наше следующее окно.

        pic = QLabel() # Создаем надпись, которую потом заполним изображением.
        pic.setPixmap(QPixmap("design//rggu_logo.png").scaled(300, 301)) # Устанавливаем наше изображение в надпись и подгоняем размер.
        pic.setAlignment(Qt.AlignCenter) # Назначаем выравнивание по центру.
        self.setCentralWidget(pic) # Назначаем картинку главным виджетом нашего окна QMainWindow.


        labelwidget = QDockWidget(self) # Создаем экземляр док-виджета. Это перемещаемый объект, уникальный для MainWindow.
        labelwidget.setWindowTitle("Приветствие") # Даем название нашему док-виджету.
        label = QLabel("Приветствую студентов РГГУ!\n"
                       "Это приложение - пример использования PyQt5 для создания\n"
                       "Ваших собственных программ на Python!") # Создаем нашу надпись.
        label.setAlignment(Qt.AlignCenter) # Выравниваем по центру.
        label.setFont(QFont('Arial', 12)) # Назначаем шрифт и его размер.
        labelwidget.setWidget(label) # Устанавливаем наш готовый виджет в экземпляр док-виджета.
        self.addDockWidget(Qt.BottomDockWidgetArea, labelwidget) # Добавляем в окно наш док-виджет и выбираем нижнюю область для него.

        exitAction = QAction(QIcon('design//exit.png'), 'Выход', self) # Создаем действие "выход". Выбираем для него иконку и название.
        exitAction.setShortcut('Ctrl+Q') # Выбираем горячие клавиши для выхода.
        exitAction.setStatusTip('Выход из приложения') # Создаем подсказку к нашему действию.
        exitAction.triggered.connect(self.close) # Привязываем функцию к действию. В данном случае это уже существуюший метод .close.

        continueAction = QAction(QIcon('design//continue.png'), 'Продолжить', self) # Делаем аналогичную работу с действием "продолжить".
        continueAction.setShortcut('Ctrl+W')
        continueAction.setStatusTip('Открыть следующее окно')
        continueAction.triggered.connect(self.next_window)

        self.statusBar() # Добавляем в окно строку состояния.
        menubar = self.menuBar() # Добавляем в окно верхнее меню.

        optionMenu = menubar.addMenu('&Опции') # Содаем категорию "опции" в меню.
        optionMenu.addAction(continueAction) # Добавляем туда наши действия.
        optionMenu.addAction(exitAction)

        toolbar = self.addToolBar('Выход') # Добавляем в поле с инструментами кнопку "Выход"...
        toolbar.addAction(exitAction) # ...И действие к нему.
        toolbar2 = self.addToolBar('Продолжить') # То же самое делаем с "Продолжить".
        toolbar2.addAction(continueAction)

    def next_window(self):
        self.w = Window2() # Создаем следующее окно,
        self.w.show() # показываем его,
        self.hide() # и скрываем это окно.

    def closeEvent(self, event): # Создаем кастомное событие выхода. Пользователю будет задан вопрос.
        reply = QMessageBox.question(self, 'Выход',
                                     "Вы уверены, что хотите выйти?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 для студентов РГГУ")
        self.resize(800, 300)
        self.setWindowIcon(QIcon('icon.png'))
        self.setFont(QFont('Arial', 14)) # Назначаем дефолтный шрифт для данного окна.
        self.w = None

        self.initUI() # Вызываем метод класса, который создаст структуру окна - он написан далее.

    def initUI(self):
        label_name = QLabel("Имя:")
        self.line_name = QLineEdit() # Создаем поле для ввода.

        label_surname = QLabel("Фамилия:")
        self.line_surname = QLineEdit()
        self.line_surname.setEchoMode(QLineEdit.Password) # Теперь при вводе текст будет закрыт звездочками.

        label_gender = QLabel("Пол:")
        gendergroup = QButtonGroup() # Используется для того, чтобы из всех кнопок можно было выбрать только одну.
        self.button_gender1 = QRadioButton("Муж.") # Радио-кнопка - кружок с точкой.
        self.button_gender2 = QRadioButton("Жен.")
        gendergroup.addButton(self.button_gender1) # Добавляем в группу наши кнопки.
        gendergroup.addButton(self.button_gender2)

        label_pet = QLabel("Питомец:")
        self.check_pet = QCheckBox() # Чек-бокс - квадрат с галочкой.

        label_petkind = QLabel("Вид питомца:")

        self.combo_petkind = QComboBox() # Комбо-бокс - коробка с выбором из множества вариантов в разворачивающемся списке.
        self.combo_petkind.addItems(["Собака",
                           "Кошка",
                           "Хомяк",
                           "Морская свинка",
                           "Попугай",
                           "Кролик",
                           "Крыса",
                           "Шиншилла",
                           "Канарейка",
                           "Рыбка",
                           "Змея",
                           "Ёжик",
                           "Ящерица",
                           "Паук",
                           "Улитка",
                           "Черепаха",
                           "Тараканы",
                           "Муравьи",
                           "Черви",
                           "Другой питомец"]) # Вводим список элементов в нашу коробочку.
        self.combo_petkind.setDisabled(True) # Запрещаем эту коробочку (зачем - дальше будет понятно)

        label_age = QLabel("Ваш возраст:")
        self.spin_age = QSpinBox() # Спин-бокс - коробка для введения чисел со стрелочками "вверх" и "вниз".
        self.spin_age.setValue(21) # Выбираем дефолтное значение.
        self.spin_age.setMinimum(10) # Назначаем минимум и максимум.
        self.spin_age.setMaximum(60)

        self.progress_bar = QProgressBar() # Строка прогресса. Мы будем обновлять ее в коде.
        self.progress_bar.setRange(0, 10) # Устанавливаем диапазон значений.
        self.progress_bar.setAlignment(Qt.AlignCenter) # Выравнивание текста по центру. Мы будем показывать текст в прогресс-баре!

        backbutton = QPushButton("Назад") # Обычная кнопка, при нажатии на которую НЕМЕДЛЕННО происходит событие.
        backbutton.setAutoDefault(False) # Отдаем предпочтение кнопке "продолжить".
        continuebutton = QPushButton("Продолжить")
        continuebutton.setAutoDefault(True) # Кнопка "продолжить" теперь будет выделена изначально и нажиматься пробелом.


        # Тут начинается самое скучное - сборка всех виджетов в раскладки, чтобы они потом появились в окне.
        mainLayout = QGridLayout() # Данная раскладка - вспомогательная.
        groupBox = QGroupBox("Расскажите немного о себе :)") # Это просто красивая коробочка, в которую мы соберем все виджеты.

        namebox = QHBoxLayout() # "H" значит "horizontal". Эта раскладка собирает виджеты горизонтально.
        namebox.addWidget(label_name) # Таким образом мы муторно собираем виджеты по раскладкам.
        namebox.addWidget(self.line_name) # Здесь, например, мы комбинируем подписи и поля для ввода.

        surnamebox = QHBoxLayout()
        surnamebox.addWidget(label_surname)
        surnamebox.addWidget(self.line_surname)

        petbox = QHBoxLayout()
        petbox.addWidget(label_pet)
        petbox.addWidget(self.check_pet)
        petbox.addStretch() # Данный метод вызывает пробел. В данном случае он "отбивает" нашу галочку в левую сторону.


        petkindbox = QHBoxLayout()
        petkindbox.addWidget(label_petkind)
        petkindbox.addWidget(self.combo_petkind)

        genderbox = QHBoxLayout()
        genderbox.addWidget(self.button_gender1)
        genderbox.addWidget(self.button_gender2)

        agebox = QHBoxLayout()
        agebox.addWidget(label_age)
        agebox.addWidget(self.spin_age)

        masterbox = QGridLayout() # Пред-предпоследняя раскладка. Это сетка - кладя в нее готовые макеты или виджеты,
        # мы указываем их расположение по x и y соответственно.

        masterbox.addLayout(namebox, 0, 0)
        masterbox.addLayout(surnamebox, 1, 0)
        masterbox.addLayout(petbox, 2, 0)
        masterbox.addLayout(petkindbox, 3, 0)
        masterbox.addWidget(label_gender, 0, 1)
        masterbox.addLayout(genderbox, 1, 1)
        masterbox.addLayout(agebox, 2, 1)
        masterbox.addWidget(self.progress_bar, 3, 1)
        masterbox.addWidget(backbutton, 4, 0)
        masterbox.addWidget(continuebutton, 4, 1)

        groupBox.setLayout(masterbox) # Кладем сетку в коробочку с подписью. Коробочка стала виджетом, а не раскладкой!
        mainLayout.addWidget(groupBox, 0, 0) # Кладем коробочку с подписью в финальную раскладку.
        self.setLayout(mainLayout) # Назначаем финальную раскладку главной и устанавливаем ее в наше окно.

        # Здесь мы привязываем кнопки к функциям, которые они будут вызывать.
        self.check_pet.toggled.connect(self.combo_petkind.setEnabled) # Здесь, например, мы разрешаем выбор типа питомца
        # только тогда, когда поставлена галочка "Питомец".
        backbutton.pressed.connect(self.first_window)
        continuebutton.pressed.connect(self.check)


    def check(self): # Функция для проверки ввода данных. Что будет если мы не введем данные?
        self.progress_bar.setValue(2) # Обновляем наш прогресс-бар. Будем вручную увеличивать его на 2.
        self.progress_bar.setFormat("Начинаем") # Устанавливаем текст в наш прогресс-бар.
        if self.line_name.text() == "":
            self.progress_bar.setValue(0) # Обнуляем прогресс-бар в случае ошибки
            self.progress_bar.setFormat("") # И текст уничтожаем
            return QMessageBox.warning(self, "Ошибка", "Введите свое имя!") # Вызываем предупреждение, которое не даст пройти дальше!

        if self.line_surname.text() == "":
            self.progress_bar.setValue(0)
            self.progress_bar.setFormat("")
            return QMessageBox.warning(self, "Ошибка", "Введите свою фамилию!")

        if not self.button_gender1.isChecked() and not self.button_gender2.isChecked():
            self.progress_bar.setValue(0)
            self.progress_bar.setFormat("")
            return QMessageBox.warning(self, "Ошибка", "Выберите свой пол!")

        dialog = Dialog() # Создаем экземпляр диалогового окна, которое попросит нас подтвердить информацию.
        result = dialog.exec_() # Вызываем диалоговое окно, результат работы которого вернет нам 1 в случае подтверждения,
        # и 0 в случае отмены.
        if result == 1: # Если юзер подтвердил правильность информации, то...
            self.last_window()  # "Паровозиком" вызываем следующую функцию.
        else: # Если нет - обнуляем прогресс-бар и остаемся в этом окне.
            self.progress_bar.setValue(0)
            self.progress_bar.setFormat("")


    def last_window(self): # Переход к следующему окну. Будет сопровождаться получением всех данных.
        self.progress_bar.setValue(4)
        name, surname = self.line_name.text(), self.line_surname.text() # метод .text возвращает текст из полей для ввода.
        if self.button_gender1.isChecked(): # Проверяем, какая из радио-кнопок выбрана.
            gender = "парень"
        else:
            gender = "девушка"

        self.progress_bar.setValue(6)
        if self.check_pet.isChecked(): # Если кнопка "питомец" подчеркнута, то мы получаем вид питомца из комбо-бокса.
            petkind = self.combo_petkind.currentText()
        else:
            petkind = False

        self.progress_bar.setValue(8)
        age = self.spin_age.value() # Получаем число из спин-бокса.

        self.progress_bar.setValue(10)
        self.progress_bar.setFormat("Готово")

        self.w2 = Window3(name, surname, gender, age, petkind) # Передаем все собранные аргументы следующему окну.
        self.w2.show() # Показываем окно, но не закрываем это.

        self.progress_bar.setValue(0)
        self.progress_bar.setFormat("")


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Выход',
                                     "Вы уверены, что хотите выйти?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def first_window(self): # Возвращение к первому окну - по аналогии с переходом во второе.
        self.w = Window1()
        self.w.show()
        self.hide()

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 для студентов РГГУ :)")
        self.resize(500, 300)
        self.setWindowIcon(QIcon('icon.png'))
        self.setFont(QFont('Arial', 15))
        self.setWhatsThis("Подтвердите правильность данных!") # Специфическая для QDialog фича - она показывает сообщение при нажатии на "?".
        self.initUI()

    def initUI(self):

        label = QLabel("Все поля заполнены верно?")
        label.setAlignment(Qt.AlignCenter)
        pic = QLabel()
        pic.setPixmap(QPixmap("design//emoji.png").scaled(200, 200))
        pic.setAlignment(Qt.AlignCenter)
        button1 = QPushButton("Да")
        button2 = QPushButton("Нет")

        button1.clicked.connect(self.accept) # Метод "подтвердить" уже присутствует у этого класса. Он возвращает число 1.
        button2.clicked.connect(self.reject) # Такой же метод "отклонить" возвращает 0.

        buttonlayout = QHBoxLayout()
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(pic)
        buttonlayout.addWidget(button1)
        buttonlayout.addWidget(button2)
        layout.addLayout(buttonlayout)
        self.setLayout(layout)

class Window3(QWidget):
    def __init__(self, name, surname, gender, age, petkind):
        super().__init__()
        self.setWindowTitle("PyQt5 для студентов РГГУ :)")
        self.resize(800, 300)
        self.setWindowIcon(QIcon('icon.png'))
        self.setFont(QFont('Arial', 14))

        self.name, self.surname = name, surname # Все аргументы кладем в атрибуты класса, чтобы их было легче достать.
        self.gender, self.age = gender, age
        self.petkind = petkind

        self.initUI()

    def initUI(self):
        pic = QLabel()
        pic.setPixmap(QPixmap("design//akinator.png"))
        pic.setAlignment(Qt.AlignRight)

        label1 = QLabel("Легко!")
        label1.setFont(QFont('Arial', 40))
        label2 = QLabel(f"Вас зовут {self.name.capitalize()} {self.surname.capitalize()}, Вы {self.gender},\n"
                        f"Ваш возраст {self.age}.") # Строим текст исходя из полученных данных.
        label3 = QLabel("")

        if self.petkind == "Другой питомец":
            label3.setText(f"У Вас есть питомец. Пока не знаю, какой.")

        elif self.petkind:
            label3.setText(f"У Вас есть питомец. Это {self.petkind.lower()}!")

        else:
            label3.setText("А еще у Вас нет питомца!")

        label4 = QLabel("© Akinator")
        backbutton = QPushButton("Закрыть")
        backbutton.setCursor(QCursor(Qt.PointingHandCursor)) # Теперь при наведении на кнопку "Закрыть" вместо стрелочки
        # курсор превратится в палец!

        mainlayout = QVBoxLayout() # Эта раскладка будет намного проще, и теперь главная раскладка здесь - вертикальная ("V").
        masterbox = QHBoxLayout()
        messagesbox = QVBoxLayout()
        messagesbox.addWidget(label1)
        messagesbox.addWidget(label2)
        messagesbox.addWidget(label3)
        messagesbox.addWidget(label4)

        masterbox.addLayout(messagesbox)
        masterbox.addWidget(pic)
        mainlayout.addLayout(masterbox)
        mainlayout.addWidget(backbutton)

        backbutton.pressed.connect(self.close) # Привязываем кнопку "Закрыть" к методу закрытия данного окошка.
        self.setLayout(mainlayout)

def open_window(): # Наша функция для открытия приложения.
    app = QApplication(sys.argv) # Создаем наше приложение с аргументами из командной строки.
    wind = Window1() # Создаем экземпляр первого окна.
    wind.show() # Показываем наше окно.
    sys.exit(app.exec_()) # Заканчиваем работу приложения в случае выхода.

open_window()