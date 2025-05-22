from django.urls import resolve, reverse
from pytest_django.asserts import assertContains, assertNotContains, assertTemplateUsed
import pytest


@pytest.mark.django_db
def test_resume_view(resume_response):
    assert resume_response.status_code == 200

    assertContains(resume_response, "test")
    assertNotContains(resume_response, "fake")
    assertTemplateUsed(resume_response, "resume/resume.html")
