from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from .validators import publish_email_validation, check_string_validation
from django.utils.text import slugify
from django.utils.timesince import timesince
from datetime import timedelta, datetime, date

PUBLISH_CHOICES =(
    ('draft','Draft'),
    ('publish','Publish'),
    ('default','Default')
)


class PostModelQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active = True)

    def post_items(self, value):
        return self.filter(title__icontains = value)



class PostModelManager(models.Manager):
    def get_queryset(self): #Wrapping the Query set with model Manager #Default method
        return PostModelQuerySet(self.model, using = self._db)

    def all(self, *args, **kwargs):
        qs = super(PostModelManager, self).all(*args, **kwargs).filter(action=True)
        print(qs)
        return qs

    def get_timeframe(self, date1, date2):
        qs = self.get_queryset()
        qs_time1 = qs.filter(publish_date__gte = date1)
        qs_time2 = qs_time1.filter(publish_date__lt = date2)

        #Combination of qs_time1 and qs_time2
        #final_qs = (qs_time1 | qs_time2).distinct()

        return qs_time2


class PostModel(models.Model):
    id = models.AutoField(primary_key= True) #auto increments
    #id = models.IntegerField(primary_key = True) #auto increments
    action = models.BooleanField(default = True) #Default value true
    #action2 = models.NullBooleanField() #Nullable
    slug = models.SlugField(editable=True, null=True, blank=True) # Editable = false then we cannot edit and it will show
    title = models.CharField(null=True,
                             max_length=200,
                             verbose_name= "Post Title",
                             unique=True,
                             error_messages =
                             {"unique": "This title is not unique"},
                             help_text="This item should be unique.")
    content = models.TextField(null = True, blank=True) # blank make it not required
    publish = models.CharField(max_length=250, choices=PUBLISH_CHOICES, default='draft')
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now = False, auto_now_add= False, default=timezone.now())
    publish_email = models.CharField(max_length=240, validators=[publish_email_validation, check_string_validation], null=True)
    email = models.EmailField(max_length=240, validators=[check_string_validation], null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    modManager = PostModelManager()
    modManager_2 = PostModelManager()


    def save(self, *args, **kwargs):
        super(PostModel, self).save(*args,**kwargs)

    def __str__(self): #convert an object to a string Just Like  toString() method
        return self.title

    def __unicode__(self):
        return smart_text(self.title) #Smart Text is used to convert text into utf-8

    class Meta: #It is optional to make it readable
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def age(self):
        if self.publish == "publish":
            now = datetime.now()
            publish_time = datetime.combine(self.publish_date, datetime.now().min.time())

            try:
                diffrence = now - publish_time
            except:
                return "UnKnown"

            if diffrence<= timedelta(minutes =1):
                return "Just Now"
            return "{time} ago".format(time = timesince(publish_time).split(", ")[0])
        return "Not Publish"

    @property
    def ftn_Property(self):
        return "Make method as a Property like others (title, slug etc)"

def blog_post_model_pre_save_receiver(sender, instance, *args, **kwargs):
    print("Before Save")
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)

pre_save.connect(blog_post_model_pre_save_receiver, sender = PostModel)


def blog_post_model_post_save_receiver(sender, instance, created, *args, **kwargs):
    print("After Save")
    print(created)
    if created:
        instance.save()#It will call save function Of model which again call post save function

post_save.connect(blog_post_model_post_save_receiver, sender=PostModel)

"""
Everytime we change something in model, just do


“python manage.py makemigrations” //Setting up the database changes
“python manage.py migrate” //Run the database changes

"""