from django.test import TestCase, Client
from django.urls import reverse
from .models import Author, Category, Article


class NewsPortalTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(name='Test Author', email='test@author.com')
        self.category = Category.objects.create(name='Technology', slug='technology')
        self.article = Article.objects.create(
            title='Test Article Title',
            slug='test-article-title',
            author=self.author,
            category=self.category,
            summary='Test summary',
            content='<p>Test content with HTML</p>'
        )

    def test_home_view(self):
        response = self.client.get(reverse('news:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Article Title')

    def test_article_detail_view(self):
        response = self.client.get(reverse('news:article_detail', args=[self.article.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Article Title')
        self.assertContains(response, 'Test content with HTML')

    def test_category_list_view(self):
        response = self.client.get(reverse('news:category_list', args=[self.category.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Technology')
        self.assertContains(response, 'Test Article Title')
