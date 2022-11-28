#pipenv install vds-api-client
# Documentation is wrong with the _ and -
from vds_api_client import VdsApiV2 
from vds_api_client import VdsApiV2
import pdb
import os
#pdb.set_trace()

## Credentials
vandersat_mail = os.environ['vandersat_mail']
vandersta_pwd = os.environ['vandersat_pwd']

## Testing API
vds = VdsApiV2(vandersat_mail, vandersta_pwd)