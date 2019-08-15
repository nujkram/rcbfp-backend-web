from os import path
from split_settings.tools import include

if path.isfile('/home/vagrant/rcbfp-backend-web/envars/local-mark'):
  print('connecting to local-mark settings...')
  include('settings_collection/local-mark.py')
elif path.isfile('/home/vagrant/rcbfp-backend-web/envars/test-server'):
  print('connecting to local-mark settings...')
  include('settings_collection/test-server.py')
elif path.isfile('/home/vagrant/rcbfp-backend-web/envars/test-server'):
  print('connecting to test-server settings...')
  include('settings_collection/test-server.py')
else:
  print('connecting to production settings...')
  include('settings_collection/productino.py')