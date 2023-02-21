  
class Motor:
  def __init__ (self, numeroCilindros: int, tipo:str, registro:int):
    self.numeroCilindros=numeroCilindros
    self.tipo=tipo
    self.registro=registro
  
  def cambiarRegistro(self, registro:int):
    self.registro=registro

  def asignarTipo(self, tipo:str):
    if tipo=="electrico" or tipo=="gasolina":
      self.tipo=tipo

class Asiento:
  def __init__ (self, color:str, precio:int, registro:int):
    self.color=color
    self.precio=precio
    self.registro=registro
  
  def cambiarColor(self, color:str):
    if (color=="verde" or color=="rojo" or color=="amarillo" or color=="negro" or color=="blanco"):
      self.color=color
    else:
      self.color=self.color

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
    c=0
    for i in self.asientos:
      if type(i)==Asiento:
        c+=1
    return c

  def verificarIntegridad(self):
    if self.registro != self.motor.registro:
      return "Las piezas no son originales"
    for j in self.asientos:
      if j.registro != self.registro:
        return "Las piezas no son originales"
    return "Auto original"
  

  