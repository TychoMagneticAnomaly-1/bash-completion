import pytest


class Test(object):

    @pytest.mark.complete("opera ")
    def test_(self, completion):
        assert completion.list