from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()


# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    content = models.TextField(blank=True, max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    def last_massage(self):
        result=Message.objects.order_by('-timestamp').all()
        print(result)
        for i in result:
            print(i.content)
        return result

    def __str__(self):
        return self.author.username