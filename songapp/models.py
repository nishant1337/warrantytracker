from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bills(models.Model):  
    song_id=models.AutoField(primary_key=True)
    productname=models.CharField(max_length=100)
    producttype=models.CharField(max_length=50)
    purchasedate = models.DateField()
    expirydate = models.DateField()
    bill=models.ImageField(upload_to='images')
    logo=models.ImageField(upload_to='images',default='"/media/images/s.png')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.productname