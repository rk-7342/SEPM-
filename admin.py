from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, StudentMarks, EntrepreneurProfile

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'phone', 'dob', 'category', 'education_level']  # Display these fields

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone', 'dob', 'category', 'education_level')}),  # Added fields
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('phone', 'dob', 'category', 'education_level')}),  # Added fields
    )

# Register User model with custom admin
admin.site.register(User, CustomUserAdmin)

# StudentMarks Admin
@admin.register(StudentMarks)
class StudentMarksAdmin(admin.ModelAdmin):
    list_display = ('user', 'education_level')  # Display these fields in the admin panel

# EntrepreneurProfile Admin
admin.site.register(EntrepreneurProfile)

from .models import CareerChangerProfile

@admin.register(CareerChangerProfile)
class CareerChangerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'twelfth_marks', 'btech_degree_marks', 'previous_skills', 'career_preference')  # ✅ Display fields in the admin panel
    search_fields = ('user__username', 'career_preference')  # ✅ Add search functionality
    list_filter = ('career_preference',)  # ✅ Add filter by career interest


