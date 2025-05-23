import pytest
from django.urls import reverse

from blog.models import Post, Category


@pytest.fixture
def post_index_response_page1(client):
    cat_1 = Category.objects.create(name="cat1")
    cat_2 = Category.objects.create(name="cat2")
    cat_3 = Category.objects.create(name="cat3")
    post_1 = Post.objects.create(title="test1", intro="test_1", body="#test1")
    post_1.categories.add(cat_1)
    post_2 = Post.objects.create(title="test2", intro="test_2", body="#test2")
    post_2.categories.add(cat_2)
    post_3 = Post.objects.create(title="test3", intro="test_3", body="#test3")
    post_3.categories.add(cat_3)
    post_4 = Post.objects.create(title="test4", intro="test_4", body="#test4")
    post_4.categories.add(cat_3)
    post_5 = Post.objects.create(title="test5", intro="test_5", body="#test5")
    post_5.categories.add(cat_3)
    post_6 = Post.objects.create(title="test6", intro="test_6", body="#test6")
    post_6.categories.add(cat_3)
    post_7 = Post.objects.create(title="test7", intro="test_7", body="#test7")
    post_7.categories.add(cat_3)
    post_8 = Post.objects.create(title="test8", intro="test_8", body="#test8")
    post_8.categories.add(cat_3)
    post_9 = Post.objects.create(title="test9", intro="test_9", body="#test9")
    post_9.categories.add(cat_3)
    post_10 = Post.objects.create(title="test40", intro="test_40", body="#test40")
    post_10.categories.add(cat_3)
    post_11 = Post.objects.create(title="test41", intro="test_41", body="#test41")
    post_11.categories.add(cat_3)
    post_12 = Post.objects.create(title="test42", intro="test_42", body="#test42")
    post_12.categories.add(cat_3)
    post_13 = Post.objects.create(title="test43", intro="test_43", body="#test43")
    post_13.categories.add(cat_3)
    url = reverse("blog_index")
    return client.get(url)


@pytest.fixture
def post_index_response_page2(client):
    cat_1 = Category.objects.create(name="cat1")
    cat_2 = Category.objects.create(name="cat2")
    cat_3 = Category.objects.create(name="cat3")
    post_1 = Post.objects.create(title="test1", intro="test_1", body="#test1")
    post_1.categories.add(cat_1)
    post_2 = Post.objects.create(title="test2", intro="test_2", body="#test2")
    post_2.categories.add(cat_2)
    post_3 = Post.objects.create(title="test3", intro="test_3", body="#test3")
    post_3.categories.add(cat_3)
    post_4 = Post.objects.create(title="test4", intro="test_4", body="#test4")
    post_4.categories.add(cat_3)
    post_5 = Post.objects.create(title="test5", intro="test_5", body="#test5")
    post_5.categories.add(cat_3)
    post_6 = Post.objects.create(title="test6", intro="test_6", body="#test6")
    post_6.categories.add(cat_3)
    post_7 = Post.objects.create(title="test7", intro="test_7", body="#test7")
    post_7.categories.add(cat_3)
    post_8 = Post.objects.create(title="test8", intro="test_8", body="#test8")
    post_8.categories.add(cat_3)
    post_9 = Post.objects.create(title="test9", intro="test_9", body="#test9")
    post_9.categories.add(cat_3)
    post_10 = Post.objects.create(title="test40", intro="test_40", body="#test40")
    post_10.categories.add(cat_3)
    post_11 = Post.objects.create(title="test41", intro="test_41", body="#test41")
    post_11.categories.add(cat_3)
    post_12 = Post.objects.create(title="test42", intro="test_42", body="#test42")
    post_12.categories.add(cat_3)
    post_13 = Post.objects.create(title="test43", intro="test_43", body="#test43")
    post_13.categories.add(cat_3)
    url = f"{reverse('blog_index')}?page=2"
    return client.get(url)


@pytest.fixture
def blog_category_response_page1(client):
    cat_3 = Category.objects.create(name="cat3")
    post_3 = Post.objects.create(title="test3", intro="test_3", body="#test3")
    post_3.categories.add(cat_3)
    post_4 = Post.objects.create(title="test4", intro="test_4", body="#test4")
    post_4.categories.add(cat_3)
    post_5 = Post.objects.create(title="test5", intro="test_5", body="#test5")
    post_5.categories.add(cat_3)
    post_6 = Post.objects.create(title="test6", intro="test_6", body="#test6")
    post_6.categories.add(cat_3)
    post_7 = Post.objects.create(title="test7", intro="test_7", body="#test7")
    post_7.categories.add(cat_3)
    post_8 = Post.objects.create(title="test8", intro="test_8", body="#test8")
    post_8.categories.add(cat_3)
    post_9 = Post.objects.create(title="test9", intro="test_9", body="#test9")
    post_9.categories.add(cat_3)
    post_10 = Post.objects.create(title="test40", intro="test_40", body="#test40")
    post_10.categories.add(cat_3)
    post_11 = Post.objects.create(title="test41", intro="test_41", body="#test41")
    post_11.categories.add(cat_3)
    post_12 = Post.objects.create(title="test42", intro="test_42", body="#test42")
    post_12.categories.add(cat_3)
    post_13 = Post.objects.create(title="test43", intro="test_43", body="#test43")
    post_13.categories.add(cat_3)
    url = reverse("blog_category", args=["cat3"])
    return client.get(url)


@pytest.fixture
def blog_category_response_page2(client):
    cat_3 = Category.objects.create(name="cat3")
    post_3 = Post.objects.create(title="test3", intro="test_3", body="#test3")
    post_3.categories.add(cat_3)
    post_4 = Post.objects.create(title="test4", intro="test_4", body="#test4")
    post_4.categories.add(cat_3)
    post_5 = Post.objects.create(title="test5", intro="test_5", body="#test5")
    post_5.categories.add(cat_3)
    post_6 = Post.objects.create(title="test6", intro="test_6", body="#test6")
    post_6.categories.add(cat_3)
    post_7 = Post.objects.create(title="test7", intro="test_7", body="#test7")
    post_7.categories.add(cat_3)
    post_8 = Post.objects.create(title="test8", intro="test_8", body="#test8")
    post_8.categories.add(cat_3)
    post_9 = Post.objects.create(title="test9", intro="test_9", body="#test9")
    post_9.categories.add(cat_3)
    post_10 = Post.objects.create(title="test40", intro="test_40", body="#test40")
    post_10.categories.add(cat_3)
    post_11 = Post.objects.create(title="test41", intro="test_41", body="#test41")
    post_11.categories.add(cat_3)
    post_12 = Post.objects.create(title="test42", intro="test_42", body="#test42")
    post_12.categories.add(cat_3)
    post_13 = Post.objects.create(title="test43", intro="test_43", body="#test43")
    post_13.categories.add(cat_3)
    url = f"{reverse('blog_category', args=['cat3'])}?page=2"
    return client.get(url)


@pytest.fixture
def blog_detail_response(client):
    cat_3 = Category.objects.create(name="cat3")
    post_1 = Post.objects.create(title="test1", intro="test_1", body="#Hi")
    post_1.categories.add(cat_3)
    url = reverse("blog_detail", args=[1])
    return client.get(url)


@pytest.fixture
def Post_object(db):
    return Post.objects.create(title="test1", intro="test1", body="#test1")


@pytest.fixture
def Category_object(db):
    return Category.objects.create(name="test")
