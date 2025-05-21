import pytest
from django.urls import reverse

from about_me.models import AboutMe


@pytest.fixture
def about_me_response(client):
    AboutMe.objects.create(title="About Akatama", body="test")
    url = reverse("about_index")
    return client.get(url)


@pytest.fixture
def AboutMe_object(db):
    return AboutMe.objects.create(title="About Akatama", body="#test")
