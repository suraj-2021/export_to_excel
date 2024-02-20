from django.db import models

class Product(models.Model):
      name = models.CharField(max_length=20)
      price = models.IntegerField()
      quantity = models.CharField(max_length = 20)

      class Meta:
            verbose_name_plural = 'Products'
    
      def __str__(self):
            return self.name
        