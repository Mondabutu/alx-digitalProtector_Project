from django.db import models

# Create digital record model here.
class DigitalRecord(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    digital_property = models.CharField(max_length=50)
    signature =  models.CharField(max_length=50)
    owner =  models.CharField(max_length=50)
    PropertyImage =  models.ImageField(upload_to='images')  

# Customise defaul records.
def __str__(self):
    return(f"{self.owner} {self.digital_property} {self.created_at}")