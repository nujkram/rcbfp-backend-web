FAILED = 0
PENDING = 1
DONE = 2

RENEWAL = 0
NEW = 1
REINSPECT = 2

STATUS_CHOICES = (
    (FAILED, 'Denied'),
    (PENDING, 'Pending'),
    (DONE, 'Approved'),
)

INSPECTION_TYPE_CHOICES = (
    (RENEWAL, 'Renewal'),
    (NEW, 'New'),
    (REINSPECT, 'Reinspect'),
)
