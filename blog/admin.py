from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'title', 'category', 'date_created', 'featured')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25
    summernote_fields = ('content', )

