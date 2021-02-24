import unittest
from hw10 import Enterprise, Department, Person

class TestEnterprise(unittest.TestCase):

    name = 'Звезда'
    town = 'г.Тольятти'
    enterprise = Enterprise(name, town)

    def test_name_and_town(self):
        self.assertEqual(self.enterprise.name, self.name)
        self.assertNotEqual(self.enterprise.name, '')
        self.assertNotEqual(self.enterprise.name, ' ')
        self.assertTrue(self.enterprise.name, True)

        self.assertEqual(self.enterprise.town, self.town)
        self.assertNotEqual(self.enterprise.town, ' ')
        self.assertNotEqual(self.enterprise.town, '')
        self.assertTrue(self.enterprise.town, True)


    def test_get_all_Control(self):
        self.name = 'Отдел управления предприятием'
        self.code_dep = 'Код отдела: 100'
        self.employers = 'Сотрудники:[]'
        # self.name = [1, 2]
        # self.code_dep = None
        # employers = None

        self.assertEqual(self.enterprise.get_all_Control(), (self.name, self.code_dep, self.employers))
        self.assertNotEqual(self.enterprise.get_all_Control(), ('', '', ''))
        self.assertNotEqual(self.enterprise.get_all_Control(), (' ', ' ', ' '))
        self.assertIsInstance(self.code_dep, str)
        self.assertIsInstance(self.employers, str)
        self.assertIsInstance(self.name, str)

    
    def test_get_all_HumResDep(self):
        self.name = 'Отдел кадров'
        self.code_dep = 'Код отдела: 10'
        self.employers = 'Сотрудники:[]'
        # self.name = [1, 2]
        # self.code_dep = None
        # employers = 0 

        self.assertEqual(self.enterprise.get_all_HumResDep(), (self.name, self.code_dep, self.employers))
        self.assertNotEqual(self.enterprise.get_all_HumResDep(), ('', '', ''))
        self.assertNotEqual(self.enterprise.get_all_HumResDep(), (' ', ' ', ' '))
        self.assertIsInstance(self.code_dep, str)
        self.assertIsInstance(self.employers, str)
        self.assertIsInstance(self.name, str)


    def test_get_all_Bookkeeping(self):
        self.name = 'Бухгалтерия'
        self.code_dep = 'Код отдела: 20'
        self.employers = 'Сотрудники:[]'
        # self.name = [1, 2]
        # self.code_dep = None
        # employers = 0

        # self.assertEqual(self.enterprise.get_all_Bookkeeping(), (5))
        self.assertEqual(self.enterprise.get_all_Bookkeeping(), (self.name, self.code_dep, self.employers))
        self.assertNotEqual(self.enterprise.get_all_Bookkeeping(), ('', '', ''))
        self.assertNotEqual(self.enterprise.get_all_Bookkeeping(), (' ', ' ', ' '))
        self.assertIsInstance(self.code_dep, str)
        self.assertIsInstance(self.employers, str)
        self.assertIsInstance(self.name, str)


    def test_get_all_Production(self):
        self.name = 'Отдел Продукции'
        self.code_dep = 'Код отдела: 30'
        self.employers = 'Сотрудники:[]'
        # self.name = [1, 2]
        # self.code_dep = None
        # employers = 0 

        # self.assertEqual(self.enterprise.get_all_Bookkeeping(), (5))
        self.assertEqual(self.enterprise.get_all_Production(), (self.name, self.code_dep, self.employers))
        self.assertNotEqual(self.enterprise.get_all_Production(), ('', '', ''))
        self.assertNotEqual(self.enterprise.get_all_Production(), (' ', ' ', ' '))
        self.assertIsInstance(self.code_dep, str)
        self.assertIsInstance(self.employers, str)
        self.assertIsInstance(self.name, str)


class TestDepartment(unittest.TestCase):

    department = Department()

    def test_add_empl(self):
        self.assertRaises(TypeError, self.department.add_empl, None)
        self.assertRaises(TypeError, self.department.add_empl, 0)
        self.assertIsNotNone(self.department.add_empl())


class TestPerson(unittest.TestCase):

    person = Person('Здоровяк', 'Олег', 'Александрович', '01.02.1965', '8-800-2000-600')

    def test_init(self):
        self.assertIsInstance(self.person._l_name, str)
        self.assertIsInstance(self.person._f_name, str)
        self.assertIsInstance(self.person._m_name, str)
        self.assertIsInstance(self.person._birthday, str)
        self.assertIsInstance(self.person._phone, str)

    def test_get_full_name(self):
        self.assertEqual(self.person.get_full_name(), 'Здоровяк О. А.')
        self.assertNotEqual(self.person.get_full_name(), ' ')
        self.assertNotEqual(self.person.get_full_name(), '')
        self.assertRaises(TypeError, self.person.get_full_name, None)
        self.assertRaises(TypeError, self.person.get_full_name, 0)
        self.assertIsNotNone(self.person.get_full_name())
        self.assertIsInstance(self.person.get_full_name(), str)
        
    def test_get_birthday(self):
        self.assertEqual(self.person.get_birthday(), '01.02.1965')
        self.assertNotEqual(self.person.get_birthday(), ' ')
        self.assertNotEqual(self.person.get_birthday(), '')
        self.assertRaises(TypeError, self.person.get_birthday, None)
        self.assertRaises(TypeError, self.person.get_birthday, 0)
        self.assertIsNotNone(self.person.get_birthday())
        self.assertIsInstance(self.person.get_birthday(), str)


    def test_get_phone(self):
        self.assertEqual(self.person.get_phone(), '8-800-2000-600')
        self.assertNotEqual(self.person.get_phone(), ' ')
        self.assertNotEqual(self.person.get_phone(), '')
        self.assertRaises(TypeError, self.person.get_phone, None)
        self.assertRaises(TypeError, self.person.get_phone, 0)
        self.assertIsNotNone(self.person.get_phone())
        self.assertIsInstance(self.person.get_phone(), str)
        

if __name__ == "__main__":
    unittest.main()
