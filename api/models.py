from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def organizations_count(self):
        return self.organization_set.count()

    @property
    def organizations_income(self):
        return sum(
            organization.bill_set.aggregate(bills_sum=models.Sum('sum'))['bills_sum']
            for organization in self.organization_set.all()
        )


class Organization(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    fraud_weight = models.PositiveSmallIntegerField(default=0)

    class Meta:
        unique_together = ['name', 'client']
        ordering = ['client', 'name']

    def __str__(self):
        return self.name


class Bill(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    client_number = models.PositiveSmallIntegerField(default=1)
    sum = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    date = models.DateField()
    fraud_score = models.FloatField(default=0)
    service_class = models.PositiveSmallIntegerField(default=1)
    service_name = models.CharField(max_length=32)

    class Meta:
        ordering = ['client', 'client_number']
        unique_together = ['organization', 'client_number']

    def __str__(self):
        return f'{self.service_name.capitalize()} для {self.client}'
