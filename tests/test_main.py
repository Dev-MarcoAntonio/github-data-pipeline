from unittest.mock import patch
from main import main

def test_main_success():

    with patch('main.setup_logging') as mock_logging, \
         patch('main.fetch_repositories') as mock_fetch, \
         patch('main.process_repositories') as mock_process, \
         patch('main.save_repositories') as mock_save, \
         patch('main.save_repositories_to_db') as mock_database:

       repositories = [
        {
            'name': 'projeto-python',
            'full_name': 'usuario/projeto-python',
            'language': 'Python',
            'stars': 20,
            'forks': 30
        }
    ]

       mock_fetch.return_value = {'items': []}
       mock_process.return_value = repositories
       mock_database.return_value = True

       main()

       mock_logging.assert_called_once()
       mock_fetch.assert_called_once()
       mock_process.assert_called_once_with({'items':   []})
       mock_save.assert_called_once_with(repositories)
       mock_database.assert_called_once_with(repositories)

def test_main_fetch_failure():

    with patch('main.setup_logging') as mock_logging, \
             patch('main.fetch_repositories') as mock_fetch, \
             patch('main.process_repositories') as mock_process, \
             patch('main.save_repositories') as mock_save, \
             patch('main.save_repositories_to_db') as mock_database:

        mock_fetch.return_value = None

        main()

        mock_logging.assert_called_once()
        mock_fetch.assert_called_once()
        mock_process.assert_not_called()
        mock_save.assert_not_called()
        mock_database.assert_not_called()

def test_main_no_valid_repositories():

    with patch('main.setup_logging') as mock_logging, \
                patch('main.fetch_repositories') as mock_fetch, \
                patch('main.process_repositories') as mock_process, \
                patch('main.save_repositories') as mock_save, \
                patch('main.save_repositories_to_db') as mock_database:

        mock_fetch.return_value = {'items': []}
        mock_process.return_value = []

        main()

        mock_logging.assert_called_once()
        mock_fetch.assert_called_once()
        mock_process.assert_called_once_with({'items': []})
        mock_save.assert_not_called()
        mock_database.assert_not_called()

def test_main_database_failure():

        with patch('main.setup_logging') as mock_logging, \
                patch('main.fetch_repositories') as mock_fetch, \
                patch('main.process_repositories') as mock_process, \
                patch('main.save_repositories') as mock_save, \
                patch('main.save_repositories_to_db') as mock_database, \
                patch('main.logging.error') as mock_error:

            repositories = [
            {
                'name': 'projeto-python',
                'full_name': 'usuario/projeto-python',
                'language': 'Python',
                'stars': 20,
                'forks': 30
            }
        ]   

            mock_fetch.return_value = {'items':[]}
            mock_process.return_value = repositories
            mock_database.return_value = False

            main()

            mock_logging.assert_called_once()
            mock_fetch.assert_called_once()
            mock_process.assert_called_once_with({'items': []})
            mock_save.assert_called_once_with(repositories)
            mock_database.assert_called_once_with(repositories)
            mock_error.assert_called_once_with(
                'Pipeline failed during database saving.'
            )
