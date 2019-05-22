import requests
from celery import Celery

from google.cloud import storage

# If you don't specify credentials when constructing the client, the
# client library will look for credentials in the environment.

app = Celery('app_celery', broker='redis://10.0.0.4:6379/0')


@app.task
def fetch_url(url):
    resp = requests.get(url)
    print(resp.status_code)


def func(urls):
    for url in urls:
        fetch_url.delay(url)


if __name__ == "__main__":
    func(["http://google.com", "https://amazon.in", "https://facebook.com", "https://twitter.com", "https://alexa.com"])
