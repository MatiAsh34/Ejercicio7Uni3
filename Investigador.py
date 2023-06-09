from Personal import *

class Investigador(Personal):
	def __init__(self,cuil,apellido,nombre,sueldo_basico,antiguedad,carrera,cargo,catedra,area,tipo):
		super().__init__(cuil,apellido,nombre,sueldo_basico,antiguedad,carrera,cargo,catedra,area,tipo)
		self.__area = area
		self.__tipo = tipo
		
	def getArea(self):
		return self.__area

	def getTipo(self):
		return self.__tipo


	def toJSON(self):
		d = dict(
			__class__=self.__class__.__name__,
			__atributos__=dict(
				cuil = self.getCuil(),
				apellido = self.getApellido(),
				nombre = self.getNombre(),
				sueldo_basico = self.getSueldo_Basico(),
				antiguedad = self.getAntiguedad(),
				area = self.__area,
				tipo = self.__tipo
				)
			)
		return d