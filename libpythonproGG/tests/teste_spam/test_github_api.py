from unittest.mock import Mock

import pytest

from libpythonproGG import github_api


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/2669?v=4'
    resp_mock.json.return_value = {
        'login': 'gabriel', 'id': 2669,
        'avatar_url': url,
    }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_original


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('gabriel')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('gabriel')
    assert 'https://avatars.githubusercontent.com/u/2669?v=4' == url
