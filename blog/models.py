from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
import markdown
from django.utils.html import strip_tags


# python_2_unicode_compatible 装饰器用于兼容 Python2

# Create your models here.


@python_2_unicode_compatible  # python3不加这个装饰器不会受到影响
class Category(models.Model):  # 分类
    name = models.CharField('分类', max_length=100)

    # 使用__str__可以返回实际的数据而不是数据的数量
    def __str__(self):
        return self.name


class Tag(models.Model):  # 标签
    name = models.CharField('标签', max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):  # 文章表
    # 文章标题
    title = models.CharField('标题', max_length=70)
    # 文章正文
    body = models.TextField('正文')
    # 文章摘要,可以为空
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了
    excerpt = models.CharField('摘要', max_length=200, blank=True)

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个Markdown类，用于渲染body的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 现将Markdown文本渲染成html文本，strip_tags去掉html文本的全部html标签
            # 从文本摘取前54个字符赋给excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        # 调用父类的save方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

    # 文章创建时间
    created_time = models.DateTimeField()
    # 文章最后一次修改时间
    modified_time = models.DateTimeField()
    # 分类字段关联分类表，用外键一对多的关系
    # 当一个model对象的ForeignKey关联的对象被删除时，默认情况下此对象也会一起被级联删除的
    # ForeingKey外键必须加on_delete参数
    category = models.ForeignKey(Category, on_delete=True)
    #  标签字段关联标签表，用多对多的外键,并且可以为空
    tags = models.ManyToManyField(Tag, blank=True)
    # 文章作者，也就是用户，从django.contrib.auth.models导入
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、
    # 登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 一篇文章只有一个作者，所以用一对多外键关联django的内置User表
    author = models.ForeignKey(User, on_delete=True)
    # 记录阅读量，注意：views 字段的类型为 PositiveIntegerField，
    # 该类型的值只允许为正整数或 0，因为阅读量不可能为负值。初始化时 views 的值为 0。
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # increase_views 方法首先将自身对应的 views 字段的值 +1（此时数据库中的值还没变）
    # ，然后调用 save 方法将更改后的值保存到数据库。注意这里使用了
    # update_fields 参数来告诉 Django 只更新数据库中 views 字段的值，以提高效率。
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    # 列表中可以用多个项，比如 ordering = ['-created_time', 'title']
    # ，那么首先依据 created_time 排序，如果 created_time 相同，则再依据 title 排序。
    class Meta:
        ordering = ['-created_time']


# 图片上传类
class MediaTest(models.Model):
    picture_url = models.ImageField(
        null=True,
        blank=True,
        upload_to='image',
        max_length=200)
    # 新增字段必须添加default属性
    name_meida = models.CharField('图片名称', max_length=100, default="")
    # 图片表
    class Meta:
        db_table = 'media_test'
