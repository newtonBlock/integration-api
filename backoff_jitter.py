import random
import hubspot
import os
import time

from http import HTTPStatus
from dotenv import load_dotenv
from pprint import pprint
from hubspot.crm.contacts.exceptions import ApiException

maxRetries = 5,
baseDelay = 1000,
maxDelay = 30000
jitterMax = 500,


def sleep_calc():
    pass

# Calculate delay: use Retry-After if present, otherwise use exponential backoff with jitter

#Exponential backoff: increase the delay exponentially with each retry attempt, up to a maximum delay
def exponential_backoff(attempt, base_delay, max_delay):
    return min(base_delay * (2 ** attempt), max_delay)

#Jitter: add a random amount of time to the delay to avoid thundering herd problem
def jitter_delay(jitter_max):
    return random.uniform(0, jitter_max)

def get_access_token():
    load_dotenv()
    return os.environ['ACCESS_TOKEN']


def get_cached():
    pass

def withRateLimit(maxRetries, base_delay, max_delay, jitter_max):
    apiClient = hubspot.Client.create(access_token=get_access_token())

    for i in range(maxRetries):
        # try:
        #     apiClient.crm.objects.basic_api.get_page(object_type="contacts")
        # except ApiException as e:
        #     if e.status == HTTPStatus.TOO_MANY_REQUESTS:
        #         e.headers.get['Retry-After', ]
        try: 
            response = apiClient.api_request(
                {"path": "/crm/v3/objects/contacts", "method": "GET"}
            )
            pprint(response.json())
        except ApiException as e:
            if e.status == HTTPStatus.TOO_MANY_REQUESTS:
                if i == maxRetries - 1:
                    raise e
                retry_after = e.headers.get['Retry-After', 0]
                delay = retry_after + jitter_delay(jitter_max) if retry_after > 0 else exponential_backoff(i, base_delay, max_delay) + jitter_delay(jitter_max)
                # the other calculation for exponential backoff with jitter
                #delay = random.uniform(0, min(max_delay, base_delay * (2 ** i)))
                time.sleep(delay / 1000)