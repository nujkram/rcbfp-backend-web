FAILED = 0
PENDING = 1
APPROVED = 2
EXPIRED = 3

STATUS_CHOICES = (
    (FAILED, 'Denied'),
    (PENDING, 'Pending'),
    (APPROVED, 'Approved'),
    (EXPIRED, 'Expired')
)