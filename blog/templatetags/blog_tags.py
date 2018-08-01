from django import template
from ..models import Post, Category, Tag
from django.db.models.aggregates import Count
from blog.models import Category

# 这里我们首先导入 template 这个模块，然后实例化了一个 template.Library 类，并将函数 get_recent_posts
# 装饰为 register.simple_tag。这样就可以在模板中使用语法 {% get_recent_posts %} 调用这个函数了。
register = template.Library()


# 统计分类文章数这个 Category.objects.annotate 方法和 Category.objects.all 有点类似
# ，它会返回数据库中全部 Category 的记录，但同时它还会做一些额外的事情，
# 在这里我们希望它做的额外事情就是去统计返回的 Category 记录的集合中每条记录下的
# 文章数。代码中的 Count 方法为我们做了这个事，它接收一个和 Categoty 相关联的
# 模型参数名（这里是 Post，通过 ForeignKey 关联的），然后它便会统计 Category 记录的
# 集合中每条记录下的与之关联的 Post 记录的行数，也就是文章数，最后把这个值保存到
#  num_posts 属性中。
@register.simple_tag
def get_categories():
    # 记得引入count函数
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型名称
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts_gt=0)


# 最新文章模板标签
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


# 归档模板标签
@register.simple_tag
def archives():
    # created_time-创建时间 month-精确到月份 order='DESC'-降序排列（即离当前越近的时间越排在前面）
    return Post.objects.dates('created_time', 'month', order='DESC')


# 分类模板标签
@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()


# 云标签
@register.simple_tag
def get_tags():
    # 记得在顶部引入Tag model
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
