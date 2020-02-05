from django.db import models

class BankInfo(models.Model):
    name = models.CharField(max_length=50,unique=True)


    class Meta:

        ordering = ('name',)

    def __str__(self):
        return "{}".format(self.name)

class BranchInfo(models.Model):
    ifsc = models.CharField(max_length=150)
    bank_id=models.CharField(max_length=5)
    branch_name = models.CharField(max_length=256)
    address = models.TextField()
    city = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    bank_name = models.CharField(max_length=150)

    class Meta:
        ordering=('ifsc',)

    def __str__(self):
        return "{0} | {1}  | {2} ".format(self.branch_name, self.city, self.bank_name)
