from django.contrib import admin
from blog.models import Category, Comment, Post

# Register your models here.

# Category Admin (make sure to add 'created_at' if needed in the Category model)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Displaying only 'name' here as no 'user' or 'created_at' exists.
    list_filter = ('name',)

# Post Admin (customize as needed)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_on', 'likes', 'user')  # Customize what to display in the list
    list_filter = ('created_on', 'category')  # Filter by 'created_on' and 'category'
    search_fields = ('title', 'content')  # Add search functionality by 'title' and 'content'

# Comment Admin (customize as needed)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_on', 'user')  # Show 'author', 'post', and 'created_on'
    list_filter = ('created_on', 'post')  # Filter by 'created_on' and 'post'
    search_fields = ('author', 'body')  # Allow searching by 'author' and 'body'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
