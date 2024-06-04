from django.db import models
from common.models import CommonModel
# Create your models here.

#제목, 내용, 작성자
#Feed와 user의 관계
#   user:feed = 1:N
#       feeds가 foreignkey를 가짐

class Feed(CommonModel):
    title= models.CharField(max_length=30)
    content= models.CharField(max_length=120)
    users= models.ForeignKey("users.User", on_delete=models.CASCADE)
        #user가 삭제되면 user의 모든 feeds 삭제

