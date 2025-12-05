from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Auctions, Bids, Comments, Categories

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register([Auctions, Bids, Comments, Categories])