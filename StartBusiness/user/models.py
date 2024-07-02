from django.db import models
import uuid
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self,user_id, user_mobile_number, user_email, user_password):
        if not user_email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            user_email = user_email,
            user_id = user_id,
            user_mobile_number = user_mobile_number,
            user_password = user_password,
           
        )

        user.set_password(user_password)
        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_email = models.EmailField(max_length=225, unique=True)
    user_mobile_number = models.CharField(max_length=225, unique=True)
    user_name = models.CharField(max_length=225)
    user_password = models.CharField(max_length=225)
    is_verify = models.BooleanField(default=False)
    user_role = models.CharField(max_length=225 , default='customer')
    otp_key = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_name = models.CharField(max_length=225,null=True)
    gender = models.CharField(choices=(('Male','Male'),('Female','Female'),('Other','Other')),max_length=10,default='Male')

    objects = UserManager()

    USERNAME_FIELD = "user_email"
    REQUIRED_FIELDS = ["user_name"]

    def __str__(self):
        return self.user_email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    # @property
   
    
    def save(self, *args, **kwargs):     
        # self.user_password = make_password(self.user_password)
  
        super(User, self).save(*args, **kwargs)
    