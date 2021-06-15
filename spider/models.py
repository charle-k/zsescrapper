from django.db import models

# Create your models here.


class ZSEData(models.Model):
    data = models.TextField(null=True)
    trading_date = models.DateField(null=True,)
    created = models.DateTimeField(auto_now_add=True)
    exported = models.DateTimeField(null=True)
    data_changed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "ZSEData"

    def __str__(self):
        t = str(self.trading_date) + ' - ' + str(self.id)
        return t
