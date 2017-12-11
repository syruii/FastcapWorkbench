import FreeCAD, FreeCADGui
import os
from Fastcap_dummy import path_icons
from exportMeshWidget import Ui_Dialog
from createQui import export_mesh

class exportCondMeshCmd:
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
                    file.write("G " + groupname + "\n")
                    for i, obj in enumerate(sel):
                        if obj == None:
                            return
                        elif obj.TypeId != "Mesh::Feature":
                            FreeCAD.Console.PrintError("Error: '" + obj.Name + "' is not an object of type 'Mesh::Feature'\n")
                            continue

                        dialog = Ui_Dialog(obj.Name)
                        if dialog.exec_():
                            if i > 0:
                                # if not the first line, append the '+' to the previous conductor definition
                                file.write(" +\n")
                            
                            # write the C objName.qui <perm> <perm?> <transpose> by reading from dialog
                            #if dialog.isConductor == True:
                            _ = export_mesh(obj.Name, obj, False, path)
                            file.write("C " + obj.Name + ".qui " + str(dialog.surroundingperm) + " 0 0 0")
                            #else:
                            #    reference = export_mesh(obj.Name, obj, True, path)
                            #    file.write("D " + obj.Name + ".qui " + str(dialog.outperm))
                            #    file.write(" " + str(dialog.inperm) + " 0 0 0 " + " ".join(map(str, reference)))
                    # finish the last line
                    file.write("\n")
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
        return {'Pixmap': os.path.join(path_icons, 'exportCondMeshIcon.png'), 'MenuText': 'Export mesh as qui', 'ToolTip': 'Exports the currently selected mesh(es) to a fastcap compatible qui file as a conductor'}

FreeCADGui.addCommand('exportCondMesh_Cmd', exportCondMeshCmd())

# Todo: add the actual command, and add dialog boxes to select options
# Todo: the function should be able to take in a multiple selection of meshes and output to a single qui file
# for completeness sake
