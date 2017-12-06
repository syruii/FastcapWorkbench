import FreeCAD, FreeCADGui
import os
from Fastcap_dummy import path_icons

class exportMeshCmd:
    def Activated(self):
        FreeCAD.Console.PrintMessage('Hello, World!')
    def GetResources(self):
        return {'Pixmap': os.path.join(path_icons, 'exportMeshIcon.png'), 'MenuText': 'Export mesh as qui', 'ToolTip': 'Exports the currently selected mesh to a fastcap compatible qui file'}

FreeCADGui.addCommand('exportMesh_Cmd', exportMeshCmd())

# Todo: add the actual command, and add dialog boxes to select options