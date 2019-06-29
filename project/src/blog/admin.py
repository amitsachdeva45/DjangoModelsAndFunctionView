from django.contrib import admin

# Register your models here.
from .models import PostModel


class PostModelAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
        'action',
        'content',
        'publish',
        'view_count',
        'publish_date',
        'updated',
        'timestamp',
        'new_content',
        'get_age',
        'ftn_property'
    ]
    readonly_fields = ['updated','timestamp','new_content','get_age','ftn_property']

    def new_content(self, obj, *args, **kwargs):
        return str(obj.title)

    def get_age(self, obj, *args, **kwargs):
        return str(obj.age())

    def ftn_property(self, obj, *args, **kwargs):
        return str(obj.ftn_property())


    class Meta:
        model = PostModel
admin.site.register(PostModel, PostModelAdmin)