import maya.cmds as mc

"""
@param: kit de utilidades para joints
"""

def jerarquiaListada(baseJoint,finalJoints=True):
    """lista de jerrquia parte en baseJoint"""
    
    listaJoints=mc.listRelatives(baseJoint,type="joint",ad=True)
    listaJoints.append(baseJoint)
    listaJoints.reverse()
    
    compilaJoints=listaJoints[:]
    
    if not finalJoints:
        compilaJoints=[j for j in listaJoints if mc.listRelatives(j,c=1,type="joint")]
    
    return compilaJoints