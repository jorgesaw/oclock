from django.db import models
from django.utils.text import slugify
from django.utils import timezone

from shortuuid.django_fields import ShortUUIDField

from userauths.models import User, Profile


LANGUAJE = (
    ("English", "English"),
    ("Spanish", "Spanish"),
    ("French", "French"),
)

LEVEL = (
    ("Beginner", "Beginner"),
    ("Intermediate", "Intermediate"),
    ("Advanced", "Advanced"),
)

TEACHER_STATUS = (
    ("Draft", "Draft"),
    ("Disabled", "Disabled"),
    ("Published", "Published"),
)

PLATFORM_STATUS = (
    ("Review", "Review"),
    ("Disabled", "Disabled"),
    ("Rejected", "Rejected"),
    ("Drafted", "Drafted"),
    ("Published", "Published"),
)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    image = models.FileField(upload_to="course-file", blank=True, null=True, default="default.jpg")
    full_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=255, blank=True, null=True)
    
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    about = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-full_name']
        indexes = [
            models.Index(fields=['-full_name']),
        ]


    def __str__(self):
        return self.full_name
    

    def students(self):
        return CartOrderItem.objects.filter(teacher=self)
    

    def courses(self):
        return Course.objects.filter(teacher=self)
    
    def review(self):
        return Course.objects.filter(teacher=self).count()


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to="course-file", blank=True, null=True, default="category.jpg")
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Category"
        ordering = ['title']
    

    def __str__(self):
        return self.title


    def course_count(self):
        return Course.objects.filter(category=self).count()
    

    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title)
        
        super(Category, self).save(*args, **kwargs)


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    title = models.CharField(max_length=230)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    languaje = models.CharField(choices=LANGUAJE, default="English", max_length=12)
    level = models.CharField(choices=LEVEL, default="Beginner", max_length=12)
    platform_status = models.CharField(choices=PLATFORM_STATUS, default="Published", max_length=12)
    teacher_course_status = models.CharField(choices=TEACHER_STATUS, default="Published", max_length=12)

    featured = models.BooleanField(default=False)

    course_id = ShortUUIDField(unique=True, length=6, max_length=20, alphabet="1234567890")

    file = models.FileField(upload_to="course-file", blank=True, null=True)
    image = models.FileField(upload_to="course-file", blank=True, null=True)
    
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title)
        
        super(Course, self).save(*args, **kwargs)
    

    def student(self):
        return EnrolledCourse.objects.filter(course=self)


    def curriculum(self):
        return VariantItem.objects.filter(variant__course=self)
    

    def lectures(self):
        return VariantItem.objects.filter(variant__course=self)
    

    def average_rating(self):
        average_rating = Review.objects.filter(course=self).aggregate(avg_rating=models.Avg('rating'))
        return average_rating['avg_rating']
    

    def rating_count(self):
        Review.objects.filter(course=self).count()
    

    def reviews(self):
        Review.objects.filter(course=self, active=True)


class Variant(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)

    title = models.CharField(max_length=1000)
    variant_id = ShortUUIDField(unique=True, length=6, max_length=20, alphabet="1234567890")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    

    def variant_items(self):
        return VariantItem.objects.filter(variant=self)


class VariantItem(models.Model):
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, related_name='variant_items')

    title = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True)

    file = models.FileField(upload_to="course-file")
    duration = models.DurationField(null=True, blank=True)
    content_duration = models.CharField(max_length=1000, null=True, blank=True)
    preview = models.BooleanField(default=False)

    variant_item_id = ShortUUIDField(unique=True, length=6, max_length=20, alphabet="1234567890")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.variant.title} - {self.title}'
