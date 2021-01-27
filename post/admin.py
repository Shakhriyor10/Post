from django.contrib import admin

# Register your models here.
from post.models import *


@admin.register(Author)
class Author(admin.ModelAdmin):
    pass


@admin.register(Post)
class Post(admin.ModelAdmin):
    pass


@admin.register(Book)
class Book(admin.ModelAdmin):
    pass


admin.site.site_header = 'DSSCHOOL'
