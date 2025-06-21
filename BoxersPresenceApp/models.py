from django.db import models

class Boxer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    boxer = models.ForeignKey(Boxer, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)
    is_excused = models.BooleanField(default=False)

    def __str__(self):
        status = 'Present' if self.is_present else 'Absent (Excused)' if self.is_excused else 'Absent'
        return f"{self.boxer.name} - {self.date} - {status}"
