from src.pipeline import fetch_repositories, process_repositories, save_repositories
from src.logging_config import setup_logging
from src.database import save_repositories_to_db
import logging

def main():

    setup_logging()

    data = fetch_repositories()

    if data is not None:
        processed_data = process_repositories(data)

        if processed_data:
            save_repositories(processed_data)
            success = save_repositories_to_db(processed_data)

            if success:
                logging.info('Pipeline executed successfully.')

            else:
                logging.error('Pipeline failed during database saving.')

        else:
            logging.warning('No valid repository found.')

if __name__ == '__main__':
    main()