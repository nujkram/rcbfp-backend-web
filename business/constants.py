FAILED = 0
PENDING = 1
APPROVED = 2
EXPIRED = 3

BUSINESS_STATUS_CHOICES = (
    (FAILED, 'Non-compliant'),
    (PENDING, 'Pending'),
    (APPROVED, 'Compliant'),
    (EXPIRED, 'Expired')
)
