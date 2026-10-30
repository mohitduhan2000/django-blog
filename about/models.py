from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200, default="About MyBlog")
    description = models.TextField()

    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title