import unittest                                                          # Импортируем библиотеку unittest
import tests_12_3                                                        # Импортируем файл

test_12_3 = unittest.TestSuite()   #  TestSuite это наборы тестов, в которые можно добавлять дополнительные тесты.
                               # Так же можно создавать разные TestSuite()-ы и запускать их по отдельности
test_12_3.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))   # Дополняем тесты класса
                                                                                       # RunnerTest из модуля tests_12_3
test_12_3.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))  # Дополняем тесты класса
                                                                                # TournamentTest из модуля tests_12_3
runner = unittest.TextTestRunner(verbosity=2)     #  Из unittest берем функцию TextTestRunner() и сохраняем в
                                               # переменной runner, verbosity=2 выводит параметры наших тестов в консоль
runner.run(test_12_3)    #  Запускаем runner по тестсистеме test_12_3
