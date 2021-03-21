from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField('Name', max_length=100, unique=True, default='general')

    class Meta:
        verbose_name = 'Tags'
        verbose_name_plural = verbose_name

    def __str__(self):
       return self.name
# magazine issue    
class Magazine(models.Model):
    pass

# news model
class News(models.Model):
    NEWS_STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    NEWS_FEATURE = (
        ('main', 'Main'),
        ('featured', 'Featured')
    )
    title = models.CharField('News Title', max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField('News Cover Image', upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    description = RichTextField('Article Description')
    body = RichTextField('News Body')
    date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.CharField('News Status', choices=NEWS_STATUS, max_length=20, default='draft',            help_text='Published or Draft')
    news_feature = models.CharField('Article Feature', choices=NEWS_FEATURE, max_length=20, help_text='News to be featured on home page')

    class Meta:
        ordering = ['-date']
        verbose_name = 'News Updates'
        verbose_name_plural = verbose_name

    def __str__(self):
       return self.title + ' ' + 'by' + ' ' + str(self.author)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

# article model
class Article(models.Model):
    # tag
    TAGS = (
        ('main', 'Main'),
        ('featured', 'Featured')
    )
    ARTICLE_STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField('Article Title', max_length=100, unique=True)
    date = models.DateField(auto_now=False, auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    image = models.ImageField('Cover Image')
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    article_feature = models.CharField('Article Feature', choices=TAGS, max_length=20)
    article_status = models.CharField('Article Status', choices=ARTICLE_STATUS, max_length=20, default='draft')
    body = RichTextField('Article Body', null=False, blank=False)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Articles'
        verbose_name_plural = verbose_name

    def __str__(self):
       return self.title + ' ' + 'by' + ' ' + str(self.author)

    def get_absolute_url(self):
        return reverse("home")
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

# Image Gallery
class ImageGallery(models.Model):
    name = models.CharField('Image Name', max_length=20)
    Tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True)
    caption = models.CharField('Image Caption', max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = 'Image Gallery'
        verbose_name_plural = verbose_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

# add with small pic
class smallAdd(models.Model):
    name = models.CharField("Add Name", max_length=150)
    image = models.ImageField(upload_to='images/')
    link = models.URLField("Preview LInk", max_length=150)

    class Meta:
        verbose_name = 'Small AdSpace'
        verbose_name_plural = verbose_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

# add with large pic
class largeAdd(models.Model):
    name = models.CharField("Add Name", max_length=150)
    image = models.ImageField(upload_to='images/')
    link = models.URLField("Preview LInk", max_length=150)

    class Meta:
        verbose_name = 'Large AdSpace'
        verbose_name_plural = verbose_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url