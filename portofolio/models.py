from dataclasses import field
from django.db import models
from django.utils.html import mark_safe


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:        
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categorii'


class Tag(models.Model):
    caption = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.caption


class StarTest(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titlu")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Categorie")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titlu")
    slug = models.SlugField(max_length=200, unique=True)
    date = models.DateField(auto_now=True, verbose_name="Data")
    excerpt = models.CharField(max_length=200)
    content = models.TextField(verbose_name="Conținut")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Categorie")
    tags = models.ManyToManyField(Tag)

    @property
    def main_image(self):
        if len(self.image_set.all()):
            return self.image_set.filter(is_main=True)[0].image
        return ""

    def __str__(self):
        return self.title
    
    class Meta:        
        verbose_name = 'Proiect'
        verbose_name_plural = 'Proiecte'



class Image(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name="Nume")
    image = models.ImageField(upload_to='images/', verbose_name="Imagine")
    is_main = models.BooleanField(default=False, verbose_name="Principală")
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, verbose_name="Proiect")

    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" height="50" style="border-radius: 50%;" />'.format(self.image.url))
        return ""

    def __str__(self):
        return self.name

    class Meta:        
        verbose_name = 'Imagine'
        verbose_name_plural = 'Imagini'

class Quote(models.Model):
    text = models.TextField(max_length=500, verbose_name="Citat")
    project = models.ForeignKey(Project, models.SET_NULL, null=True, verbose_name="Proiect")

    class Meta:        
        verbose_name = 'Citat'
        verbose_name_plural = 'Citate'


class Comment(models.Model):
    user_name = models.CharField(max_length=150, verbose_name="User")
    user_email = models.EmailField(verbose_name="Email", null=True, blank=True)
    text = models.TextField(max_length=400, verbose_name="Text")
    project = models.ForeignKey(Project, models.SET_NULL, null=True, verbose_name="Proiect")

    class Meta:        
        verbose_name = 'Comentariu'
        verbose_name_plural = 'Comentarii'