import json

f = open("clientes.json", "r")

try:
  clientes_json = f.read() # ler arquivo
  clientes = json.loads(clientes_json) # converte para objeto dict

  for cliente in clientes:
    print(f"-" * 30)
    print(f"id: {cliente['id']}")
    print(f"nome: {cliente['nome']}")
    print(f"email: {cliente['email']}")
    
except Exception as e:
  print(e)
  print("Algo deu errado na leitura do arquivo")
finally:
  f.close()