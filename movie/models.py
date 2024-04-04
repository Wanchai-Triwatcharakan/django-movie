from django.db import models

class Status_list(models.TextChoices):
    Yes = 'yes'
    No = 'no'
    
class Category(models.Model):
    name_category = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name_category

class Data_movie(models.Model):
    name = models.TextField()  # unique=True ไม่ให้มีข้อมูลซ้ำ
    image = models.ImageField(upload_to='movie_images') # อัพโหลดรูปภาพไปที่โฟลเดอร์ movie_images
    vdo_ex = models.TextField()
    vdo_main = models.TextField()
    vdo_main_2 = models.TextField()
    vdo_main_3 = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    status_list = models.CharField(max_length=3, choices=Status_list.choices, default=Status_list.No)


    # แปลงข้อมูลที่เป็น object ให้แสดงผลเป็นข้อความ
    def __str__(self):
        return self.name

class Data_list(models.Model):
    main_id = models.ForeignKey(Data_movie,on_delete=models.CASCADE,limit_choices_to={'status_list': 'yes'})
    name = models.TextField()
    vdo = models.TextField()
    vdo_2 = models.TextField()
    vdo_3 = models.TextField()
    part = models.IntegerField()
    
    def __str__(self):
        return str(self.main_id)