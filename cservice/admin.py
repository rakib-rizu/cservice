from django.contrib import admin
from .models import Service, Testimonial, Profile, Contact
from .forms import ContactAdminForm

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    list_filter = ('title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'created_at', 'updated_at')
    ordering = ('-created_at',)
Service._meta.verbose_name_plural = "Services"

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    list_filter = ('title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'created_at', 'updated_at')
    ordering = ('-created_at',)
Testimonial._meta.verbose_name_plural = "Testimonials"

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
Profile._meta.verbose_name_plural = "Profile"
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'service', 'book_date', 'message', 'assigned_staff', 'status', 'created_at', 'updated_at')
    list_filter = ('name', 'phone', 'email', 'service', 'book_date', 'message', 'assigned_staff', 'status', 'created_at', 'updated_at')
    search_fields = ('name', 'phone', 'email', 'service', 'book_date', 'message', 'assigned_staff', 'status', 'created_at', 'updated_at')
    ordering = ('-created_at',)

    readonly_fields = ('name', 'phone', 'email', 'service', 'book_date', 'message', 'created_at', 'updated_at')
    form = ContactAdminForm

    def get_queryset(self, request):
        # Filter the queryset based on assigned_staff
        qs = super(ContactAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            # If the user is not a superuser, filter contacts by assigned_staff
            qs = qs.filter(assigned_staff=request.user)
        return qs

    def get_form(self, request, obj=None, **kwargs):
        # Restrict assigning staff only to admin users
        form = super(ContactAdmin, self).get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            form.base_fields['assigned_staff'].widget.attrs['disabled'] = True
        return form

    def has_add_permission(self, request):
        return False
    # def has_change_permission(self, request, obj=None):
    #     return False
    def has_delete_permission(self, request, obj=None):
        return False
Contact._meta.verbose_name_plural = "Appointments"