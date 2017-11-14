import urllib.request

import json


way1 = '42.3314300,-83.0457500'
way0 = '42.3873532,-83.2263674'

with urllib.request.urlopen('https://route.cit.api.here.com/routing/7.2/calculateroute.json?app_id=8F1RFyPZhyqzXdPYDY5X&app_code=8A2jhlt0SHYdRiD7rVs1pw&waypoint0=geo!'+ way0 + '&waypoint1=geo!'+ way1 +'&mode=fastest;car;traffic:enabled') as f:
   json_str = str(f.read(), 'utf-8')

parsed_json = json.loads(json_str)
i = 0
waypoints = len(parsed_json['response']['route'][0]['leg'][0]['maneuver'])
print(waypoints, ' Waypoints')



print('heelo'+way1)
#way1+=str(way0)

print(way1)


while i < waypoints:
    lat = str(parsed_json['response']['route'][0]['leg'][0]['maneuver'][i]['position']['latitude'])
    lon = str(parsed_json['response']['route'][0]['leg'][0]['maneuver'][i]['position']['longitude'])
    print('        ',lon, ' ' ,lat)
    i = i+1





#print(str(len(parsed_json['response']['route'][0]['leg'][0]['maneuver'])))
#print(str(parsed_json['response']['route'][0]['leg'][0]['maneuver'][2]['position']))
