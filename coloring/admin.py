from django.contrib import admin
from coloring.models import Author
from coloring.models import Drawing

# Register your models here.
# https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#modeladmin-objects

admin.site.register(Author)
admin.site.register(Drawing)

