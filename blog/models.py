from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse
from django.template.defaultfilters import truncatechars # For Admin truncatechars Show


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('blog:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class post(models.Model):
	sno 		= models.AutoField(primary_key= True)
	category   	= models.ForeignKey(Category, related_name='post', on_delete=models.CASCADE)
	created_by  = models.ForeignKey(User, related_name='post_creator', on_delete=models.CASCADE, default='admin')
	author 		= models.CharField(max_length=255, default='admin')
	postimage 	= models.ImageField(upload_to='image/', default='default/blog-1.jpg')
	title 		= models.CharField(max_length=255)
	slug        = models.CharField(max_length=255, unique=True)
	views 		= models.IntegerField(default=0) 	# For total view count
	content 	= models.TextField(max_length=10000, blank=False)
	timestamp 	= models.DateTimeField(auto_now_add=True, blank=True)

	# For Admin truncatechars view
	@property
	def short_description(self):
		return truncatechars(self.content, 100)

	def __str__(self):
		return self.title



class blogComment(models.Model):
	sno 		= models.AutoField(primary_key= True)
	comment 	= models.TextField()
	user 		= models.ForeignKey(User, on_delete=models.CASCADE)
	post 		= models.ForeignKey(post, on_delete=models.CASCADE)
	parent 		= models.ForeignKey('self', on_delete=models.CASCADE, null=True)
	timestamp 	= models.DateTimeField(default=now)

	# Admin truncatechars
	@property
	def short_comment(self):
		return truncatechars(self.comment, 80) # truncatechars limit
	
	def __str__(self):
		return self.comment