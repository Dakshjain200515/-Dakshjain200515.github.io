from django.db import models

class Entry(models.Model):
    party_name = models.CharField(max_length=100)
    weight = models.FloatField()
    rate = models.FloatField()
    purity = models.FloatField()
    amount = models.FloatField()
    gst = models.FloatField()
    tds = models.FloatField()
    final_amount = models.FloatField()
