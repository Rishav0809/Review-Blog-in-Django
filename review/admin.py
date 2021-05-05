from django.contrib import admin
from .models import Review,ExpertProfile,GenerateCode

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields=('date',)

admin.site.register(Review,ReviewAdmin)
admin.site.register(ExpertProfile)
admin.site.register(GenerateCode)
