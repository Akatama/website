import pytest
from django.urls import reverse

from blog.models import Post, Category


@pytest.fixture
def post_index_response(client):
    Post.objects.create(title="test1", intro="test1", body="#test1")
    Post.objects.create(title="test2", intro="test2", body="#test2")
    Post.objects.create(title="test3", intro="test3", body="#test3")
    Post.objects.create(title="test4", intro="test4", body="#test4")
    Post.objects.create(title="test5", intro="test5", body="#test5")
    Post.objects.create(title="test6", intro="test6", body="#test6")
    Post.objects.create(title="test7", intro="test7", body="#test7")
    Post.objects.create(title="test8", intro="test8", body="#test8")
    Post.objects.create(title="test9", intro="test9", body="#test9")
    Post.objects.create(title="test10", intro="test10", body="#test10")
    Post.objects.create(title="test11", intro="test11", body="#test11")
    url = reverse("blog_index")
    return client.get(url)


@pytest.fixture
def blog_category_response(client):
    Category.objects.create(name="test3")
    url = reverse("blog_category", args=["test3"])
    return client.get(url)


@pytest.fixture
def blog_detail_response(client):
    Post.objects.create(title="test1", intro="test1", body="#test1")
    url = reverse("blog_detail", args=[1])
    return client.get(url)


@pytest.fixture
def Post_object(db):
    return Post.objects.create(title="test1", intro="test1", body="#test1")


@pytest.fixture
def Category_object(db):
    return Category.objects.create(name="test")
