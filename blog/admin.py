from django.contrib import admin
# Register your models here.
from blog.models import post, blogComment, Category



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display        = ['name', 'slug'] # For Display fields
    prepopulated_fields = {'slug': ('name',)} # Slug e auto name bosbe
    search_fields       = ('name', 'slug') # For search fields


@admin.register(post)
class Post(admin.ModelAdmin):
    list_display 		= ['category', 'author', 'views', 'title', 'short_description', 'timestamp'] # For Display fields
    prepopulated_fields = {'slug': ('title',)} # Slug e auto bosbe
    search_fields       = ('category__name', 'author', 'title', 'content') # For search fields and FOREIGN KEY search_fields = ['foreinkeyfield__foreinkeyfield name']
    list_per_page 		= 20  #for pagination 

    class Media: # for tinyMCE
        js= ('tinyInject.js',)



@admin.register(blogComment)
class PostComment(admin.ModelAdmin):
    list_display  = ['short_comment', 'user', 'sno', 'parent', 'timestamp']
    search_fields = ('user__username', 'comment') # search for any FOREIGN KEY search_fields = ['foreinkeyfield__foreinkeyfield name']
    list_per_page = 20  #for pagination 

