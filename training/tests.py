from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    def setUp(self):
        self.User = get_user_model()

    def test_create_coach_user(self):
        user = self.User.objects.create_user(
            username="coach_user",
            email="coach@example.com",
            password="testpassword123",
            role="coach"
        )
        self.assertEqual(user.role, "coach")
        self.assertTrue(user.check_password("testpassword123"))

    def test_create_student_user(self):
        user = self.User.objects.create_user(
            username="student_user",
            email="student@example.com",
            password="testpassword123",
            role="student"
        )
        self.assertEqual(user.role, "student")
        self.assertTrue(user.check_password("testpassword123"))

    def test_superuser_role(self):
        superuser = self.User.objects.create_superuser(
            username="admin_user",
            email="admin@example.com",
            password="adminpassword123"
        )
        self.assertEqual(superuser.role, "student")  
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
