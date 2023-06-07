from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Currency(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Attachment(models.Model):
    class AttachmentType(models.TextChoices):
        PHOTO = 'Photo', _("PHOTO")
        VIDEO = 'VIDEO', _("VIDEO")
    name = models.CharField(max_length=255)
    file = models.ImageField('Attachment', upload_to='KGTravelGuide/attachments/')
    file_type = models.CharField('File type', choices=AttachmentType.choices, max_length=10)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.TextField()
    description = models.TextField()
    images = models.ForeignKey("Attachment", on_delete=models.PROTECT, null=True, blank=True)
    price = models.PositiveIntegerField(default=1)
    currency = models.ForeignKey("Currency", on_delete=models.PROTECT, null=False, default=1)
    city = models.CharField(max_length=255, default="Bishkek", null=False)
    address = models.TextField(default="")
    room_number = models.PositiveIntegerField(default=1)
    area = models.PositiveIntegerField(default=1)
    floor = models.TextField(default="")
    email = models.TextField(default="")
    phone = models.TextField(default="")
    whatsapp = models.TextField(default="")

    class PostType(models.TextChoices):
        SALE = 'Sale', _("Sale")
        RENT = 'Rent', _("Rent")

    post_type = models.CharField(
        max_length=10,
        choices=PostType.choices,
        default=PostType.SALE,
    )

    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.title

class SavedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    comment = models.TextField()