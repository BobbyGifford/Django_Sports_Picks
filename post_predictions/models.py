from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Pick(models.Model):
    """
    Creates a Pick model which has a selection of categories,
    a User as a foreign key, a prediction.
    """

    CATEGORIES = (
        ('NFL', 'NFL'),
        ('NCAAF', 'NCAAF'),
        ('MLB', 'MLB'),
        ('UFC', 'UFC')
    )

    user = models.ForeignKey(User, related_name="picks")
    prediction = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20,
        choices=CATEGORIES,
        default='NFL'
        )

    def __str__(self):
        return self.prediction
