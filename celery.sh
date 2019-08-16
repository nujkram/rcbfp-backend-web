#!/bin/bash
celery -A rcbfp worker --loglevel=debug --logfile=/rcbfp/logs/celery.log
