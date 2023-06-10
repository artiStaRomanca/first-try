from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget
from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from django.forms import TextInput, Textarea
from .models import Category, Comment, Image, Project, Quote, Tag, StarTest


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []

        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)

            output.append(
                f' <a href="{image_url}" target="_blank">'
                f' <img src="{image_url}" alt="{file_name}" height="50" '
                f' style="object-fit: cover; border-radius: 50%;"/> </a>')

        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe(u''.join(output))

# class ImageAdminForm(forms.ModelForm):
#     def clean_project(self):
#         project = self.cleaned_data['project']
#         if project.image_set.exclude(pk=self.instance.pk).count() == 3:
#             raise ValidationError('Max three images allowed!')
#         return project
        
class ImageInline(admin.TabularInline):
    model = Image
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}
    extra = 0
    # form = ImageAdminForm

class QuoteInline(admin.TabularInline):
    model = Quote
    formfield_overrides = {models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100})}}
    extra = 0

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    fields = ['title', 'slug', 'excerpt', 'content', 'category', 'tags']
    list_filter = ["category"]
    inlines = []
    prepopulated_fields = {"slug": ("title",) }
    inlines = [ ImageInline, QuoteInline]
    formfield_overrides = {models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100})}}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    
    
@admin.register(StarTest)
class StarTestAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['project', 'text']
    list_filter = ['project']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['project', 'user_name', 'text']
    list_filter = ['project']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    model = Image    
    list_display = ['image_preview', 'name', 'project', 'is_main']
    list_filter=('is_main', 'project')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['caption']