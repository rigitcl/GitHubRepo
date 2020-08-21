"""conloles y modulos"""
import maya.cmds as mc

class Control():
    """control para personaje"""
    def __init__(self, prefix="nuevo",
                 scale=1.0,
                 traslateTo="",
                 rotateTo="",
                 parent="",
                 lockChannels=["s","v"]
                 ):
        controlObjeto = mc.circle(n=prefix + "_ctl",ch=False,normal=[1,0,0],radius = scale)[0]
        controlOffset = mc.group ( n= prefix + "offset_grp", em= 1)
        mc.parent(controlObjeto,controlOffset)
        
        #translacion de control
        
        if mc.objExists(traslateTo):
            mc.delete(mc.pointContraint(traslateTo,controlOffset))
            
        if mc.objExists(rotateTo):
            mc.orientContraint((rotateTo,controlOffset))
            
        if mc.objExists(parent):
            mc.parent(controlOffset, parent)
            
        #color controles
        
        controlShape = mc.listRelatives(controlObjeto, s=1)[0]
        mc.setAttr(controlShape + ".ove",1)
        
        if prefix.startswith("l_"):
            mc.setAttr(controlShape + ".ovc",15)
        elif prefix.startswith("r_"):
            mc.setAttr(controlShape + ".ovc",4)
        else:
            mc.setAttr(controlShape + ".ovc", 16)
            
        #instancias publicas
        
        self.Off=controlOffset
        self.Co=controlObjeto
        
            
        
        
        
            
        
        
        
        
        
            
        
        
        