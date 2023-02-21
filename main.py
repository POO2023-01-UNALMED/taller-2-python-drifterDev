  
class Motor:
  def __init__ (self, numeroCilindros: int, tipo:str, registro:int):
    self.numeroCilindros=numeroCilindros
    self.tipo=tipo
    self.registro=registro
  
  def cambiarRegistro(self, registro:int):
    self.registro=registro

  def asignarTipo(self, tipo:str):
    if tipo.lower()=="electrico" or tipo.lower()=="gasolina":
      self.tipo=tipo.lower()

class Asiento:
  def __init__ (self, color:str, precio:int, registro:int):
    self.color=color
    self.precio=precio
    self.registro=registro
  
  def cambiarColor(self, color:str):
    colores=["verde", "rojo", "amarillo", "negro", "blanco"]
    if color.lower() in colores:
      self.color=color.lower()

class Auto:
  cantidadCreados=0
  def __init__(self, modelo:str, precio:int, asientos:list, marca:str, motor:Motor, registro:int):
    self.modelo=modelo
    self.precio=precio
    self.asientos=asientos
    self.marca=marca
    self.motor=motor
    self.registro=registro

  def cantidadAsientos(self):
    cantidad=0
    for i in range(len(self.asientos)):
      if type(self.asientos[i])==Asiento:
        cantidad+=1
    return cantidad

  def verificarIntegridad(self):
    if self.registro != self.motor.registro:
      return "Las piezas no son originales"
    for j in range(len(self.asientos)):
      if (type(self.asientos[j])==Asiento):
        if (self.asientos[j].registro != self.registro):
          return "Las piezas no son originales"
    return "Auto original"
  

  