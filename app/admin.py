from django.contrib import admin

# Register your models here.
from .models import Account, Post, Comment


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    fields = ('id', 'username', 'email', 'gender', 'first_name', 'last_name')
    list_display = ('id', 'username', 'email', 'gender', 'first_name', 'last_name')
    readonly_fields = ('id',)
    search_fields = ('username', 'email')
    list_per_page = 20


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('user', 'title', 'content')
    list_display = ('user', 'title', 'content')
    readonly_fields = ('id',)
    search_fields = ('user', 'title')
    list_per_page = 20


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('user', 'post', 'content')
    list_display = ('user', 'post', 'content')
    readonly_fields = ('id',)
    search_fields = ('user', 'post')
    list_per_page = 20
