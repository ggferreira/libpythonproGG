from unittest.mock import Mock

from libpythonproGG import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'gabriel', 'id': 2669,
        'avatar_url': 'https://avatars.githubusercontent.com/u/2669?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('gabriel')
    assert 'https://avatars.githubusercontent.com/u/2669?v=4' == url
