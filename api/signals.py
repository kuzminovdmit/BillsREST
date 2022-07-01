from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Organization, Bill


@receiver(post_save, sender=Bill)
def increase_organization_fraud_weight(sender, instance, created, **kwargs):
    if created and instance.fraud_score >= 0.9:
        organization = instance.organization
        organization.fraud_weight += 1
        organization.save()


@receiver(post_delete, sender=Bill)
def decrease_organization_fraud_weight(sender, instance, **kwargs):
    organization = instance.organization
    organization.fraud_weight -= 1
    organization.save()
