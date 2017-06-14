import requests

r = requests.get('http://picole-pi2.herokuapp.com/machines/1/')

machine = r.json()

for i in machine["stocks"]:
    name = '{}.txt'.format(i["popsicle"]["flavor"])
    with open(name, 'w') as f:
        f.write(str(i["amount"]))
