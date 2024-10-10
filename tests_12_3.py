import unittest                                  # Импортируем библиотеку unittest
from runner import Runner                        # Импортируем из модуля runner класс Runner
from runner_and_tournament import Runner, Tournament    # Импортируем из модуля runner_and_tournament
                                                          # классы Runner и Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False                            # Добавляем значение is_frozen для пропуска тестов
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")   # Декоратор - если is_frozen = False, то
                                                                            # тест выполняется
    def test_walk(self):                         # Создаем метод test_walk
        run1 = Runner("Test_1")                  # Создаем объект run1 класса Runner (из модуля runner)
        i = 1                                    # Объявляем переменную для цикла while
        while i <= 10:                           # Цикл вызывает функцию walk из класса Runner (из модуля runner) 10 раз
            run1.walk()
            i += 1                               # С каждым проходом увеличиваем переменную i на единицу
        self.assertEqual(run1.distance, 50)  # Методом assertEqual сравниваем distance объекта run1
                                                       # со значением 50

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")  # Декоратор - если is_frozen = False, то
                                                                           # тест выполняется
    def test_run(self):                          # Создаем метод test_run
        run2 = Runner("Test_2")                  # Создаем объект run2 класса Runner (из модуля runner)
        j = 1                                    # Объявляем переменную j для цикла while
        while j <= 10:                           # Цикл вызывает функцию run из класса Runner (из модуля runner) 10 раз
            run2.run()
            j += 1                               # С каждым проходом увеличиваем переменную j на единицу
        self.assertEqual(run2.distance, 100)   # Методом assertEqual сравниваем distance объекта run2
                                                         # со значением 100

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")  # Декоратор - если is_frozen = False, то
                                                                           # тест выполняется
    def test_challenge(self):                    # Создаем метод test_challenge
        run3 = Runner("Test_3")                  # Создаем объектs run3 класса Runner (из модуля runner)
        run4 = Runner("Test_3")                  # Создаем объектs run4 класса Runner (из модуля runner)
        l = 1                                    # Объявляем переменную l для цикла while
        while l <= 10:                           # Цикл вызывает функцию run из класса Runner (из модуля runner) 10 раз
            run3.run()
            run4.walk()
            l += 1                               # С каждым проходом увеличиваем переменную l на единицу
        self.assertNotEqual(run3.distance, run4.distance)  # Методом assertNotEqual сравниваем distance объектов run3 и
                                                           # run4, и убеждаемся в их неравенстве


class TournamentTest(unittest.TestCase):     # Определяем класс TournamentTest, наследованный от unittest.TestCase
    is_frozen = True                         # Добавляем значение is_frozen для пропуска тестов

    @classmethod
    def setUpClass(cls):        # Метод, который будет запускаться перед запуском тестов, где создается и очищается
                                  # пустой словарь
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)     # Создаем объект Usein класса Runner
                                                            # (из модуля runner_and_tournament)
        self.andrei = Runner("Андрей", 9)    # Создаем объект Andrei класса Runner
                                                            # (из модуля runner_and_tournament)
        self.nik = Runner("Ник", 3)          # Создаем объект Nik класса Runner
                                                            # (из модуля runner_and_tournament)
    @classmethod
    def tearDownClass(cls):                              # Метод tearDownClass, который будет выполняться один раз
                                                            # после завершения всех тестов
        for results in cls.all_results.values():         # Цикл по всем значениям словаря cls.all_results, где
                                                            # каждое значение представляет собой словарь с
                                                            # местом (результат) и именем бегуна
            formated_results = {place:str(runner) for place, runner in results.items()}   # Форматируем результаты в
                                                                                            # читаемый вид
            print(formated_results)                       # Выводим в консоль

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")  # Декоратор - если is_frozen = True, то
                                                                           # тест НЕ выполняется
    def test_usain_nik(self):      # Определяем первый тест, чтобы протестировать забег между Усэйном и Ником
        tournament = Tournament(90, self.usain, self.nik)   # Создаем объект класса Tournament с
                                                                                  # дистанцией девяносто и участниками
                                                                                  # self.usain и self.nik
        results = tournament.start()                   # Запускаем метод start и
        TournamentTest.all_results[1] = results        # сохраняем его в словарь
        self.assertEqual("Ник", results[2].name)  # Проверяем, что имя последнего бегуна равно Ник

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")  # Декоратор - если is_frozen = True, то
                                                                           # тест НЕ выполняется
    def test_andrei_nik(self):      # Определяем первый тест, чтобы протестировать забег между Андреем и Ником
        tournament = Tournament(90, self.andrei, self.nik)   # Создаем объект класса Tournament с
                                                                                   # дистанцией девяносто и участниками
                                                                                   # self.andrei и self.nik
        results = tournament.start()                   # Запускаем метод start и
        TournamentTest.all_results[2] = results        # сохраняем его в словарь
        self.assertEqual("Ник", results[2].name)  # Проверяем, что имя последнего бегуна равно Ник

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")  # Декоратор - если is_frozen = True, то
                                                                           # тест НЕ выполняется
    def test_usain_andrei_nik(self):  # Определяем первый тест, чтобы протестировать забег между Усэйном, Андреем и Ником
        tournament = Tournament(90, self.usain, self.andrei, self.nik)  # Создаем объект класса
                                                                                   # Tournament с
                                                                                   # дистанцией девяносто и участниками
                                                                                   # self.usain, self.andrei и self.nik
        results = tournament.start()                   # Запускаем метод start и
        TournamentTest.all_results[3] = results        # сохраняем его в словарь
        self.assertEqual("Ник", results[3].name)  # Проверяем, что имя последнего бегуна равно Ник

if __name__ == "__main__":                       # Для запуска используем юнит-тест "main"
    unittest.main()

