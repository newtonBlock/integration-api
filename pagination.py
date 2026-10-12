import json
import requests
from urllib.parse import urlparse, parse_qs

state_info = {'limit': 60,
              'offset': 0,}

baseurl = "https://pokeapi.co/api/v2/"
endpoint = "evolution-chain"

def get_pagination_state(state_info):
    try:
        return state_info['limit'], state_info['offset']
    except Exception:
        return 20,0
        
def save_pagination_state(state_info, limit, offset):
    try:
        state_info['limit'] = limit
        state_info['offset'] = offset
        return True
    except Exception as e:
        raise Exception(f'Failed to save pagination state: {e}')

def delete_pagination_state(state_info):
    try:
        state_info['limit'] = 20
        state_info['offset'] = 0
    except Exception as e:
        raise Exception(f'Failed to restart pagination: {e}')

def main_request(baseurl, endpoint, state_info):
    
    """
    Handle the loop to fetch paginated Pokemon data.
    Args:

    Returns:
        Response: JSON response with Pokemon results and pagination state
    
    """
    while True:

        limit, offset = get_pagination_state(state_info)    
        try:
            response = requests.get(baseurl + endpoint + f'?offset={offset}&limit={limit}')
            rdata = response.json()
            parse_json(rdata)
            next_link = rdata['next']
            # check for next page
            if next_link:
                # parse next URL to get pagination params
                parsed_url = urlparse(next_link)
                query_params = parse_qs(parsed_url.query)
                query_params = {
                    k:v[0]
                    for k,v in query_params.items()
                }
                save_pagination_state(state_info, int(query_params['limit']), int(query_params['offset']))
                print(f'offset: {int(query_params['limit'])}')
            else:
                break            
            # print(response.json())
        except Exception as e:
            raise Exception(f'Failed to make request: {e}' + f'Process stops at offset {offset}')


def parse_json(response):
    # get the all dicts of resouces
    charlist = []
    for item in response['results']:
        char = {
           'name': item.get('name', 'unknown'), 
           'url': item.get('url', 'no url')
        } 
        #print(char)
        #charlist.append(char)
    print(len(response['results']))
    return charlist

main_request(baseurl, endpoint, state_info)

