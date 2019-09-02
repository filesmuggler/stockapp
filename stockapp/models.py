from django.db import models

# Create your models here.

class StockPart(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # TODO: limit to non-zero values
    quantity = models.IntegerField()
    barcode = models.IntegerField()
    # TODO: add possibility for adding photo

    def add_parts(self,number_of_parts):
        self.quantity = self.quantity + number_of_parts
        self.save()

    def remove_parts(self, number_of_parts):
        self.quantity = self.quantity - number_of_parts
        self.save()

    def get_barcode(self):
        return self.barcode

    def __str__(self):
        return self.name
