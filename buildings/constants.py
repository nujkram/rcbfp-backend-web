FAILED = 0
PENDING = 1
APPROVED = 2
EXPIRED = 3

LOCATION_CHOICES = (
    ('None', 'None'),
    ('Interior', 'Interior'),
    ('Exterior', 'Exterior'),
)

CURRENT_CHOICES = (
    ('None', 'None'),
    ('AC/DC', 'AC/DC'),
    ('Others', 'Others'),
)

STANDPIPE_CHOICES = (
    ('None', 'None'),
    ('Wet', 'Wet'),
    ('Dry', 'Dry'),
)

FUEL_CHOICES = (
    ('None', 'None'),
    ('Bunker', 'Bunker'),
    ('Coal', 'Coal'),
    ('Diesel', 'Diesel'),
    ('Kerosene', 'Kerosene'),
    ('PG', 'PG'),
)

CONTAINER_LOCATION_CHOICES = (
    ('None', 'None'),
    ('Above Ground', 'Above Ground'),
    ('Underground', 'Underground'),
)

GENERATOR_TYPE_CHOICES = (
    ('None', 'None'),
    ('Automatic', 'Automatic'),
    ('Manual', 'Manual'),
)

GENERATOR_FUEL_CHOICES = (
    ('None', 'None'),
    ('Diesel', 'Diesel'),
    ('Gasoline', 'Gasoline'),
)

GENERATOR_DISPENSING_CHOICES = (
    ('None', 'None'),
    ('By Gravity', 'By Gravity'),
    ('By Pump', 'By Pump'),
)

SERVICE_SYSTEM_CHOICES = (
    ('None', 'None'),
    ('Water Treatment', 'Water Treatment'),
    ('Water Sewage Treatment Facility', 'Water Sewage Treatment Facility'),
)

HAZARDOUS_AREA_CHOICES = (
    ('None', 'None'),
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
