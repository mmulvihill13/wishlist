from django.test import TestCase, SimpleTestCase #Import built in tooling form their test package
from django.urls import reverse #find url, give it the name of our urls and get the full paht thing of it liek rversing all th eurl details 

# Test to check cart 
class URLRoutingTestCase(TestCase):
    #test the cart url
    def test_cart_url(self):
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)
    #test uses the correct html
    def test_cart_template(self):
        response = self.client.get(reverse('cart'))
        self.assertTemplateUsed(response, 'cart/cart.html')

#Test if the button works for the cart
class ButtonTest(TestCase):
    def test_start_order(self):
        response = self.client.get(reverse('cart'))
        self.assertContains(response, f'href="{reverse("order:menu")}"')
        response = self.client.get(reverse('order:menu'))
        self.assertEqual(response.status_code, 200)