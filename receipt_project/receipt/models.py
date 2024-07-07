from django.db import models
from django.contrib.auth.models import User


class Receipt(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField()
    total=models.DecimalField(max_digits=10,decimal_places=2)

    def save(self,*args,**kwargs):
        self.total=self.price*self.quantity
        super().save(*args,**kwargs)
