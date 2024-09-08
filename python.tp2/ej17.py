from num2words import num2words
dia=int(input("diga un dia: "))
mes=int(input("diga un mes: "))
año=int(input("diga un año: "))
palabradia=num2words(dia,lang='es')
palabraaño=num2words(año,lang='es')
def sacarmes(palabrames):
     match(palabrames):
      case 1:
         palabrames="Enero"
      case 2: 
         palabrames="Febrero"
      case 3:
         palabrames="Marzo"
      case 4:
         palabrames="Abril"
      case 5:
         palabrames="Mayo"
      case 6:
         palabrames="Junio"  
      case 7:
         palabrames="Julio"                      
      case 8:
         palabrames="Agosto"      
      case 9:
        palabrames="Septiembre"
      case 10:
         palabrames="Octubre"   
      case 11:
          palabrames="Noviembre"       
      case 12:
         palabrames="Diciembre"  
     return palabrames


class FuncionesPrograma:
     @staticmethod
     def getFechaString(palabradia,conclusionmes,palabraaño):
          print (f"La fecha es: {palabradia} de {conclusionmes} de {palabraaño}")
class Principal:
     def main():
         FuncionesPrograma.getFechaString(palabradia,sacarmes(mes),palabraaño)
          
Principal.main()
