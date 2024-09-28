from django.db import models
from wagtail.admin.panels.field_panel import FieldPanel
from wagtail.models import Page


class Article(Page):
    author = models.CharField(max_length=255)
    date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/")
    tags = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel("author"),
        FieldPanel("date"),
        FieldPanel("body"),
        FieldPanel("image"),
        FieldPanel("tags"),
        FieldPanel("category"),
        FieldPanel("is_featured"),
        FieldPanel("is_published"),
    ]

    def __str__(self):
        return self.title

