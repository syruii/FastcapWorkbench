import FreeCAD, FreeCADGui
import os
from Fastcap_dummy import path_icons
import exportMeshWidget #todo

class exportMeshCmd:
    def Activated(self):
        newDialog = exportMeshWidget.meshCreator()
        # see https://freecadweb.org/wiki/Dialog_creation
        # dialog = QtGui.QFileDialog(
        #   QtGui.qApp.activeWindow(),
        #   "Select document to import from
        #   )
        # dialog.setNameFilter("Support formats")
        # if dialog.exec_():
        #   filename = dialog.selectedFiles()[0]
        # else:
        #   return
        # writing file subheading for writing list file
        # write function that appends appropriately
    def GetResources(self):
        return {'Pixmap': os.path.join(path_icons, 'exportMeshIcon.png'), 'MenuText': 'Export mesh as qui', 'ToolTip': 'Exports the currently selected mesh to a fastcap compatible qui file'}

FreeCADGui.addCommand('exportMesh_Cmd', exportMeshCmd())

# Todo: add the actual command, and add dialog boxes to select options
# Todo: the function should be able to take in a multiple selection of meshes and output to a single qui file
# for completeness sake
