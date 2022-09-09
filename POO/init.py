class Celular():
  def __init__(self):
    self.capa = ""
    self.cor = ""
    self.botoes = []

  def ligar(self):
    return f"Estou ligando o celular com a capa ({self.capa}) nos botões ({self.botoes_formatados})"

  def botoes_formatados(self):
    return ', '.join(self.botoes)


samsung = Celular()
samsung.capa = "B3G-ttt"
samsung.cor = "Preto"
samsung.botoes = ["Ligar", "Volume Up", "Volume Down", "Home"]

lg = Celular()
lg.capa = "KG-ttt"
lg.cor = "Vermelho"
lg.botoes = ["Ligar", "Volume Up", "Volume Down", "Home"]

iphone = Celular()
iphone.capa = "11-ttt"
iphone.cor = "Prata"
iphone.botoes = ["Ligar", "Volume Up", "Volume Down", "Home"]