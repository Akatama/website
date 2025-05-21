from about_me.models import AboutMe
from pytest_django.asserts import assertRaisesMessage
from django.core.exceptions import ValidationError


def test_about_me_content(AboutMe_object):
    assert AboutMe_object.title == "About Akatama"
    assert AboutMe_object.body == "#test"


def test_about_formatted_markdown(AboutMe_object):
    assert AboutMe_object.formatted_markdown == "<h1>test</h1>"


def test_about_me_save(AboutMe_object):
    AboutMe_object.body = "#Me"
    AboutMe_object.save()
    assert AboutMe_object.body == "#Me"


def test_about_me_cannot_create_second(AboutMe_object):
    with assertRaisesMessage(
        ValidationError, "There can only be one About Me, you cannot add another"
    ):
        (AboutMe.objects.create(title="About Akatama", body="#test"),)
