from config import *
import argparse
from tabulate import tabulate
import requests
import json
from dateutil.parser import parse

parser = argparse.ArgumentParser(description='API tocken key')
parser.add_argument('--token', metavar='token', type=str, nargs='?', help='API token key')
args = parser.parse_args()

headers = {
  'accept': 'application/json',
  'X-API-Token': args.token
}

response = requests.get(f'https://api.appcenter.ms/v0.1/apps/{user}/{appname}/branches', headers=headers, data=data)

for obj in response.json():
  name = obj['branch']['name']
  status = obj['lastBuild']['result']
  st = parse(obj['lastBuild']['startTime'])
  ft = parse(obj['lastBuild']['finishTime'])
  duration = ft - st
  id = obj['lastBuild']['id']
  link = f'python3 build_logs.py {id} --token=%secret_key%'
  ar.append([name, status, duration, link])

print(tabulate(ar, headers=['Branch name', 'Build status', 'Duration', 'Link to build log'], tablefmt='orgtbl'))
