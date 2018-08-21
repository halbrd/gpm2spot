import json
import gmusicapi

with open('credentials.json', 'r') as f:
    credentials = json.load(f)

api = gmusicapi.clients.Mobileclient()
api.login(credentials['email'], credentials['password'], credentials['device_id'])

with open('data.json', 'w') as f:
    json.dump(api.get_all_songs(), f, indent='\t')
