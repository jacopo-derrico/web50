from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    watchlist = models.ManyToManyField('Auctions', related_name="watch_auction", blank=True)

# auctions model
class Auctions(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.TextField()
    starting_bid = models.IntegerField()
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)

class Bids(models.Model):
    bid = models.IntegerField()
    users = models.ManyToManyField(User, related_name="bid_user")
    auctions = models.ManyToManyField(Auctions, related_name="bid_auction")

class Comments(models.Model):
    comment = models.CharField(max_length=250)
    users = models.ManyToManyField(User, related_name="comment_user")
    auctions = models.ForeignKey(Auctions, on_delete=models.CASCADE)

class Categories(models.Model):
    title = models.CharField(max_length=30)