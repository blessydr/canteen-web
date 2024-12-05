from django.db import models

class Category(models.Model):
    CANDIES_JARS = 'CJ'
    POTATO_CHIPS = 'PC'
    CAKE = 'CA'
    BISCUIT = 'BI'
    JUICE = 'JU'
    CHOCOLATE = 'CH'

    CATEGORY_CHOICES = [
        (CANDIES_JARS, 'Candies Jars'),
        (POTATO_CHIPS, 'Potato Chips'),
        (CAKE, 'Cake'),
        (BISCUIT, 'Biscuit'),
        (JUICE, 'Juice'),
        (CHOCOLATE, 'Chocolate'),
    ]

    name = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=CAKE,
    )

    def __str__(self):
        return dict(self.CATEGORY_CHOICES).get(self.name, 'Unknown')
    
    
class Snack(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='snacks/', default='snacks/default.jpg')
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
