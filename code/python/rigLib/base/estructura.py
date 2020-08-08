"""
estructura de grupos y modulo de rigging
"""
import maya.cmds as mc
sceneObjectType = "rig"

from.import control
class Root():
    """
    base para construir la estructura 
    """
    def __init__(self, nombrePersonaje="nuevo",scale=1.0):
        
        self.baseGrp = mc.group(n=nombrePersonaje + "_rig_grp", em=1)
        self.rigGrp= mc.group(n="rig_grp", em=True,p= self.baseGrp)
        self.meshGrp= mc.group(n="geo_grp", em=1,p=self.baseGrp)
        
        nombrePersonajeVa= "nombrePersonaje"
        sceneObjectTypeVa = "sceneObjectType"
        
        for va in [nombrePersonajeVa,sceneObjectTypeVa]:
            mc.addAttr(self.baseGrp, ln=va, dt="string")
            
        mc.setAttr(self.baseGrp + "."+nombrePersonajeVa,nombrePersonaje,type ="string", l=1)#l=1 look
        mc.setAttr(self.baseGrp + "."+sceneObjectTypeVa,sceneObjectType,type="string",l=1)
        
        
        #controles visuales del root "agregar parametro a control"
        
        root_Ctl = control.Control(prefix ="root",scale=scale,parent=self.rigGrp)
        
        translate_Ctl = control.Control(prefix ="global",scale=scale,parent=root_Ctl.Co)
       
        #carpetas restantes
        
        self.jointsGrp =mc.group(n="joints_grp",em=True, p=translate_Ctl.Co)
        self.modulosGrp= mc.group(n="modulo_grp",em=1, p=translate_Ctl.Co)
        
        self.limbsGrp= mc.group(n="limbs_grp",em=True,p=self.rigGrp)
        mc.setAttr(self.limbsGrp + ".it", 0, l=1)
        
        
    