from django.contrib import admin

from goods.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)
# Register your models here.

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

#admin.site.register(Categories)
#admin.site.register(Products)