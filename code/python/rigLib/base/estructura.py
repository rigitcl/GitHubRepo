import maya.cmds as mc
tipoObjeto = "rig"
from . import control
class Root():
    """
    base para construir la estructura
    """
    
    def __init__(self, nombrePersonaje="nuevo",scale=1.0):
        
        self.baseGrp = mc.group(n=nombrePersonaje + "_rig_grp",em=1)
        self.rigGrp = mc.group(n="rig_grp",em=True,p =self.baseGrp)
        self.meshGrp = mc.group(n="geo_grp",em=1,p = self.baseGrp)
        
        nombrePersonajeVa ="nombrePersonaje"
        tipoObjetoVa ="tipoObjeto"
        
        for va in[nombrePersonajeVa, tipoObjetoVa]:
            mc.addAttr(self.baseGrp, ln=va, dt="string")
            
        mc.setAttr(self.baseGrp + "."+ nombrePersonajeVa,nombrePersonaje,type="string",l=1)
        mc.setAttr(self.baseGrp + "."+ tipoObjetoVa,tipoObjeto,type="string",l=1)
        
        #controles para viewport
        
        root_Ctl=control.Control(prefix="root",scale=scale*15,parent=self.rigGrp)
        traslacion_Ctl=control.Control(prefix="global",scale=scale*13,parent=root_Ctl.Co)
        
        
        #carpetas restantes
        
        self.jointsGrp = mc.group(n="joint_grp" ,em=1,p=traslacion_Ctl.Co)
        self.modulosGrp = mc.group(n="modulo_grp",em=True,p=traslacion_Ctl.Co)
        
        self.limbsGrp = mc.group(n="limbs_grp",em=True,p=self.rigGrp)
        mc.setAttr(self.limbsGrp + ".it",0,l=True)
        
        #rotar shape
        self._OrientacionControlShape(root_Ctl.Co)
        self._OrientacionControlShape(traslacion_Ctl.Co)
        
        for axis in["y","z"]:
            mc.connectAttr(root_Ctl.Co + ".sx",root_Ctl.Co + ".s" +axis)
            mc.setAttr(root_Ctl.Co+".s"+ axis,k=0)
            
    def _OrientacionControlShape(self,controlObjeto):
        #orientacion del shape
        ctlShape=mc.listRelatives(controlObjeto,s=1,type="nurbsCurve")
        cls=mc.cluster(ctlShape)[1]
        mc.setAttr(cls+".rz",90)
        mc.delete(ctlShape,ch=1)
        
class Modulo():
    """
    Modulo de la estructura
    """
    def __init__(self,prefix="nuevo",baseObjeto=None):
        """
        @param: prefix: str:prefijo para nombrar nuevo objeto
        """
        
        self.topGrp=mc.group(n=prefix +"Modulo_grp",em=1)
        self.controlsGrp=mc.group(n=prefix + "Control_grp",em=1,p=self.topGrp)
        self.partesGrp=mc.group(n=prefix + "Partes_grp",em=1,p=self.topGrp)
        self.HoldGrp=mc.group(n=prefix + "Hold_grp",em=1,p=self.topGrp)
        
        mc.setAttr(self.holdGrp+"it",0,l=True)
        
        #parent modulo
        if baseObjeto:
            mc.parent(self.topGrp,baseObjeto.modulosGrp)

        
            
        
        
            
        