import secrets

from django.db import models

# Create your models here.
from django.utils import timezone as tz


class Model(models.Model):
    id_prefix = None
    id = models.CharField(primary_key=True, max_length=128)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = tz.now()
            if self.id_prefix:
                self.id = f'{self.id_prefix}_{secrets.token_hex(16)}'
            else:
                self.id = secrets.token_hex(16)
        self.updated_at = tz.now()
        super(Model, self).save(*args, **kwargs)

    class Meta:
        managed = False
