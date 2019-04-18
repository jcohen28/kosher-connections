from django.contrib.admin import AdminSite

from .models import *

class KosherConnectionsAdminSite(AdminSite):
    site_header = 'Kosher Connections'

admin_site = KosherConnectionsAdminSite(name='kosher_connections_admin')

admin_site.register(User)
admin_site.register(PersonalInfo)
admin_site.register(Address)
admin_site.register(Phone)
admin_site.register(Quality)
admin_site.register(PersonalQuality)
admin_site.register(SeekingQuality)
admin_site.register(Endorsement)
admin_site.register(Recommendation)
admin_site.register(Relationship)
admin_site.register(Family)
admin_site.register(School)
