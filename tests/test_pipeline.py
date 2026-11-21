from main import process_repositories,fetch_repositories,save_repositories
import pytest
from unittest.mock import Mock, patch
import requests
import json

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


def test_process_repositories_name_with_spaces():
    data_test = {
        'items': [
            {
            'name': '      ',
            'full_name': 'usuario/projeto-python',
            'language': 'Python',
            'stargazers_count': 100,
            'forks_count': 20
        }
        ]
    }
    result = process_repositories(data_test)

    assert result == []


def test_process_repositories_invalid_full_name():

    data_test = {
        'items': [
            {
            'name': 'project-python',
            'full_name': '',
            'language': 'Python',
            'stargazers_count': 100,
            'forks_count': 20
        }
        ]
    }
    result = process_repositories(data_test)

    assert result == []

def test_process_repositories_full_name_with_spaces():

    data_test = {
        'items': [
            {
                'name': 'projeto-python',
                'full_name': '      ',
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

    with patch('main.requests.get',return_value = mock_response) as mock_get:

        result = fetch_repositories()

        mock_get.assert_called_once_with(
            'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc&per_page=30',
            timeout=10
        )

        assert result == mock_response.json.return_value

def test_fetch_repositories_error():

    mock_response = Mock()

    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError

    with patch('main.requests.get',return_value = mock_response):

        result = fetch_repositories()

        assert result is None

def test_fetch_repositories_connection_error():

    with patch('main.requests.get',side_effect = requests.exceptions.ConnectionError):

        result = fetch_repositories()

        assert result is None

def test_fetch_repositories_invalid_json():

    mock_response = Mock()

    mock_response.raise_for_status.return_value = None

    mock_response.json.side_effect = requests.exceptions.JSONDecodeError(
        'JSON Inválido','',0
    )

    with patch('main.requests.get',return_value = mock_response):

        result = fetch_repositories()

        assert result is None

def test_save_repositories(tmp_path, monkeypatch):

    monkeypatch.chdir(tmp_path)

    data_test = [
    {
        'name': 'projeto-python',
        'full_name': 'usuario/projeto-python',
        'language': 'Python',
        'stars': 100,
        'forks': 20
    }
]
    save_repositories(data_test)

    file = tmp_path / 'data' / 'processed' / 'repositories.json'

    assert file.exists()

    with open(file,'r',encoding = 'utf-8') as file2:

        save_data = json.load(file2)

    assert save_data == data_test