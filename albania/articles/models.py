from django.db import models


class Article(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	pic = models.ImageField(upload_to='images/', default='IMG')
	date = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	#author = models.ForeignKey(
     #       get_user_model(),
      #      on_delete=models.CASCADE,
       # )


class Comment(models.Model):  # new
	article = models.ForeignKey(
		Article, on_delete=models.CASCADE, related_name='comments',)
	comment = models.CharField(max_length=140)
	author = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)

	def __str__(self):
		return self.comment

	@staticmethod
	def get_absolute_url():
		return reverse('article_list')
