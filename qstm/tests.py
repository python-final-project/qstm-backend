# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from django.db.utils import IntegrityError
# from .models import (
#     User,
#     Parent,
#     Student,
#     Task,
#     Site,
# )

# class AccountTests(TestCase):


#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             username = 'Debugger',
#             email = 'debug@email.com',
#             password = 'uncommon',
#         )

#     def test_creation(self):
#         self.assertIsInstance(self.user, User)