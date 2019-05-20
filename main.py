import requests

payload = {'nombre' : 'Jose', 'apellido':'solares', 'telefono' : '23465709'}
r = requests.post('https://demo2452794.mockable.io/finalprograufm_get', json=payload)
print(r.text) 