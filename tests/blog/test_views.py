from django.urls import resolve, reverse
from pytest_django.asserts import assertContains, assertNotContains, assertTemplateUsed
import pytest


@pytest.mark.django_db
def test_blog_index_page_1(post_index_response_page1):
    assert post_index_response_page1.status_code == 200

    # post titles that do not appear on page 1
    assertNotContains(post_index_response_page1, "test1")
    assertNotContains(post_index_response_page1, "test2")
    assertNotContains(post_index_response_page1, "test3")

    # post intros that do not appear on page 1
    assertNotContains(post_index_response_page1, "test_1")
    assertNotContains(post_index_response_page1, "test_2")
    assertNotContains(post_index_response_page1, "test_3")

    # post categories that do not appear page 1
    assertNotContains(post_index_response_page1, "cat1")
    assertNotContains(post_index_response_page1, "cat2")

    # post category that do appear on page 1
    assertContains(post_index_response_page1, "cat3")

    # post titles that do appear on page 1
    assertContains(post_index_response_page1, "test4")
    assertContains(post_index_response_page1, "test5")
    assertContains(post_index_response_page1, "test6")
    assertContains(post_index_response_page1, "test7")
    assertContains(post_index_response_page1, "test8")
    assertContains(post_index_response_page1, "test9")
    assertContains(post_index_response_page1, "test40")
    assertContains(post_index_response_page1, "test41")
    assertContains(post_index_response_page1, "test42")
    assertContains(post_index_response_page1, "test43")

    # post intros that do appear on page 1
    assertContains(post_index_response_page1, "test_4")
    assertContains(post_index_response_page1, "test_5")
    assertContains(post_index_response_page1, "test_6")
    assertContains(post_index_response_page1, "test_7")
    assertContains(post_index_response_page1, "test_8")
    assertContains(post_index_response_page1, "test_9")
    assertContains(post_index_response_page1, "test_40")
    assertContains(post_index_response_page1, "test_41")
    assertContains(post_index_response_page1, "test_42")
    assertContains(post_index_response_page1, "test_43")

    assertContains(post_index_response_page1, "page=2")

    assertTemplateUsed(post_index_response_page1, "blog/index.html")


@pytest.mark.django_db
def test_blog_index_page_2(post_index_response_page2):
    assert post_index_response_page2.status_code == 200

    # post titles that do appear on page 2
    assertContains(post_index_response_page2, "test1")
    assertContains(post_index_response_page2, "test2")
    assertContains(post_index_response_page2, "test3")

    # post intros that do appear on page 2
    assertContains(post_index_response_page2, "test_1")
    assertContains(post_index_response_page2, "test_2")
    assertContains(post_index_response_page2, "test_3")

    # post categories that do appear page 2
    assertContains(post_index_response_page2, "cat1")
    assertContains(post_index_response_page2, "cat2")
    assertContains(post_index_response_page2, "cat3")

    # post titles that does not appear on page 2
    assertNotContains(post_index_response_page2, "test4")
    assertNotContains(post_index_response_page2, "test5")
    assertNotContains(post_index_response_page2, "test6")
    assertNotContains(post_index_response_page2, "test7")
    assertNotContains(post_index_response_page2, "test8")
    assertNotContains(post_index_response_page2, "test9")
    assertNotContains(post_index_response_page2, "test40")
    assertNotContains(post_index_response_page2, "test41")
    assertNotContains(post_index_response_page2, "test42")
    assertNotContains(post_index_response_page2, "test43")

    # post intros that does appear on page 2
    assertNotContains(post_index_response_page2, "test_4")
    assertNotContains(post_index_response_page2, "test_5")
    assertNotContains(post_index_response_page2, "test_6")
    assertNotContains(post_index_response_page2, "test_7")
    assertNotContains(post_index_response_page2, "test_8")
    assertNotContains(post_index_response_page2, "test_9")
    assertNotContains(post_index_response_page2, "test_40")
    assertNotContains(post_index_response_page2, "test_41")
    assertNotContains(post_index_response_page2, "test_42")
    assertNotContains(post_index_response_page2, "test_43")

    assertContains(post_index_response_page2, "page=1")

    assertTemplateUsed(post_index_response_page2, "blog/index.html")


