SUPERADMIN = 984
ADMIN = 548
INSPECTOR =374

USER_TYPE_CHOICES = (
    (SUPERADMIN, 'Super User'),
    (ADMIN, 'Admin'),
    (INSPECTOR, 'Inspector')
)

USERNAME_REGEX = "^[a-zA-Z0-9.-]*$"

USER_CREATION_TYPE_CHOICES = (
    (ADMIN, 'Admin'),
    (INSPECTOR, 'Inspector'),
)