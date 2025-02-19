from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    # I THINK -- TRY TO FIND TUTORIAL USED -- Allows class to be referenced plurally.
    class Meta: 
        verbose_name_plural = "categories"


    def __str__(self):
        return self.name
    


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title



class Comment(models.Model): 
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"

                    

class Contact(models.Model):
    enquiry_text = models.CharField(max_length=500)
    enquiry_select = models.CharField(max_length=100)
    enquire_fname = models.CharField(max_length=20)
    enquire_lname = models.CharField(max_length=20)
    enquire_email = models.CharField(max_length=30)

    # def __str__(self):
    #     return f'{self.enquire_email}' 

