from django.contrib import admin
from .models import Entity

class EntityAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    fields = ['name', 'email','ico']


admin.site.register(Entity, EntityAdmin)