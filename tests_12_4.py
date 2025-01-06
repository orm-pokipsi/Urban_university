import logging
import rt_with_exceptions as rt
import unittest

print('Задача "Логирование бегунов":')

class RunnerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log",
                            encoding="utf-8", format="%(asctime)s | %(levelname)s | %(message)s")

    def test_walk(self):
        try:
            runner_1 = rt.Runner('Name', -10)
            for _ in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            runner_2 = rt.Runner(5)
            for _ in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    if __name__ == "__main__":
        unittest.main()