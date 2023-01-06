from django.db import models

# Create your models here.


class Account(models.Model):
    c1 = models.SmallIntegerField()
    c2 = models.SmallIntegerField()
    c3 = models.SmallIntegerField()
    c4 = models.SmallIntegerField()
    c5 = models.SmallIntegerField()
    c6 = models.SmallIntegerField()
    dp = models.CharField(max_length=3)
    account = models.CharField(max_length=100)

    def __str__(self):
        text = f"{self.c1}-{self.c2}{self.c3}{self.c4}{self.c5}{self.c6} | {self.account}".title()
        return text


class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date} | {self.type}"


class Journal(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    pos = models.CharField(max_length=6)
    total = models.IntegerField()

    def __str__(self):
        return f"{self.transaction} | {self.account}"






