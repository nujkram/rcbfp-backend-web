FAILED = 0
PENDING = 1
APPROVED = 2
EXPIRED = 3

LOCATION_CHOICES = (
    ('Interior', 'Interior'),
    ('Exterior', 'Exterior'),
)

CURRENT_CHOICES = (
    ('AC/DC', 'AC/DC'),
    ('Others', 'Others'),
)

STANDPIPE_CHOICES = (
    ('Wet', 'Wet'),
    ('Dry', 'Dry'),
)

FUEL_CHOICES = (
    ('Bunker', 'Bunker'),
    ('Coal', 'Coal'),
    ('Diesel', 'Diesel'),
    ('Kerosene', 'Kerosene'),
    ('PG', 'PG'),
)

CONTAINER_LOCATION_CHOICES = (
    ('Above Ground', 'Above Ground'),
    ('Underground', 'Underground'),
)

GENERATOR_TYPE_CHOICES = (
    ('Automatic', 'Automatic'),
    ('Manual', 'Manual'),
)

GENERATOR_FUEL_CHOICES = (
    ('Diesel', 'Diesel'),
    ('Gasoline', 'Gasoline'),
)

GENERATOR_DISPENSING_CHOICES = (
    ('By Gravity', 'By Gravity'),
    ('By Pump', 'By Pump'),
)

SERVICE_SYSTEM_CHOICES = (
    ('Water Treatment', 'Water Treatment'),
    ('Water Sewage Treatment Facility', 'Water Sewage Treatment Facility'),
)

HAZARDOUS_AREA_CHOICES = (
    ('Kitchen', 'Kitchen'),
    ('Laundry', 'Laundry'),
    ('Windowless Basement', 'Windowless Basement'),
    ('Storage Room', 'Storage Room'),
    ('Others', 'Others'),
)

BUILDING_STATUS_CHOICES = (
    (FAILED, 'Denied'),
    (PENDING, 'Pending'),
    (APPROVED, 'Approved'),
    (EXPIRED, 'Expired')
)
