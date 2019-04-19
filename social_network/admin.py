from django.contrib.admin import AdminSite, ModelAdmin, StackedInline, TabularInline
from django.utils.safestring import mark_safe

from .models import *

class KosherConnectionsAdminSite(AdminSite):
    site_header = 'Kosher Connections'

admin_site = KosherConnectionsAdminSite(name='kosher_connections_admin')

# class UserAdmin(ModelAdmin):
#     list_display = ('id', 'full_name', 'status')
#     list_filter = ('first_name', 'last_name', 'email')
#     inlines = (PersonalInfoAdmin, )

class PersonalInfoInline(StackedInline):
    model = PersonalInfo
    readonly_fields = ('headshot_image',)
    list_display = ('user', 'birthdate', 'marital_status')
    date_hierarchy = 'birthdate'
    list_select_related = ('user',)

    def headshot_image(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.headshot.url,
                width=100,
                height=100,
            )
        )

class AddressInline(TabularInline):
    model = Address
    extra = 0

class PhoneInline(TabularInline):
    model = Phone
    extra = 0

class FamilyInline(TabularInline):
    model = Family
    extra = 0

class PersonalQualityInline(TabularInline):
    model = PersonalQuality
    extra = 0
    fields = ('quality',)
    list_select_related = ('quality',)

class SeekingQualityInline(TabularInline):
    model = SeekingQuality
    extra = 0
    fields = ('quality',)
    list_select_related = ('quality',)

class UserAdmin(ModelAdmin):
    list_display = ('id', 'full_name', 'status')
    list_filter = ('first_name', 'last_name', 'email')
    inlines = (PersonalInfoInline, FamilyInline, AddressInline, PhoneInline, PersonalQualityInline, SeekingQualityInline)


admin_site.register(User, UserAdmin)
# admin_site.register(PersonalInfo, PersonalInfoAdmin)
# admin_site.register(Address)
# admin_site.register(Phone)
admin_site.register(Quality)
# admin_site.register(PersonalQuality)
# admin_site.register(SeekingQuality)
admin_site.register(Endorsement)
admin_site.register(Recommendation)
admin_site.register(Relationship)
# admin_site.register(Family)
admin_site.register(School)
