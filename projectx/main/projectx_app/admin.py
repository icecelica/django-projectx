from django.contrib import admin
from projectx_app.models import Blog, Description, AccessRecord
from projectx_app.models import UserProfileInfo

# Register your models here.
admin.site.register(Blog)
admin.site.register(Description)
admin.site.register(AccessRecord)
admin.site.register(UserProfileInfo)
