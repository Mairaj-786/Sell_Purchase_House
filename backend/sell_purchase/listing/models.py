from django.db import models
from django.utils.timezone import now
from realtor.models import Realtor


class Listing(models.Model):
    class SalesType(models.TextChoices):
        For_Sale = "For Sale"
        For_Rent = "For Rent"

    class HouseType(models.TextChoices):
        House = "House"
        Condo = "Condo"
        Townhouse = "Townhouse"

    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=15)
    desc = models.TextField(blank=True)
    sale_type = models.CharField(
        max_length=30, choices=SalesType.choices, default=SalesType.For_Sale)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    home_type = models.CharField(
        max_length=30, choices=HouseType.choices, default=HouseType.House)
    sqft = models.IntegerField()
    open_house = models.BooleanField(default=False)
    main_photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_10 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.TimeField(default=now, blank=True)

    def __str__(self):
        return self.title
