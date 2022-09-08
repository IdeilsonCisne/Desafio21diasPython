import json

cliente = {
  "id": 1,
  "nome": "Ideilson",
  "email": "ideilson.cisne@teste.com",
}

clientes = []
clientes.append(cliente)

f = open("clientes.json", "w")
try:
  clientes_json = json.dumps(clientes)
  f.write(clientes_json)
except Exception as e:
  print(e)
  print("Algo deu errado a escrita do arquivo")
finally:
  f.close()