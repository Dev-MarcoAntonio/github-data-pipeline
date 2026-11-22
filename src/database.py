import psycopg
import os
import logging

def connect_database():

    try:
        connection = psycopg.connect(
            host = os.getenv('DB_HOST'),
            port = os.getenv('DB_PORT'),
            dbname = os.getenv('DB_NAME'),
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD')
        )

        logging.info('Database connected successfully.')

    except psycopg.Error as error:
        logging.error(f'Failure: {error}')
        return None

    return connection

def save_repositories_to_db(repositories):

    connection = connect_database()
    cursor = None

    if connection is not None:
        try:

            cursor = connection.cursor()

            for repository in repositories:
                cursor.execute(
                    """
                    INSERT INTO repositories (name,full_name,language,stars,forks)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (full_name) DO NOTHING;
                    """,
                    (
                        repository['name'],
                        repository['full_name'],
                        repository['language'],
                        repository['stars'],
                        repository['forks']
                    )
                )

            connection.commit()

            logging.info('Repositories saved successfully.')

        except psycopg.Error as error:

            logging.error(f'Failed to save repositories: {error}')
            connection.rollback()

        finally:
            if cursor is not None:
                cursor.close()
            connection.close()