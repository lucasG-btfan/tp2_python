from num2words import num2words
dia=int(input("diga un dia: "))
mes=int(input("diga un mes: "))
año=int(input("diga un año: "))

class FuncionesPrograma:
     @staticmethod
     def getFechaString(dia,mes,año,):
          palabradia=num2words(dia,lang='es')
          palabraaño=num2words(año,lang='es')
          def sacarmes(ames):
             match (ames):
              case 1:
                  ames="Enero"
              case 2: 
                  ames="Febrero"
              case 3:
                  ames="Marzo"
              case 4:
                  ames="Abril"
              case 5:
                   ames="Mayo"
              case 6:
                   ames="Junio"  
              case 7:
                  ames="Julio"                      
              case 8:
                  ames="Agosto"      
              case 9:
                  ames="Septiembre"
              case 10:
                  ames="Octubre"   
              case 11:
                   ames="Noviembre"       
              case 12:
                   ames="Diciembre"  
             return ames
          print (f"Fecha: {palabradia} de {sacarmes(mes)} de {palabraaño}")
          
        
     def getFechaDate(diaa,mees,añoo):
         print(f"El dia es {diaa}/{mees}/{añoo}")

     
  
class Principal:
     def main():
         FuncionesPrograma.getFechaString(dia,mes,año,)
         FuncionesPrograma.getFechaDate(dia,mes,año)
          
Principal.main()
