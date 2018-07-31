import requests
import csv
with open('test.txt') as f:
    lines = f.read().split('\n')
fields = ['text','entity','intent','projection']
with open('result.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    for line in lines:
        r = requests.post('http://localhost:5002/parse',data=json.dumps({'q':line}))
        # print(r.text)
        # print(r.json()['projection'])
        r = r.json()
        # print(r['projection'])
        writer.writerow(r.values())
