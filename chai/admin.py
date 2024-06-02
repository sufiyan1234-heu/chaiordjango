from django.contrib import admin
from .models import ChaiVarity,ChaiCertificate,ChaiReview,Store

# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2
    
class ChaiCVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type','date_added')
    inlines = [ChaiReviewInline]
    
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)
    
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')
    
    
    

admin.site.register(ChaiVarity,ChaiCVarityAdmin,
                    )
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)
admin.site.register(Store,StoreAdmin)


