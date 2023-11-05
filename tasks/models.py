from django.db import models


class Type_task (models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Otdels(models.Model):
    name = models.CharField(max_length=300)
    kod = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tasks (models.Model):
    sana = models.DateField()
    javobgar = models.CharField(max_length=100)
    topshiriq_turi = models.ForeignKey(Type_task, on_delete=models.CASCADE)
    topshiriq_nomer = models.CharField(max_length=100)
    topshiriq_sana = models.DateField()
    topshiriq_otdel = models.ForeignKey(Otdels, on_delete=models.CASCADE)
    topshiriq_mavzu = models.CharField(max_length=100)
    topshirq_muddat = models.DateField()

    def __str__(self):
        return self.topshiriq_nomer
