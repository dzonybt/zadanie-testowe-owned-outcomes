from django.db import models
from django.core.validators import MinValueValidator


class Frase(models.Model):  

    STATUSES = (
        ('pending', 'pending'),
        ('started', 'started'),
        ('finished', 'finished'),
        ('failed', 'failed'),
    )

    status = models.CharField(choices=STATUSES, max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    frase = models.TextField(blank=False)
    pages = models.IntegerField(null=True, validators=[MinValueValidator(1)])

    def save(self, *args, **kwargs):
        super(Frase, self).save(*args, **kwargs)
        if self.status == 'pending':
            from .tasks import crawler

            pages_to_crawl = []

            for i in xrange(0, 10 * self.pages, 10):
                pages_to_crawl.append(i)
                if len(pages_to_crawl) == 10:
                    self._create_task(crawler, pages_to_crawl)
                    del pages_to_crawl[:]

            self._create_task(crawler, pages_to_crawl)

    def _create_task(self, crawler, pages):
        crawler.apply(job_id=self.id, frase=self.frase, pages=pages)


class Url(models.Model):
    url = models.TextField()
    frase_key = models.ForeignKey(Frase, on_delete=models.CASCADE)