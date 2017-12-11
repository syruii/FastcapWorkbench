import FreeCAD, FreeCADGui, Mesh, Part, MeshPart
import os
from Fastcap_dummy import path_icons
from exportMeshWidget import Ui_Dialog
import random
from FreeCAD import Vector

DEF_FOLDER = "."

def export_mesh(filename, meshobj=None, isDiel=False, folder=DEF_FOLDER):
   
    # check input in caller
    
    # add qui extension
    filename = filename + ".qui"
    
    if not os.path.isdir(folder):
        os.mkdir(folder)

    with open(os.path.join(folder, filename), 'w') as fid:
        if isDiel == True:
            fid.write("0 dielectric definition file for mesh '" + meshobj.Label)
        else:
            fid.write("0 conductor definition file for mesh '" + meshobj.Label)
        fid.write("' created using FreeCAD's Electromagnetic workbench script\n")
        fid.write("\n")
        
        # export faces
        # for dielectric, right now, assumes that any old normal surface vector can be chosen
        # as the reference vector, should be more mathematically rigorous than that
        refvectors = []
        condName = meshobj.Label.replace(" ","_")
        for facet in meshobj.Mesh.Facets:
            if len(facet.Points) == 3:
                fid.write("T " + condName)
            elif len(facet.Points) == 4:
                fid.write("Q " + condName)
            else:
                FreeCAD.Console.PrintError("Error: Unforseen number of mesh facet points: " + len(facet.Points) + ", skipping facet\n")
                continue
            center = Vector(0.0, 0.0, 0.0)
            avgSideLen = 0.0
            for j, point in enumerate(facet.Points):
                fid.write(" ")
                fid.write(" ".join(map(str,point)))
                if isDiel == True:
                    for i in range(3):
                        center = center + Vector(point)
                        side = Vector(facet.Points[(j+1)%3]) - Vector(point)
                        avgSideLen += side.Length
                    center.multiply(1.0 / len(facet.Points))
                    scaledNormal = Vector(facet.Normal)
                    scaledNormal.multiply(avgSideLen / len(facet.Points))
                    refpoint = center + scaledNormal
                    refvectors.append((refpoint.x, refpoint.y, refpoint.z))
            fid.write("\n")
        fid.close

        if isDiel == True:
            return random.choice(refvectors)
        else:
            return None


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
                            if dialog.isConductor == True:
                                _ = export_mesh(obj.Name, obj, False, path)
                                file.write("C " + obj.Name + ".qui " + str(dialog.surroundingperm) + " 0 0 0")
                            else:
                                reference = export_mesh(obj.Name, obj, True, path)
                                file.write("D " + obj.Name + ".qui " + str(dialog.outperm))
                                file.write(" " + str(dialog.inperm) + " 0 0 0 " + " ".join(map(str, reference)))
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
        return {'Pixmap': os.path.join(path_icons, 'exportMeshIcon.png'), 'MenuText': 'Export mesh as qui', 'ToolTip': 'Exports the currently selected mesh to a fastcap compatible qui file'}

FreeCADGui.addCommand('exportMesh_Cmd', exportMeshCmd())

# Todo: add the actual command, and add dialog boxes to select options
# Todo: the function should be able to take in a multiple selection of meshes and output to a single qui file
# for completeness sake
