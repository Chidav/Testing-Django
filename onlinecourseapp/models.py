from django.db import models


# Create your models here.
class pricing(models.Model):
    price1 = models.IntegerField()
    # price2 = models.IntegerField()
    # price3 = models.IntegerField()


class gallery(models.Model):
    link1 = models.ImageField(upload_to="images")
    link2 = models.ImageField(upload_to="images")
    home_img = models.ImageField(upload_to="images")
    about_img = models.ImageField(upload_to="images")
    gallery_img1 = models.ImageField(upload_to="images" )
    gallery_img2 = models.ImageField(upload_to="images")
    gallery_img3 = models.ImageField(upload_to="images")
    gallery_img4 = models.ImageField(upload_to="images")
    gallery_img5 = models.ImageField(upload_to="images")
    gallery_img6 = models.ImageField(upload_to="images")
    blog_img1 = models.ImageField(upload_to="images")
    blog_img2 = models.ImageField(upload_to="images")
    blog_img3 = models.ImageField(upload_to="images")
    blog_name1 = models.IntegerField()
    blog_name2 = models.CharField(max_length=10)
    team_img1 = models.ImageField(upload_to="images")
    team_img2 = models.ImageField(upload_to="images")
    team_img3 = models.ImageField(upload_to="images")
    team_img4 = models.ImageField(upload_to="images")
    footer_img = models.ImageField(upload_to="images")


class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=300)
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name
