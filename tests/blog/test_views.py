from django.urls import resolve, reverse
from pytest_django.asserts import assertContains, assertNotContains, assertTemplateUsed
import pytest


@pytest.mark.django_db
def test_blog_index(post_index_response):
    assert post_index_response.status_code == 200

    assertContains(post_index_response, "test")
    assertTemplateUsed(post_index_response, "blog/index.html")


@pytest.mark.django_db
def test_blog_category(blog_category_response):
    assert blog_category_response.status_code == 200

    assertContains(blog_category_response, "test3")
    assertTemplateUsed(blog_category_response, "blog/category.html")


@pytest.mark.django_db
def test_blog_detail(blog_detail_response):
    assert blog_detail_response.status_code == 200

    assertContains(blog_detail_response, "test")
    assertTemplateUsed(blog_detail_response, "blog/detail.html")
