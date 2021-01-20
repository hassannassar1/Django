from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify
# Create your models here.
class Profile(models.Model):
    GENDER=(
            ('M',"Male"),
            ('F',"Female")
        )
    DOCTOR_IN=(
            ('جلدية',"جلدية"),              
            ('أسنان',"أسنان"),              
('باطنة',"باطنة"),              
            ('قلب',"قلب"),              
('جراحة',"جراحة"),              
            ('مخ وأعصاب',"مخ وأعصاب"),              
('نفسية',"نفسية"),              
            ('أنف وأذن وحنجرة',"أنف وأذن وحنجرة"),              
('عيون',"عيون"),              
            ('عظام',"عظام"),              
('أطفال',"أطفال"),              
            ('صدر',"صدر"),              
                           
              
           )
    user = models.OneToOneField(User,verbose_name=_("user"),on_delete=models.CASCADE)
    name = models.CharField(_("الأسم؟"),max_length=50)
    surname = models.CharField(_("اللقب؟"),max_length=50)
    who_i = models.TextField(_("من أنا ؟"),max_length=250)
    subtitle = models.CharField(_("نبذة عنك"),max_length=50)
    price = models.IntegerField(_("سعر الكشف"),null=True,blank=True)
    waiting_hours = models.IntegerField(_("عدد ساعات الإنتظار"),default=2)
    phone_number = models.CharField(_("رقم الموبايل"),max_length=14)
    working_hours = models.CharField(_("عدد ساعات العمل"),max_length=2)
    specialization = models.CharField(_("التخصص"),max_length=100,null=True,blank=True)
    address = models.CharField(_("المحافظة"),max_length=15)
    address_details = models.CharField(_("العنوان بالتفصيل"),max_length=15)
    image = models.ImageField(_("الصورة الشخصية"),upload_to="profile",null=True,blank=True)
    joined = models.DateTimeField(_("وقت الإنضمام"),auto_now_add=True,)
    slug = models.SlugField(_("slug"),null=True,blank=True)
    doctor = models.CharField(_("دكتور؟"),choices=DOCTOR_IN,max_length=30,)
    gender = models.CharField(_("النوع"),choices=GENDER,max_length=6)
    facebook = models.CharField(max_length=100,null=True,blank=True)
    twitter = models.CharField(max_length=100,null=True,blank=True)
    google = models.CharField(max_length=100,null=True,blank=True)
    
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)

        super(Profile,self).save(*args,**kwargs)    
    
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
    def __str__(self):
        return '%s' %self.user.username
def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
        
post_save.connect(create_profile,sender=User)        
    
    
