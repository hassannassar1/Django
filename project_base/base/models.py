from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
#from django.db.models.signals import post_save
#from django.utils.text import slugify
# Create your models here.
class Profile(models.Model):
    GENDER=(
            ('M',"Male"),
            ('F',"Female")
        )
    user = models.OneToOneField(User,verbose_name=_("user"),
                                                on_delete=models.CASCADE)
    first_name = models.CharField(_("First Name"),max_length=50)
    last_name = models.CharField(_("Last Name"),max_length=50)
    email = models.EmailField(_("Email Address"),max_length=100,)
    gender = models.CharField(_("Gender"),choices=GENDER,max_length=6)
    bio = models.TextField(_("Bio"),max_length=250,null=True,blank=True)
    phone_number = models.CharField(_("Phone Number"),max_length=14,
                                                null=True,blank=True)
    address = models.CharField(_("Country"),max_length=15)
    address_details = models.CharField(_("Detailed address"),max_length=15)
    image = models.ImageField(_("Profile Picture"),upload_to="profile",
                                                    null=True,blank=True)
    joined = models.DateTimeField(_("Joined"),auto_now_add=True,)
    slug = models.SlugField(_("slug"),null=True,blank=True)
    date_of_birth = models.DateField(_("Birth Date"),blank=True, null=True)
    
    
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
    
    def __str__(self):
        return '%s' %self.user.username
    '''
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)

        super(Profile,self).save(*args,**kwargs)    
    
    
    
def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
        
post_save.connect(create_profile,sender=User)  
'''    