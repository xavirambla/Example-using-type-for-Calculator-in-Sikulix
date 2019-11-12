## Script que maneja la calculador utilizando la función type.

##Función que manipula el texto para convertir los caracteres de operativa de la calculadora en carácteres válidos
def getStringForTypeFunction(pText):
    vDict={'\\':Key.SEPARATOR, '+':Key.ADD, '-':Key.MINUS, '*':Key.MULTIPLY, '/':Key.DIVIDE , '=':Key.ENTER,}
    vRetorno=""
    for simbolo in pText:
        try:
            vNew=vDict[simbolo]
            vRetorno=vRetorno+vNew   
        except KeyError:
            vRetorno=vRetorno+simbolo
    return vRetorno


import java.lang.IllegalArgumentException
vApp =App.open("calc")
formula = input(u"Introduce la fórmula")
try:
    type("1573547938755.png",getStringForTypeFunction(formula))
    type(Key.ENTER)
except java.lang.IllegalArgumentException:    
    print ("IllegalArgumentException " , sys.exc_info()[0])
    type(Key.SHIFT)
except :
    print ("Error no identificado", sys.exc_info()[0])

