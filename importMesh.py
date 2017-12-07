import FreeCAD, FreeCADGui
from Fastcap_dummy import path_icons
import PySide
from PySide import QtGui, QtCore
from PySide.QtGui import *
from PySide.QtCore import *
import Mesh
import os

path = FreeCAD.ConfigGet("UserAppData")

class importMeshCmd:
    def Activated(self):
        FreeCAD.Console.PrintMessage('Importing mesh')
        try:
            openName = QFileDialog.getOpenFileName(None, QString.fromLocal8Bit("Open a file qui"), path, "*.qui")
        except Exception:
            openName, _ = PySide.QtGui.QFileDialog.getOpenFileName(None, "Open a file text", path, "*.qui")
        
        if openName == "":
            FreeCAD.Console.PrintMessage("No file selected\n")
        else:
            FreeCAD.Console.PrintMessage("Reading from " + openName + "\n")
            try:
                file = open(openName, "r")
                try:
                    doc = FreeCAD.activeDocument()
                    if doc is None:
                        raise RuntimeError('No active document')
                    m = Mesh.Mesh()
                    lines = file.readlines()
                    lines = [x for x in lines if x.startswith('Q') or x.startswith('T')]
                    #if you don't split via commented lines, the meshes may contain more than one component
                    for line in lines:
                        tokens = list(filter(None, line.split()))
                        m.addFacet(*tokens[2:11])
                        if line.startswith('Q'):
                            # add the second triangle of the quadrilateral
                            m.addFacet(*tokens[5:14])
                    me = doc.addObject("Mesh::Feature", openName[:-3])
                    me.Mesh = m
                    doc.recompute()
                except Exception, e:
                    FreeCAD.Console.PrintError("Error parsing the qui file: " + str(e))
                finally:
                    file.close()
            except Exception:
                FreeCAD.Console.PrintError("Error in opening the file " + openName + "\n")
    def GetResources(self):
        return {'Pixmap': os.path.join(path_icons, 'importMeshIcon.png'), 'MenuText': 'Import qui as a mesh', 'ToolTip': 'Imports the selected qui file as a triangular mesh object'}

FreeCADGui.addCommand('importMesh_Cmd', importMeshCmd())
