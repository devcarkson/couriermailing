# core/models.py
from django.db import models

class ExpressSender(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    weight = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class ExpressReceiver(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Normalsender(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    weight = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Normalreceiver(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class AccountDetail(models.Model):
    BankName = models.CharField(max_length=60000)
    AccountNumber = models.CharField(max_length=50000)
    AccountName = models.CharField(max_length=50000)
    SwiftCode = models.CharField(max_length=50000, null=True)


    def __str__(self):
        return "Account Detail"

class Wallet(models.Model):
    Bitcoin = models.CharField(max_length=60000)
    Ethereum = models.CharField(max_length=500000)
    Solana = models.CharField(max_length=500000)

    def __str__(self):
        return "Wallet Address"


class ContactForm(models.Model):
    name = models.CharField(max_length=10000)
    email = models.EmailField()
    subject = models.CharField(max_length=10000)
    phonenumber = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name