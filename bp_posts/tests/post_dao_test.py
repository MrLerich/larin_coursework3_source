import pytest

from bp_posts.dao.post import Post
from bp_posts.dao.post_dao import PostDAO


def check_fields(post):
    fields = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]

    for field in fields:
        assert hasattr(post, field), f"Нет поля {field}"


class TestPostDAO:

    @pytest.fixture
    def post_dao(self):
        post_dao_instance = PostDAO('./bp_posts/tests/post_mock.json')
        return post_dao_instance

    def test_get_all_types(self, post_dao):
        posts = post_dao.get_all()
        assert type(posts) == list, 'Неверный тип для вывода постов'

        post = post_dao.get_all()[0]
        assert type(post) == Post, 'Неверный тип для вывода одного поста'

    def test_get_all_fields(self, post_dao):
        posts = post_dao.get_all()
        post = post_dao.get_all()[0]
        check_fields(post)

    # def test_get_all_correct_ids(self):
    #     posts = post_dao.get_all()
    #
    #     correct_pks = {1, 2, 3}
    #     pks = set([post.pk for post in posts])
    #     assert pks == correct_pks, "Не совпадают полученные pk"

    # #Функция получения одного по pk
    #
    # def test_get_by_pk_types(self, post_dao):
    #     post = post_dao.get_by_pk(1)
    #     assert type(post) == Post, "Не верный тип для первого поста"
    #
    # def test_get_by_pk_fields(self, post_dao):
    #     post = post_dao.get_by_pk(1)
    #     check_fields(post)
    #
    # def test_get_by_pk_none(self):
    #     post = post_dao.get_by_pk(888)
    #     assert post is None, "Должен быть None для несуществующих pk"

    # @pytest.mark.parametrize("pk", [1, 2, 3])
    # def test_get_by_pk_correct_id(self, post_dao, pk):
    #     post = post_dao.get_by_pk(pk)
    #     assert post.pk == pk, f'Не верный post.pk для для запрашиваемого поста с pk = {pk}'

    #Функция получения постов по автору

    def test_search






