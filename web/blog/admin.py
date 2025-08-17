from django.contrib import admin
from blog.models import Category, Comment, Post

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on', 'last_modified']
    list_filter = ['created_on', 'categories']
    search_fields = ['title', 'body']

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
