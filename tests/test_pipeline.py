from main import process_repositories,fetch_repositories
import pytest
from unittest.mock import Mock, patch

def test_process_repositories():

    data_test = {
        'items': [
            {
                'name': 'projeto-python',
                'full_name': 'usuario/projeto-python',
                'language': 'Python',
                'stargazers_count': 100,
                'forks_count': 20
            }
        ]
    }

    result = process_repositories(data_test)

    assert len(result) == 1

def test_process_repositories_invalid_name():

    data_test = {
        'items': [
            {
            'name': '',
            'full_name': 'usuario/projeto-python',
            'language': 'Python',
            'stargazers_count': 100,
            'forks_count': 20
        }
        ]
    }
    result = process_repositories(data_test)

    assert result == []

@pytest.mark.parametrize('stars',[None,-20,'cem'])

def test_process_repositories_invalid_stars(stars):

    data_test = {
        'items': [
        {
            'name': 'projeto-python',
            'full_name': 'usuario/projeto-python',
            'language': 'Python',
            'stargazers_count': stars,
            'forks_count': 20
        }
        ]
    }
    result = process_repositories(data_test)

    assert result == []

@pytest.mark.parametrize('forks',[None,-20,'vinte'])

def test_process_repositories_invalid_forks(forks):

    data_test = {
        'items': [
        {
            'name': 'projeto-python',
            'full_name': 'usuario/projeto-python',
            'language': 'Python',
            'stargazers_count': 20,
            'forks_count': forks
        }
        ]
    }

    result = process_repositories(data_test)

    assert result == []

def test_process_repositories_empty_items():

    data_test = {
        'items': []
    }

    result = process_repositories(data_test)

    assert result == []

def test_fetch_repositories_success():

    mock_response = Mock()

    mock_response.raise_for_status.return_value = None

    mock_response.json.return_value = {
        'items': [
            {
                'name': 'projeto-python',
                'full_name': 'usuario/projeto-python',
                'language': 'Python',
                'stargazers_count': 100,
                'forks_count': 20
            }
        ]
    }

    with patch('main.requests.get',return_value = mock_response):

        result = fetch_repositories()

        assert result == mock_response.json.return_value
