from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from .models import (
    # User,
    CustomUser,
    Parent,
    Student,
    Task,
    Site,
)

class UserTest(TestCase):


    def setUp(self):
        self.user = CustomUser.objects.create(
            username = 'Debugger',
            password = 'uncommon',
            is_parent = True,
        )

    def test_creation(self):
        self.assertIsInstance(self.user, CustomUser)
        self.assertEqual(self.user.username, 'Debugger')
        self.assertIsNotNone(self.user.password)
        self.assertNotEqual(self.user.password, 'foobar')
    
    def test_unique_user(self):
        try:
            duplicate_user = CustomUser.objects.create(
                username = 'Debugger',
                password = 'random',  
            )
        except IntegrityError:
            pass

class ParentTest(TestCase):


    def setUp(self):

        self.user = CustomUser.objects.create(
            username = 'Debugger_Parent',
            password = 'uncommon',
            is_parent = True,
        )

        self.user2 = CustomUser.objects.create(
            username = 'Random_Parent',
            password = 'uncommon',
            is_parent = True,
        )

        self.parent = Parent.objects.create(
            user_id = self.user,
            email = 'debugger@email.com',
            name = 'Debug Parent',
            cellphone = 1234567890,
        )
    
    def test_creation(self):
        self.assertIsInstance(self.parent, Parent)
        self.assertEqual(self.parent.email, 'debugger@email.com')

    def test_unique_email(self):
        try:
            duplicate_email = Parent.objects.create(
                user_id = self.user2,
                email = 'debugger@email.com',
                name = 'Random Parent',
                cellphone = 1234567890,
            )
        
        except IntegrityError:
            pass

class StudentTest(TestCase):


    def setUp(self):

        self.student_user = CustomUser.objects.create(
            username = 'Debugger_Student',
            password = 'uncommon',
            is_parent = False,
        )

        self.parent_user = CustomUser.objects.create(
            username = 'Debugger_Parent',
            password = 'uncommon',
            is_parent = False,
        )

        self.parent = Parent.objects.create(
            user_id = self.parent_user,
            email = 'debugger@email.com',
            name = 'Debug_Student Parent',
            cellphone = 1234567890,
        )

        self.student = Student.objects.create(
            user_id = self.student_user,
            parent_id = self.parent,
            name = 'Bob Debugger'
        )

    def test_creation(self):
        self.assertIsInstance(self.student, Student)
        self.assertEqual(self.student.name, 'Bob Debugger')
        self.assertEqual(self.student.parent_id.name, 'Debug_Student Parent')

class TaskTest(TestCase):

    def setUp(self):

        self.student_user = CustomUser.objects.create(
            username = 'Debugger_Student',
            password = 'uncommon',
            is_parent = False,
        )

        self.parent_user = CustomUser.objects.create(
            username = 'Debugger_Parent',
            password = 'uncommon',
            is_parent = False,
        )

        self.parent = Parent.objects.create(
            user_id = self.parent_user,
            email = 'debugger@email.com',
            name = 'Debug_Student Parent',
            cellphone = 1234567890,
        )

        self.student = Student.objects.create(
            user_id = self.student_user,
            parent_id = self.parent,
            name = 'Bob Debugger'
        )

        self.task = Task.objects.create(
            student_id = self.student,
            class_topic = 'Math Review',
            description = 'Big test ahead',
            priority = 'N',
        )

    def test_creation(self):
        self.assertIsInstance(self.task, Task)
        self.assertEqual(self.task.class_topic, 'Math Review')
        self.assertEqual(self.task.completed, False)

class SiteTest(TestCase):

    def setUp(self):

        self.student_user = CustomUser.objects.create(
            username = 'Debugger_Student',
            password = 'uncommon',
            is_parent = False,
        )

        self.parent_user = CustomUser.objects.create(
            username = 'Debugger_Parent',
            password = 'uncommon',
            is_parent = False,
        )

        self.parent = Parent.objects.create(
            user_id = self.parent_user,
            email = 'debugger@email.com',
            name = 'Debug_Student Parent',
            cellphone = 1234567890,
        )

        self.student = Student.objects.create(
            user_id = self.student_user,
            parent_id = self.parent,
            name = 'Bob Debugger'
        )

        self.site = Site.objects.create(
            student_id = self.student,
            url = 'codefellows.org',
            account = 'debugger-codefellows',
            password = 'uncommon-coder',
            class_topic = 'Math',
        )

    def test_creation(self):
        self.assertIsInstance(self.site, Site)
        self.assertEqual(self.site.url, 'codefellows.org')
        self.assertEqual(self.site.student_id.name, 'Bob Debugger')
        self.assertEqual(self.site.student_id.parent_id.name, 'Debug_Student Parent')