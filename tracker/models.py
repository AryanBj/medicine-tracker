from django.db import models

class MedicationRecord(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    dose = models.FloatField()

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M')} - {self.dose} mg"
