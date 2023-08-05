from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
class CarMake(models.Model):
    Name=models.CharField(max_length=50)
    Description=models.CharField(max_length=80)
    def __str__(self):
        return self.name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    SEDAN='Sedan'
    SUV='Suv'
    WAGON='Wagon'
    CAR_TYPE_CHOICES=[(SEDAN,'Sedan'),(SUV,'Suv'),(WAGON,'Wagon')]
    make=models.ForeignKey(CarMake, on_delete=models.CASCADE)
    Name=models.CharField(max_length=60)
    type=models.CharField(max_length=50,choices=CAR_TYPE_CHOICES)
    Dealer_id=models.PositiveIntegerField()
    year=models.DateField()
    def __str__(self):
        return f"{self.Name}{self.type}"


# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