@pytest.mark.django_db
def test_blog_category_page_1(blog_category_response_page1):
    assert blog_category_response_page1.status_code == 200

    # post titles that do not appear on page 1
    assertNotContains(blog_category_response_page1, "test1")
    assertNotContains(blog_category_response_page1, "test2")
    assertNotContains(blog_category_response_page1, "test3")

    # post intros that do not appear on page 1
    assertNotContains(blog_category_response_page1, "test_1")
    assertNotContains(blog_category_response_page1, "test_2")
    assertNotContains(blog_category_response_page1, "test_3")

    # post categories that do not appear page 1
    assertNotContains(blog_category_response_page1, "cat1")
    assertNotContains(blog_category_response_page1, "cat2")

    # post category that do appear on page 1
    assertContains(blog_category_response_page1, "cat3")

    # post titles that do appear on page 1
    assertContains(blog_category_response_page1, "test4")
    assertContains(blog_category_response_page1, "test5")
    assertContains(blog_category_response_page1, "test6")
    assertContains(blog_category_response_page1, "test7")
    assertContains(blog_category_response_page1, "test8")
    assertContains(blog_category_response_page1, "test9")
    assertContains(blog_category_response_page1, "test40")
    assertContains(blog_category_response_page1, "test41")
    assertContains(blog_category_response_page1, "test42")
    assertContains(blog_category_response_page1, "test43")
    #
    # post intros that do appear on page 1
    assertContains(blog_category_response_page1, "test_4")
    assertContains(blog_category_response_page1, "test_5")
    assertContains(blog_category_response_page1, "test_6")
    assertContains(blog_category_response_page1, "test_7")
    assertContains(blog_category_response_page1, "test_8")
    assertContains(blog_category_response_page1, "test_9")
    assertContains(blog_category_response_page1, "test_40")
    assertContains(blog_category_response_page1, "test_41")
    assertContains(blog_category_response_page1, "test_42")
    assertContains(blog_category_response_page1, "test_43")

    assertContains(blog_category_response_page1, "page=2")

    assertTemplateUsed(blog_category_response_page1, "blog/category.html")


@pytest.mark.django_db
def test_blog_category_page_2(blog_category_response_page2):
    assert blog_category_response_page2.status_code == 200

    # post titles that do appear on page 2
    assertContains(blog_category_response_page2, "test3")

    # post intros that do appear on page 2
    assertContains(blog_category_response_page2, "test_3")

    # post categories that do not appear page 2
    assertNotContains(blog_category_response_page2, "cat1")
    assertNotContains(blog_category_response_page2, "cat2")

    # post category that do appear on page 2
    assertContains(blog_category_response_page2, "cat3")

    # post titles that do not appear on page 2
    assertNotContains(blog_category_response_page2, "test4")
    assertNotContains(blog_category_response_page2, "test5")
    assertNotContains(blog_category_response_page2, "test6")
    assertNotContains(blog_category_response_page2, "test7")
    assertNotContains(blog_category_response_page2, "test8")
    assertNotContains(blog_category_response_page2, "test9")
    assertNotContains(blog_category_response_page2, "test40")
    assertNotContains(blog_category_response_page2, "test41")
    assertNotContains(blog_category_response_page2, "test42")

    # post intros that do not appear on page 2
    assertNotContains(blog_category_response_page2, "test_4")
    assertNotContains(blog_category_response_page2, "test_5")
    assertNotContains(blog_category_response_page2, "test_6")
    assertNotContains(blog_category_response_page2, "test_7")
    assertNotContains(blog_category_response_page2, "test_8")
    assertNotContains(blog_category_response_page2, "test_9")
    assertNotContains(blog_category_response_page2, "test_40")
    assertNotContains(blog_category_response_page2, "test_41")
    assertNotContains(blog_category_response_page2, "test_42")
    assertNotContains(blog_category_response_page2, "test_43")

    assertContains(blog_category_response_page2, "page=1")

    assertTemplateUsed(blog_category_response_page2, "blog/category.html")


@pytest.mark.django_db
def test_blog_detail(blog_detail_response):
    assert blog_detail_response.status_code == 200

    # title
    assertContains(blog_detail_response, "test1")
    assertContains(blog_detail_response, "By Jimmy Lindsey")
    assertNotContains(blog_detail_response, "Last Updated: ")

    # body
    assertContains(blog_detail_response, "<h1>Hi</h1>")

    # category
    assertContains(blog_detail_response, "cat3")
    assertContains(blog_detail_response, "Categories:")

    assertTemplateUsed(blog_detail_response, "blog/detail.html")
