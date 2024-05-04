import requests

from dotenv import dotenv_values


QUOTE_TOKEN = dotenv_values('.env').get('QUOTE_TOKEN')

def get_my_quote(category):
    category = 'inspirational'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': QUOTE_TOKEN})
    if response.status_code != requests.codes.ok:
        return None, None, '"Error:", response.status_code, response.text'
    else:
        return response.json()[0].get('quote'), response.json()[0].get('author'), None