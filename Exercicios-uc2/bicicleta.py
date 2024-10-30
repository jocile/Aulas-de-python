class Bicicleta:
  def __init__(self, cor, modelo, ano, valor):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor

  def buzinar(self):
    print("bi bi biii")
  
  def parar(self):
    print("bicicleta parou")

  def correr(self):
    print("bicicleta correndo")
  
  def __str__(self) -> str:
    return f"A bicicleta tipo {self.modelo} da cor {self.cor} custa {self.valor}"
    

bicicleta_1 = Bicicleta("azul", "caloi", 1999, 250)
bicicleta_2 = Bicicleta("vermelha", "Monarck", 2010, 300)
bicicleta_1.buzinar()
print(bicicleta_1.modelo)

bicicleta_2.correr()
print(bicicleta_1)
print(bicicleta_2)