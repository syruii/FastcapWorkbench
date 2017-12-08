import FreeCAD, FreeCADGui
import os
from Fastcap_dummy import path_icons
from exportMeshWidget import Ui_Dialog()


class exportMeshCmd:
    def Activated(self):
        # attempt to open project name lst file
        path = os.path.dirname(FreeCAD.ActiveDocument.FileName)
        name = FreeCAD.ActiveDocument.Name
        sel = FreeCADGui.Selection.getSelection()
        if not sel:
            FreeCAD.Console.PrintMessage("Error: no meshes selected\n")
            return
        lstFile = os.path.join(path,name + ".lst")
        try:
            with open(lstFile, "a+") as file:
                try:
                    # add ui later to specify name, but currently just get name of first
                    # selected object
                    groupname = sel[0].Name
                    file.write("G " + groupName + "\n")
                    for obj in sel:
                        d = QtGui.QWidget()
                        ui = Ui_Dialog()
                        ui.setupUi(self.d, obj.Name)
                        d.show()
                        if d.exec_():
                            print(d.isConductor)
                except Exception, e:
                    FreeCAD.Console.PrintError("Error in generating the mesh or writing to the file: " + str(e))
                finally:
                    file.close()
        except Exception:
            FreeCAD.Console.PrintError("Error in opening the file " + lstFile + "\n")
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
