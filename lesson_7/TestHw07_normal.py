import unittest

from hw07_normal import School, Person, Pupil, Teacher

class TestSchool(unittest.TestCase):
    school_name = 'Начальная школа №1'
    town = 'Тольятти'
    pupils = [Pupil('Борисов', 'Борис', 'Борисович', '2А', 'Борисова А.В.', 'Борисов Б.А.'),
              Pupil('Наумов', 'Петр', 'Дмитриевич', '2А', 'Наумова А.В.', 'Наумов Д.А.'),]
    teachers = [Teacher('Федоров', 'Микола', 'Иванович', 'Историк', ['7А', '8А'])]
    school = School(school_name, town, teachers, pupils)

    def test_init(self):
        self.assertIsInstance(self.school.school_name, str)
        self.assertTrue(self.school.school_name, True)
        self.assertIsInstance(self.school.town, str)
        self.assertTrue(self.school.town, True)
        self.assertTrue(self.school.teachers, True)
        self.assertTrue(self.school.pupils, True)
        self.assertIsNotNone(self.school.teachers)
        self.assertIsNotNone(self.school.pupils)

    def test_get_school_classes(self):
        self.assertIsInstance(self.school.get_school_classes(), list)
        self.assertTrue(self.school.get_school_classes, True)
        self.assertIsNotNone(self.school.get_school_classes)

    def test_get_all_pupils(self):
        self.assertEqual(self.school.get_all_pupils(), ['Борисов Б. Б.', 'Наумов П. Д.'])
        self.assertIsInstance(self.school.get_all_pupils(), list)
        self.assertTrue(self.school.get_all_pupils, True)
        self.assertIsNotNone(self.school.get_all_pupils)


class TestPupil(unittest.TestCase):
    pupil = Pupil('Борисов', 'Борис', 'Борисович', '5А', 'Борисова А.В.', 'Борисов Б.А.')

    def test_init(self):
        self.assertIsInstance(self.pupil.f_name, str)
        self.assertTrue(self.pupil.f_name, True)
        self.assertIsInstance(self.pupil.m_name, str)
        self.assertTrue(self.pupil.m_name, True)
        self.assertIsInstance(self.pupil.l_name, str)
        self.assertTrue(self.pupil.l_name, True)
        self.assertIsInstance(self.pupil.school_class, str)
        self.assertTrue(self.pupil.school_class, True)
        self.assertIsInstance(self.pupil.parents, dict)
        self.assertTrue(self.pupil.parents, True)

    def test_get_full_name(self):
        self.assertEqual(self.pupil.get_full_name(), 'Борисов Б. Б.')
        self.assertNotEqual(self.pupil.get_full_name(), ' ')
        self.assertNotEqual(self.pupil.get_full_name(), '')
        self.assertRaises(TypeError, self.pupil.get_full_name, None)
        self.assertRaises(TypeError, self.pupil.get_full_name, 0)
        self.assertIsNotNone(self.pupil.get_full_name())
        self.assertIsInstance(self.pupil.get_full_name(), str)
        
    def test_get_parents(self):
        self.assertEqual(self.pupil.get_parents(), {'Мама:': 'Борисова А.В.', 'Папа:': 'Борисов Б.А.'})
        self.assertRaises(TypeError, self.pupil.get_parents, None)
        self.assertRaises(TypeError, self.pupil.get_parents, 0)
        self.assertIsNotNone(self.pupil.get_parents())
        self.assertIsInstance(self.pupil.get_parents(), dict)


    def test_get_school_class(self):
        self.assertEqual(self.pupil.get_school_class(), '5А')
        self.assertIsInstance(self.pupil.get_school_class(), str)
        self.assertNotEqual(self.pupil.get_school_class(), ' ')
        self.assertNotEqual(self.pupil.get_school_class(), '')
        self.assertRaises(TypeError, self.pupil.get_school_class, None)
        self.assertRaises(TypeError, self.pupil.get_school_class, 0)
        self.assertIsNotNone(self.pupil.get_school_class())


class TestTeacher(unittest.TestCase):
    teacher = Teacher('Горбунов', 'Иван', 'Иванович', 'Математика', ['7А', '8А'])

    def test_init(self):
        self.assertIsInstance(self.teacher.f_name, str)
        self.assertTrue(self.teacher.f_name, True)
        self.assertIsInstance(self.teacher.m_name, str)
        self.assertTrue(self.teacher.m_name, True)
        self.assertIsInstance(self.teacher.l_name, str)
        self.assertTrue(self.teacher.l_name, True)
        self.assertIsInstance(self.teacher.school_class, list)
        self.assertTrue(self.teacher.school_class, True)
        self.assertIsInstance(self.teacher.object_name, str)
        self.assertTrue(self.teacher.object_name, True)

    def test_get_full_name(self):
        self.assertEqual(self.teacher.get_full_name(), 'Горбунов И. И.')
        self.assertNotEqual(self.teacher.get_full_name(), ' ')
        self.assertNotEqual(self.teacher.get_full_name(), '')
        self.assertRaises(TypeError, self.teacher.get_full_name, None)
        self.assertRaises(TypeError, self.teacher.get_full_name, 0)
        self.assertIsNotNone(self.teacher.get_full_name())
        self.assertIsInstance(self.teacher.get_full_name(), str)
        
    def test_get_object_name(self):
        self.assertEqual(self.teacher.get_object_name(), 'математика')
        self.assertNotEqual(self.teacher.get_object_name(), ' ')
        self.assertNotEqual(self.teacher.get_object_name(), '')
        self.assertRaises(TypeError, self.teacher.get_object_name, None)
        self.assertRaises(TypeError, self.teacher.get_object_name, 0)
        self.assertIsNotNone(self.teacher.get_object_name())
        self.assertIsInstance(self.teacher.get_object_name(), str)

    def test_get_class(self):
        self.assertEqual(self.teacher.get_class(), ['7А', '8А'])
        self.assertIsInstance(self.teacher.get_class(), list)
        self.assertNotEqual(self.teacher.get_class, ' ')
        self.assertNotEqual(self.teacher.get_class(), '')
        self.assertRaises(TypeError, self.teacher.get_class, None)
        self.assertRaises(TypeError, self.teacher.get_class, 0)
        self.assertIsNotNone(self.teacher.get_class())


if __name__ == "__main__":
    unittest.main()
