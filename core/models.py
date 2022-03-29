from django.conf import settings
from django.db import models
from django.utils.timezone import now


# Modelo común entre todos los modelos
class CommonInfo(models.Model):
    # Cuándo ha sido creado
    created_at = models.DateTimeField("Created at", default=now, blank=True)
    last_modified_at = models.DateTimeField("Last modified at", default=now, blank=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = now()

        self.last_modified_at = now()
        super(CommonInfo, self).save(*args, **kwargs)

    class Meta:
        # Clase abstracta
        abstract = True