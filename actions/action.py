import sys
import requests

#templateid=sys.argv[1]
from requests.auth import HTTPBasicAuth

res = requests.post('http://20.198.234.27/api/v2/job_templates/'+'9'+'/launch/', verify=False, auth=HTTPBasicAuth('admin','MinhNhut@#68'))
print (res.content)
