from django.urls import resolve, reverse
from pytest_django.asserts import assertContains, assertNotContains, assertTemplateUsed
import pytest


@pytest.mark.django_db
def test_about_me_view(about_me_response):
    assert about_me_response.status_code == 200

    assertContains(about_me_response, "About Akatama")
    assertContains(about_me_response, '<h1 id="test">test</h1>')
    assertNotContains(about_me_response, "fake")
    assertTemplateUsed(about_me_response, "about_me/about.html")
