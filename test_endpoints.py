import subprocess
import json

def make_request(url):
    response = subprocess.run(['curl', '-s', url], capture_output=True, text=True)
    return response

def check_response(response, keys):
    try:
        data = json.loads(response.stdout)
        for key in keys:
            if key not in data:
                return False
        return True
    except json.JSONDecodeError:
        return False

urls = [
    'https://pokeapi.co/api/v2/pokemon/1',      
    'https://pokeapi.co/api/v2/type/1',          
    'https://pokeapi.co/api/v2/ability/1'          
]

expected_keys = [
    ['id', 'name', 'base_experience', 'height', 'weight'],
    ['id', 'name', 'damage_relations', 'pokemon'],
    ['id', 'name', 'effect_entries']
]

for i, url in enumerate(urls):
    response = make_request(url)
    if response.returncode != 0:
        print(f"Test {i + 1}: FAILED (HTTP request error)")
    elif response.returncode == 0 and check_response(response, expected_keys[i]):
        print(f"Test {i + 1}: PASSED")
    else:
        print(f"Test {i + 1}: FAILED (Missing keys in JSON response)")
