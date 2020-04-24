from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date_published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    imgpath = models.FilePathField(default=__file__)

    def __str__(self):
        return self.choice_text

# shell'de Question modelini çağırıp variable'a assign edince
# choice_set diye bi metot olduğunu farkettim. Ben yazmamıştım, kendi yapıyor demek ki.

# diger husus da, q.choice_set.create(choice_text="Spring", votes=2) dediğimizde
# db'ye otomatik kaydediyor.

