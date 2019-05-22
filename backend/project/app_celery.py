import random

import requests
from celery import Celery

from google.cloud import storage

# If you don't specify credentials when constructing the client, the
# client library will look for credentials in the environment.

app = Celery('app_celery', broker='redis://10.0.0.4:6379/mymemorystore')


@app.task
def fetch_url(url):
    resp = requests.get(url)
    print(resp.status_code)


def get_response(url):
    fetch_url.delay(url)


if __name__ == "__main__":
    test_list = ["http://google.com", "https://amazon.in", "https://facebook.com", "https://twitter.com", "https://alexa.com"]
    for _ in range(10000):
        random_website = random.choice(test_list)
        get_response(random_website)
