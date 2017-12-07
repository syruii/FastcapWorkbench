import FreeCAD, FreeCADGui
import os
from Fastcap_dummy import path_icons
import showNormalsWidget #todo

class showNormalsCmd:
    def Activated(self):
        newDialog = showNormalsWidget.normal()
    def GetResources(self):
        return {'Pixmap': os.path.join(path_icons, 'showNormalsIcon.png'), 'MenuText': 'Show surface normals to mesh', 'ToolTip': 'Generates a new object containing the surface normal of every panel in the currently selected mesh. Use before defining inperm and outperm when exporting'}

FreeCADGui.addCommand('showNormals_Cmd', showNormalsCmd())
