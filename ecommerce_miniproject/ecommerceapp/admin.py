from django.contrib import admin

from ecommerceapp.models import Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
            list_display = ['name','slug']
            prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
            list_display = ['name','slug','price','stock','available','created_date','updated_date']
            list_editable = ['price','stock','available']
            prepopulated_fields = {'slug':('name',)}
            list_per_page = 20
admin.site.register(Product,ProductAdmin)