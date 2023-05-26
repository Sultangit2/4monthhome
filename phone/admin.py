from django.contrib import admin
from phone.models import Product, Comment


# Register your models here.
# #
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'rate', 'created_date', 'modified_date')
#
#    # sortable_by = ('rate',)


admin.site.register(Product)
admin.site.register(Comment)
