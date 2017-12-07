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
            openNames = QFileDialog.getOpenFileNames(None, QString.fromLocal8Bit("Open a file qui"), path, "*.qui")
        except Exception:
            openNames, _ = PySide.QtGui.QFileDialog.getOpenFileNames(None, "Open a file text", path, "*.qui")
        
        if not openNames:
            FreeCAD.Console.PrintMessage("No files selected\n")
        else:
            for openName in openNames:
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
                            m.addFacet(*[float(x) for x in tokens[2:11]])
                            if line.startswith('Q'):
                                # add the second triangle of the quadrilateral
                                secondTriangle = tokens[2:5] + tokens[8:]
                                m.addFacet(*[float(x) for x in secondTriangle])
                        me = doc.addObject("Mesh::Feature", os.path.basename(openName)[:-3])
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
