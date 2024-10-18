import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


# Address Model
class Address(models.Model):
    STRASSE_MAX_LENGTH = 100
    STADT_MAX_LENGTH = 100
    POSTLEITZAHL_MAX_LENGTH = 10
    HAUSNUMMER_MAX_LENGTH = 10

    strasse = models.CharField(max_length=STRASSE_MAX_LENGTH)
    hausnummer = models.CharField(max_length=HAUSNUMMER_MAX_LENGTH)
    postleitzahl = models.CharField(max_length=POSTLEITZAHL_MAX_LENGTH)
    stadt = models.CharField(max_length=STADT_MAX_LENGTH)

    def __str__(self):
        return f"{self.strasse} {self.hausnummer}, {self.postleitzahl} {self.stadt}"

# Bank Details Model
class BankDetails(models.Model):
    KONTOINHABER_MAX_LENGTH = 200
    IBAN_MAX_LENGTH = 34
    BIC_MAX_LENGTH = 11

    kontoinhaber = models.CharField(max_length=KONTOINHABER_MAX_LENGTH)
    iban = models.CharField(max_length=IBAN_MAX_LENGTH)
    bic = models.CharField(max_length=BIC_MAX_LENGTH)

    def __str__(self):
        return f"Kontoinhaber: {self.kontoinhaber}, IBAN: {self.iban}, BIC: {self.bic}"

# Member Model
class Member(models.Model):
    VORNAME_MAX_LENGTH = 100
    NACHNAME_MAX_LENGTH = 100
    NATIONALITAET_MAX_LENGTH = 100
    TELEFONNUMMER_MAX_LENGTH = 20
    EMAILADRESSE_MAX_LENGTH = 100
    BERUF_MAX_LENGTH = 100

    FAMILIENSTAND_CHOICES = [
        ('ledig', 'Ledig'),
        ('verheiratet', 'Verheiratet'),
        ('geschieden', 'Geschieden'),
        ('verwitwet', 'Verwitwet'),
    ]

    vorname = models.CharField(max_length=VORNAME_MAX_LENGTH)
    nachname = models.CharField(max_length=NACHNAME_MAX_LENGTH)
    geburtsdatum = models.DateField()
    geburtsort = models.CharField(max_length=NACHNAME_MAX_LENGTH)
    nationalitaet = models.CharField(max_length=NATIONALITAET_MAX_LENGTH)
    familienstand = models.CharField(max_length=20, choices=FAMILIENSTAND_CHOICES)
    telefonnummer = models.CharField(max_length=TELEFONNUMMER_MAX_LENGTH)
    emailadresse = models.EmailField(max_length=EMAILADRESSE_MAX_LENGTH)
    beruf = models.CharField(max_length=BERUF_MAX_LENGTH, blank=True, null=True)  # Optional field

    # Foreign keys to related models
    address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='members')
    bank_details = models.ForeignKey('BankDetails', on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return f"{self.vorname} {self.nachname}"
