PENDING = 0
NOT_TO_OPERATE = 1
REINSPECT = 2
PASSED = 3
FAILED = 2

REMARKS_CHOICES = (
    (PENDING, 'Pending'),
    (NOT_TO_OPERATE, 'Not to Operate'),
    (REINSPECT, 'Reinspect'),
    (PASSED, 'FSIC'),
)

STATUS_CHOICES = (
    (PENDING, 'Pending'),
    (FAILED, 'Failed'),
    (PASSED, 'Passed')
)
