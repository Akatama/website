from resume.models import Resume
from pytest_django.asserts import assertRaisesMessage
from django.core.exceptions import ValidationError


def test_resume_content(Resume_object):
    assert Resume_object.body == "#test"


def test_resume_formatted_markdown(Resume_object):
    assert Resume_object.formatted_markdown == '<h1 id="test">test</h1>'


def test_resume_save(Resume_object):
    Resume_object.body = "#Me"
    Resume_object.save()
    assert Resume_object.body == "#Me"


def test_resume_cannot_create_second(Resume_object):
    with assertRaisesMessage(
        ValidationError, "There can only be one Resume, you cannot add another"
    ):
        (Resume.objects.create(body="#test"))
