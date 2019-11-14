from config import *
import argparse
import requests
import json

parser = argparse.ArgumentParser(description='API tocken key and build id')
parser.add_argument('id', metavar='id', type=int, nargs='?', help='id is integer')
parser.add_argument('--token', metavar='token', type=str, nargs='?', help='API token key')
args = parser.parse_args()

headers = {
  'accept': 'application/json',
  'X-API-Token': args.token
}

response = requests.get(f'https://api.appcenter.ms/v0.1/apps/{user}/{appname}/builds/{args.id}/logs', headers=headers)

for obj in response.json()['value']:
  log = f'{log}{obj}\n'

print(log)
