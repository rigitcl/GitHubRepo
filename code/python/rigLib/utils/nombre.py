"""
@ nombre utils
@ utilidad para limpiar suffix
"""

def remueveSuffix(nombre):
    """
    remueve sufijo
    @raram: nombre: pasarle un string para procesar
    @return: str,nombre con sufijo
    """
    
    edits=nombre.split("_")
    if len(edits)<2:
        return nombre
    
    suffix="_"+ edits[-1]
    nombreNoSuffix=nombre[:-len(suffix)]
    
    return nombreNoSuffix