from django.contrib import admin
from vidyo.models import ExtractAudio, Watermark

# Register your models here.
@admin.register(ExtractAudio)
class ExtractAudioAdmin(admin.ModelAdmin):
    list_display = ['username','input','output','timestamp']

@admin.register(Watermark)
class WatermarkAdmin(admin.ModelAdmin):
    list_display = ['username','video','image','output','size','position','timestamp']