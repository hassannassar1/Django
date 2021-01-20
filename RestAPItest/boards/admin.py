from django.contrib import admin
from .models import Board, Topic, Post
# Register your models here.

admin.site.site_header = 'Board Admin Panel'
admin.site.site_title = 'Board Admin Panel'

class InlineTopic(admin.StackedInline):
    model = Topic
    extra = 1
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    inlines = [InlineTopic]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    fields = ('subject','board',)
    list_display = ('subject','board','created_by')
    list_display_links = ('board','created_by')
    list_editable = ('subject',)
    list_filter = ('subject','board','created_by')
    search_fields = ('board',)

admin.site.register(Post)