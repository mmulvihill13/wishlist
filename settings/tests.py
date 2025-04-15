from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import UserUpdateForm

User = get_user_model()
class SettingsViewTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

    def test_setting_page_get(self):
        response = self.client.get(reverse('settings:setting'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings/settings.html')

    def test_update_user_get_request(self):
        response = self.client.get(reverse('settings:update_user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings/update_user.html')
        self.assertIsInstance(response.context['form'], UserUpdateForm)


class UserUpdateFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123', email='testuser@example.com')
    def test_form_valid_data(self):
        form_data = {
            'first_name': 'Bryce',
            'last_name': 'Kriner',
            'email': 'krinerbk@hotmail.com',
            'password': '123Django',
        }
        form = UserUpdateForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())
        updated_user = form.save()
        self.assertEqual(updated_user.first_name, 'Bryce')
        self.assertEqual(updated_user.last_name, 'Kriner')
        self.assertEqual(updated_user.email, 'krinerbk@hotmail.com')
        self.assertTrue(updated_user.check_password('123Django'))\
        
        form_data = {
            'first_name': 'Byce',
            'last_name': 'Kiner',
            'email': 'krinrbk@hotmail.com',
            'password': '123jango',
        }
        form = UserUpdateForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())
        updated_user = form.save()
        self.assertNotEqual(updated_user.first_name, 'Bryce')
        self.assertNotEqual(updated_user.last_name, 'Kriner')
        self.assertNotEqual(updated_user.email, 'krinerbk@hotmail.com')
        self.assertFalse(updated_user.check_password('123Django'))
        
