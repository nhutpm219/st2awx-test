from st2common.runners.base_action import Action
import sys
import requests

#templateid=sys.argv[1]

from requests.auth import HTTPBasicAuth

class LauchAWXTemplate(Action):
    def run(self):
        res = requests.post('http://20.198.234.27/api/v2/job_templates/'+'9'+'/launch/', verify=False, auth=HTTPBasicAuth('admin','MinhNhut@#68'))
        print (res.content)
