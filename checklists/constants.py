FAILED = 0
PENDING = 1
APPROVED = 2
REINSPECT = 3

REMARKS_CHOICES = (
    (PENDING, 'Pending'),
    (REINSPECT, 'Reinspect'),
    (APPROVED, 'FSIC'),
)

STATUS_CHOICES = (
    (PENDING, 'Pending'),
    (FAILED, 'Non-Compliant'),
    (APPROVED, 'Compliant')
)
