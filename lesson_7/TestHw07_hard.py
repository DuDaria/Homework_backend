import unittest

from hw07_hard import Worker, HourseOf

class TestWorker(unittest.TestCase):
    f_name = 'Иван'
    l_name = 'Иванов'
    salary = 30000
    position = 'рабочий'
    hour_rate = 30

    woker = Worker(f_name, l_name, salary, position, hour_rate)

    def test_init(self):
        self.assertIsInstance(self.woker.f_name, str)
        self.assertTrue(self.woker.f_name, True)
        self.assertIsNotNone(self.woker.f_name)
        self.assertIsInstance(self.woker.l_name, str)
        self.assertTrue(self.woker.l_name, True)
        self.assertIsNotNone(self.woker.l_name)
        self.assertIsInstance(self.woker.salary, int)
        self.assertTrue(self.woker.salary, True)
        self.assertIsNotNone(self.woker.salary)
        self.assertIsInstance(self.woker.position, str)
        self.assertTrue(self.woker.position, True)
        self.assertIsNotNone(self.woker.position)
        self.assertIsInstance(self.woker.hour_rate, int)
        self.assertTrue(self.woker.hour_rate, True)
        self.assertIsNotNone(self.woker.hour_rate)
    
    def test_get_full_name(self):
        self.assertEqual(self.woker.get_full_name(), 'Иванов Иван')
        self.assertNotEqual(self.woker.get_full_name(), ' ')
        self.assertNotEqual(self.woker.get_full_name(), '')
        self.assertRaises(TypeError, self.woker.get_full_name, None)
        self.assertRaises(TypeError, self.woker.get_full_name, 0)
        self.assertIsNotNone(self.woker.get_full_name())
        self.assertIsInstance(self.woker.get_full_name(), str)

    def test_get_sallary(self):
        self.assertEqual(self.woker.get_sallary(), 30000)
        self.assertRaises(TypeError, self.woker.get_sallary, None)
        self.assertRaises(TypeError, self.woker.get_sallary, 0)
        self.assertIsInstance(self.woker.get_sallary(), int)
        self.assertIsNotNone(self.woker.get_sallary())

    def test_get_position(self):
        self.assertEqual(self.woker.get_position(), 'рабочий')
        self.assertNotEqual(self.woker.get_full_name(), ' ')
        self.assertNotEqual(self.woker.get_full_name(), '')
        self.assertRaises(TypeError, self.woker.get_position, None)
        self.assertRaises(TypeError, self.woker.get_position, 0)
        self.assertIsInstance(self.woker.get_position(), str)
        self.assertIsNotNone(self.woker.get_position())
    
    def test_get_hour_rate(self):
        self.assertEqual(self.woker.get_hour_rate(), 30)
        self.assertRaises(TypeError, self.woker.get_hour_rate, None)
        self.assertRaises(TypeError, self.woker.get_hour_rate, 0)
        self.assertIsInstance(self.woker.get_hour_rate(), int)
        self.assertIsNotNone(self.woker.get_hour_rate())


class TestHourseOf(unittest.TestCase):
    f_name = 'Иван'
    l_name = 'Иванов'
    work_hours = 18

    hourseof = HourseOf(f_name, l_name, work_hours)

    def test_init(self):
        self.assertEqual(self.hourseof.f_name, 'Иван')
        self.assertIsInstance(self.hourseof.f_name, str)
        self.assertTrue(self.hourseof.f_name, True)
        self.assertIsNotNone(self.hourseof.f_name)
        self.assertEqual(self.hourseof.l_name, 'Иванов')
        self.assertIsInstance(self.hourseof.l_name, str)
        self.assertTrue(self.hourseof.l_name, True)
        self.assertIsNotNone(self.hourseof.l_name)
        self.assertIsInstance(self.hourseof.work_hours, int)
        self.assertTrue(self.hourseof.work_hours, True)
        self.assertIsNotNone(self.hourseof.work_hours)

    def test_get_work_hours(self):
        self.assertEqual(self.hourseof.get_work_hours(), 18)
        self.assertRaises(TypeError, self.hourseof.get_work_hours, None)
        self.assertRaises(TypeError, self.hourseof.get_work_hours, 0)
        self.assertIsInstance(self.hourseof.get_work_hours(), int)
        self.assertIsNotNone(self.hourseof.get_work_hours())


if __name__ == "__main__":
    unittest.main()
