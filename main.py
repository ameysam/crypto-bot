import requests
import json

def get_data():
    response = requests.get('http://data.fixer.io/api/latest?access_key=a1aef3b10ba8eec768b8f248eeed4c02')
    if response.status_code == 200:
        return response.text
    return None
        
def archive(filename, rates):
    with open(f'./archives/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))

if __name__ == "__main__":
    data = get_data()
    data = json.loads(data)
    archive(data['timestamp'], data['rates'])
    print(data)