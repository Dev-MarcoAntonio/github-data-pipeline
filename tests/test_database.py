import pytest
from unittest.mock import Mock,patch
from src.database import connect_database
import psycopg
from src.database import save_repositories_to_db

def test_connect_database_success(monkeypatch):

    monkeypatch.setenv('DB_HOST','localhost')
    monkeypatch.setenv('DB_PORT','5432')
    monkeypatch.setenv('DB_NAME','github_data_pipeline')
    monkeypatch.setenv('DB_USER','postgres')
    monkeypatch.setenv('DB_PASSWORD','test_password')

    mock_connection = Mock()

    with patch('src.database.psycopg.connect',return_value = mock_connection) as mock_connect:
        
        result = connect_database()

        assert result is mock_connection

        mock_connect.assert_called_once_with(
            host='localhost',
            port='5432',
            dbname='github_data_pipeline',
            user='postgres',
            password='test_password'
        )

def test_connect_database_failure():

    with patch('src.database.psycopg.connect',side_effect = psycopg.Error):

        result = connect_database()

        assert result is None

def test_save_repositories_to_db_success():

    mock_connection = Mock()
    mock_cursor = Mock()

    mock_connection.cursor.return_value = mock_cursor

    with patch('src.database.connect_database',return_value = mock_connection):

        repositories =  [
        {
            'name': 'projeto-python',
            'full_name': 'usuario/projeto-python',
            'language': 'Python',
            'stars': 20,
            'forks': 30
        }
    ]

        result = save_repositories_to_db(repositories)

        mock_cursor.execute.assert_called_once()
        mock_connection.commit.assert_called_once()

        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()

        assert result is True

def test_save_repositories_to_db_failure():

    mock_connection = Mock()
    mock_cursor = Mock()

    mock_connection.cursor.return_value = mock_cursor
    mock_cursor.execute.side_effect = psycopg.Error('Database error')

    with patch('src.database.connect_database',return_value = mock_connection):

        repositories =  [
        {
            'name': 'projeto-python',
            'full_name': 'usuario/projeto-python',
            'language': 'Python',
            'stars': 20,
            'forks': 30
        }
    ]

        result = save_repositories_to_db(repositories)

        mock_connection.rollback.assert_called_once()
        mock_connection.commit.assert_not_called()

        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()

        assert result is False

def test_save_repositories_to_db_connection_failure():

    with patch('src.database.connect_database',return_value = None) as mock_connect:

        repositories =  [
            {
            'name': 'projeto-python',
            'full_name': 'usuario/projeto-python',
            'language': 'Python',
            'stars': 20,
            'forks': 30
            }
        ]

        result = save_repositories_to_db(repositories)

        mock_connect.assert_called_once()

        assert result is False