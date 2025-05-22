import pytest
from django.urls import reverse

from resume.models import Resume


@pytest.fixture
def resume_response(client):
    Resume.objects.create(body="test")
    url = reverse("resume_index")
    return client.get(url)


@pytest.fixture
def Resume_object(db):
    return Resume.objects.create(body="#test")
