from django.db import models
from django.utils import timezone


# Create your models here.
class Foo(models.Model):
    is_private = models.BooleanField(default=False)


class drug(models.Model):
    drug_name = models.CharField(max_length=100, unique=True)
    drug_form = models.TextField()
    drug_class = models.TextField()
    drug_indication = models.TextField()
    drug_contraindication = models.TextField()
    drug_careful = models.TextField()
    drug_side_effect = models.TextField()
    drug_dosage = models.TextField()
    drug_attention = models.TextField()
    drug_reference = models.TextField()
    drug_status = models.BooleanField()
    drug_update_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.drug_name
