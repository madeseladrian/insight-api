from inspect import isabstract

from src.data.contracts.db.account import UpdateAccessTokenRepository


class TestUpdateAccessTokenRepository:
    def test_1_should_UpdateAccessTokenRepository_is_an_abstract_class(self):
        assert isabstract(UpdateAccessTokenRepository)
