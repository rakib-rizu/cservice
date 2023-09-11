from django.contrib import admin
from .models import Service, Testimonial, Profile, Contact

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    list_filter = ('title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    list_filter = ('title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'address', 'information', 'facebook', 'twitter', 'linkedin', 'instagram', 'created_at', 'updated_at')
    list_filter = ('email', 'phone', 'address', 'information', 'facebook', 'twitter', 'linkedin', 'instagram', 'created_at', 'updated_at')
    search_fields = ('email', 'phone', 'address', 'information', 'facebook', 'twitter', 'linkedin', 'instagram', 'created_at', 'updated_at')
    ordering = ('-created_at',)

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'service', 'book_date', 'message', 'created_at', 'updated_at')
    list_filter = ('name', 'phone', 'email', 'service', 'book_date', 'message', 'created_at', 'updated_at')
    search_fields = ('name', 'phone', 'email', 'service', 'book_date', 'message', 'created_at', 'updated_at')
    ordering = ('-created_at',)

    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
