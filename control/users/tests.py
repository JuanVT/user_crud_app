from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class UserViewsTests(TestCase):

    def setUp(self):
        # Creates an user for the test cases
        self.user = User.objects.create_user(
            'test',
            'test@test.com',
            'test'
        )

    def test_user_profile_view(self):
        # Test user profile when no user logged in
        response = self.client.get(reverse('view_profile'))

        # Redirects to home as there is no user logged in
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('users/profile.html')

        # Test user profile when logged in
        self.client.force_login(self.user)
        response = self.client.get(reverse('view_profile'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/profile.html')
