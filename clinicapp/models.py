from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class clinicuser(AbstractUser):
    ROLE_CHOICES = [
        ('B_Admin', 'BAdmin'),
        ('T_Admin', 'TAdmin'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='TAdmin')
    
    groups = models.ManyToManyField(
        Group,
        related_name='clinic_users',
        related_query_name='clinic_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='clinic_users',
        related_query_name='clinic_user',
    )
    
    class Meta:
        permissions = [
            ("can_view_dashboard", "Can view dashboard"),
            ("can_view_all_users", "Can view all users")
        ]
