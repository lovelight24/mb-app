from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.

class PostModelTest(TestCase):
	"""docstring for PostModelTest"TestCase"""
	def setUp(self):
		Post.objects.create(text="Just a test")

	def test_text_content(self):
		posts = Post.objects.get(id=1)
		expected_object_name = f'{posts.text}'
		self.assertEqual(expected_object_name, "Just a test")


class HomePageViewTest(TestCase):
	"""docstring for HomePageViewTest"SimpleTestCase"""
	def setUp(self):
		Post.objects.create(text="Home Page Testcase")


	def test_view_url_proper_location(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code,200)


	def test_view_url_by_name(self):
		resp = self.client.get(reverse('Home'))
		self.assertEqual(resp.status_code, 200)


	def test_view_uses_correct_template(self):
		resp = self.client.get(reverse('Home'))
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'home.html')
