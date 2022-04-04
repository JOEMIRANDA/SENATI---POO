class Trabajador:
    def __init__(self, nombre,categoria,horas_x,tardanzas):
      self.nombre = nombre
      self.categoria = categoria
      self.horas_x = horas_x
      self.tardanzas = tardanzas
      
      
    def nom(self):
      print("TRABAJADOR:                   ",self.nombre)
      print("CATEGORIA:                    ",self.categoria)
      print("HORAS EXTRAS:                 ", self.horas_x)
      print("TARDANZAS:(minutos)           ",self.tardanzas)




