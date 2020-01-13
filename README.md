## System Dependencies
- Nginx
- Postgresql 9.5
- Python 3.6
- Gunicorn


## Locations and DateDim
-- Load locations json
-- Preload DateDim from 2015 - 2020

## Get Data
1. Open shell
2. from helpers import converter
3. buildings = converter.import_building_data()

## Generate Buildings and Businesses
1. from helpers import converter, batch_create
2. batch_create.businesses(buildings)

## Generate Checklist for each Businesses by Year
1. from helpers import converter, batch_create
2. businesses = Business.objects.all()
3. batch_create.checklist(businesses, [year])

## Generate Incident Report
1. from helpers import batch_create
2. batch_create.incidents([number of incident(s)], [year])
