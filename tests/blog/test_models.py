from blog.models import Post, Category
from pytest_django.asserts import assertRaisesMessage
from django.core.exceptions import ValidationError


def test_post_content(Post_object):
    assert Post_object.title == "test1"
    assert Post_object.intro == "test1"
    assert Post_object.body == "#test1"


def test_post_formatted_markdown(Post_object):
    assert Post_object.formatted_markdown == '<h1 id="test1">test1</h1>'


def test_post_save(Post_object):
    Post_object.body = "#Me"
    Post_object.save()
    assert Post_object.body == "#Me"


def test_category_content(Category_object):
    assert Category_object.name == "test"


def test_category_save(Category_object):
    Category_object.name = "Me"
    Category_object.save()
    assert Category_object.name == "Me"
