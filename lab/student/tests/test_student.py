from unittest import TestCase, main
from project_14.student import Student


# class Student:
#     def __init__(self, name: str, courses=None):
#         if courses is None:
#             courses = {}
#         self.name = name
#         self.courses = courses  # {course_name: [notes]}

class TestStudent(TestCase):
    STUDENT_NAME = 'Daniel'

    def setUp(self) -> None:
        self.student = Student(self.STUDENT_NAME)

    def test_student_init_with_courses(self):
        self.assertEqual(self.STUDENT_NAME, self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_student_init_without_courses(self):
        courses = {"Python Advanced": ['note1', 'note2']}

        student = Student(self.STUDENT_NAME, courses)

        self.assertEqual(self.STUDENT_NAME, student.name)
        self.assertEqual(courses, student.courses)

# -----------------------------------------------------------------

#     def enroll(self, course_name: str, notes, add_course_notes: str = ""):
#         if course_name in self.courses.keys():
#             [self.courses[course_name].append(x) for x in notes]
#             return "Course already added. Notes have been updated."
#
#         if add_course_notes == "Y" or add_course_notes == "":
#             self.courses[course_name] = notes
#             return "Course and course notes have been added."
#
#         self.courses[course_name] = []
#         return "Course has been added."

    def test_enroll_student_updates_course_notes_when_course_is_already_enrolled(self):
        course_name = "Python Advanced"
        courses = {course_name: ['note1', 'note2']}

        student = Student(self.STUDENT_NAME, courses)

        result = student.enroll(course_name, ['note3', 'note4'])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(['note1', 'note2', 'note3', 'note4'], student.courses[course_name])

    def test_enroll_student_extends_courses_with_course_and_notes_when_add_course_notes_is_not_passed(self):
        course_name = "Python OOP"
        course_notes = ['note1', 'note2']
        result = self.student.enroll(course_name, course_notes)

        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual(course_notes, self.student.courses[course_name])

    def test_enroll_student_extends_courses_with_course_and_notes_when_add_course_notes_is_y(self):
        course_name = "Python OOP"
        course_notes = ['note1', 'note2']
        result = self.student.enroll(course_name, course_notes, "Y")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual(course_notes, self.student.courses[course_name])

    def test_enroll_student_extends_courses_with_course_without_notes_when_invalid_add_course(self):
        course_name = "Python OOP"
        course_notes = ['note1', 'note2']
        result = self.student.enroll(course_name, course_notes, "N")

        self.assertEqual("Course has been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual([], self.student.courses[course_name])

# -----------------------------------------------------------------

#     def add_notes(self, course_name, notes):
#         if course_name in self.courses.keys():
#             self.courses[course_name].append(notes)
#             return "Notes have been updated"
#         raise Exception("Cannot add notes. Course not found.")

    def test_add_notes_raises_error_when_course_is_not_existing(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Python Advanced", 'Note 3')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_updates(self):
        course_name = "Python Advanced"
        courses = {course_name: ['note 1', 'note 2']}
        student = Student(self.STUDENT_NAME, courses)

        result = student.add_notes(course_name, 'note 3')

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(['note 1', 'note 2', 'note 3'], student.courses[course_name])

# -----------------------------------------------------------------

#     def leave_course(self, course_name):
#         if course_name in self.courses.keys():
#             self.courses.pop(course_name)
#             return "Course has been removed"
#         raise Exception("Cannot remove course. Course not found.")

    def test_leave_course_raises_error(self):
        self.student.enroll("Python Basics", [])

        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Python Advanced")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_removes_course(self):
        course_name = "Python Advanced"

        student = Student(self.STUDENT_NAME, {course_name: []})

        result = student.leave_course(course_name)
        self.assertEqual("Course has been removed", result)
        self.assertTrue(course_name not in student.courses)


if __name__ == '__main__':
    main()
