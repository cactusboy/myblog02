from django.contrib import admin
from .models import Post, Category, Tag
from .models import MediaTest


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


# 图片上传类
class MangeMedia(admin.ModelAdmin):
    fields = ['picture_url', 'name_meida']
    

# 把新增的PostAdmin也注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(MediaTest, MangeMedia)  # 图片上传类
