from django.contrib import admin
from .models import (
    Category, 
    Region,
    Item,
    Form,
    Appeal
)

admin.site.register(Category)
admin.site.register(Region)
admin.site.register(Item)
admin.site.register(Form)
admin.site.register(Appeal)