from django.db import models
from accounts.models import User

class Address(models.Model):
		# 강의에서는 python shell에서 관계 설정을 했지만, 과제에서는 아래와 같이 코드로 관계설정을 합니다.
		# 코드 작성이라고 적혀있는 부분에 코드를 작성해주시면 됩니다.
		
    user = models.ForeignKey(User, related_name="addresses", on_delete= models.CASCADE)
    street = models.CharField(max_length=225)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}"