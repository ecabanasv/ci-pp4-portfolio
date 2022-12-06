"""
Models for the portfolio app
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


PUBLISH = ((0, "NO"), (1, "YES"))
RATE = ((0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"))
class Project(models.Model):
    """
    Model for the project
    """
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="project_posts"
    )
    image_main = CloudinaryField("image", default="placeholder")
    excerpt = models.TextField(blank=True)
    description = models.TextField()
    github_url = models.URLField(max_length = 200)
    live_url = models.URLField(max_length = 200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    published = models.IntegerField(choices=PUBLISH, default=0)
    likes = models.ManyToManyField(User, related_name="project_likes", blank=True)


# Meta class for ordering projects by date

    class Meta:
        """
        Meta class for ordering projects by date
        """
        ordering = ["-created_on"]

    def __str__(self):
        return str(self.title)

    def likes_counter(self):
        """
        Return the number of likes for a project
        """
        return self.likes.count()


# Comments model

class Comment(models.Model):
    """
    Model for the comments
    """
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text_pros = models.TextField()
    text_cons = models.TextField()
    score = models.IntegerField(choices=RATE, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)


    class Meta:
        """
        Meta class for ordering comments by date
        """
        ordering = ["created_on"]

    def __str__(self):
        return ("Pros: {self.text_pros}" +
                "Cons: {self.text_cons}"+
                "Score: {self.score}"+
                "By: {self.name}")
