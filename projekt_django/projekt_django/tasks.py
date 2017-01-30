import time
from functools import wraps

import requests
from bs4 import BeautifulSoup

from .models import Frase, Url
from projekt_django.celeryconf import app  


def update_job(fn):  

    @wraps(fn)
    def wrapper(job_id, *args, **kwargs):
        job = Frase.objects.get(id=job_id)
        job.status = 'started'
        job.save()
        try:
            results = fn(*args, **kwargs)
            for result in results:
                url = Url.objects.create(frase_key=job, url=result)
                url.save()
            if job.status != 'failed':
                job.status = 'finished'
            job.save()
        except Exception as e:
            job.status = 'failed'
            job.save()
    return wrapper

@app.task
@update_job
def crawler(frase, pages):  
    url = 'https://www.google.com/search'
    result = []
    query = {'q': frase}

    for start in pages:
        query['start'] = start
        page = requests.get(url, params=query)
        soup = BeautifulSoup(page.content)
        links = soup.select("h3.r a")

        for link in links:
            result.append(link['href'].replace('/url?q=', '').split('&sa=')[0])
        
        time.sleep(1)

    return result