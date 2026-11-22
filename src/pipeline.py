import requests
import json
from pathlib import Path
import logging

def fetch_repositories():
    try:

        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc&per_page=30'

        logging.info('Requesting repositories from GitHub API.')

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        logging.info('Repositories successfully fetched.')

        return data
    
    except requests.exceptions.RequestException as erro:
        logging.error(f'Failure: {erro}')

def process_repositories(data):

    processed_repositories = []

    repositories = data.get('items',[])

    logging.info(f'Processing {len(repositories)} repositories.')

    for repository in repositories:

        name = repository.get('name')
        full_name = repository.get('full_name')
        language = repository.get('language')
        stars = repository.get('stargazers_count')
        forks = repository.get('forks_count')

        if not isinstance(name,str) or name.strip() == '':
            continue

        if not isinstance(full_name,str) or full_name.strip() == '':
            continue

        if type(stars) is not int or stars < 0:
            continue

        if type(forks) is not int or forks < 0:
            continue

        processed_repository = {
            'name': name, 
            'full_name': full_name,
            'language': language,
            'stars': stars,
            'forks': forks
        }
        processed_repositories.append(processed_repository)

    return processed_repositories

def save_repositories(processed_data):

    caminho = Path('data/processed')
    caminho.mkdir(parents=True,exist_ok=True)

    with open('data/processed/repositories.json','w',encoding='utf-8') as arquivo:
        json.dump(processed_data,arquivo,indent = 4,ensure_ascii=False)

    logging.info(f'{len(processed_data)} repositories saved successfully.')