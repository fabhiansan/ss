from django.db import models

Month = (
    ('Januari', 'Januari'),
    ('Februari', 'Februari')
)
Years = (
    ('2018', '2018'),
    ('2019', '2019')
)

Segmen = (
    ('75', '75'),
    ('75.5', 'KM75.5')
)




class RCI(models.Model):
    years = models.CharField(max_length=10, choices=Years, default='2018')
    month = models.CharField(max_length=10, choices=Month, default='Januari')
    segmen = models.CharField(max_length=10, choices=Segmen)
    parameter1 = models.IntegerField()
    parameter2 = models.IntegerField()
    parameter3 = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return "KM {0} Bulan {1} Tahun {2}".format(self.segmen, self.years, self.month)

    def totalrci(self):
        roadindex = (self.parameter1 + self.parameter2 + self.parameter3)/3
        return roadindex


class Reklamasi(models.Model):
    nama = models.CharField(max_length=10)
    parameter1 = models.IntegerField()
    parameter2 = models.IntegerField()
    parameter3 = models.IntegerField()
    objects = models.Manager()
    
    def __str__(self):
        return self.nama

    