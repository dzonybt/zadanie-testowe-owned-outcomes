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
            for start_page in xrange(0, 10 * self.pages, 10):
                crawler.delay(job_id=self.id, frase=self.frase, start_page=start_page)


class Url(models.Model):
    url = models.TextField()
    frase_key = models.ForeignKey(Frase, on_delete=models.CASCADE)