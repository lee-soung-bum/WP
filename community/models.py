from django.db import models

class Question2002(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date publisghed')

    def __str__(self):
        return self.question_text

class Choice2002(models.Model):
    question = models.ForeignKey(Question2002, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

######################################################33

class Question2010(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date publisghed')

    def __str__(self):
        return self.question_text

class Choice2010(models.Model):
    question = models.ForeignKey(Question2010, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

###########################################################

class QuestionNow(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date publisghed')

    def __str__(self):
        return self.question_text

class ChoiceNow(models.Model):
    question = models.ForeignKey(QuestionNow, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

#######################################################3

class QuestionBest(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date publisghed')

    def __str__(self):
        return self.question_text

class ChoiceBest(models.Model):
    question = models.ForeignKey(QuestionBest, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

##################################################################

class User(models.Model):
    username = models.CharField(max_length=64 , verbose_name="이름")
    userid = models.CharField(max_length=64 , verbose_name="아이디")
    password = models.CharField(max_length=64 , verbose_name="비밀번호")
    registerd_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.username

    class Meta:  # 메타 클래스를 이용하여 테이블명 지정
        db_table = 'test_user'