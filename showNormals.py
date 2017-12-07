import FreeCAD, FreeCADGui, Mesh, Part, MeshPart, DraftGeomUtils
from FreeCAD import Vector
import os
from Fastcap_dummy import path_icons

class showNormalsCmd:
    def make_arrow__(self, startpoint, endpoint):
        '''create an arrow

        'startpoint' is a Vector specifying the start position
        'endpoint' is a Vector specifying the end position
        '''

        line = Part.makeLine(startpoint, endpoint)
        # calculate arrow head base
        dir = endpoint - startpoint
        len = dir.Length
        base = dir
        base.normalize()
        base.multiply(len * 0.8)
        base = startpoint + base
        # radius2 is calculated for a fixed arrow head angle tan(15deg)=0.27
        cone = Part.makeCone(0.2 * len * 0.27, 0.0, 0.2 * len, base, dir, 360)

        # add the compound representing the arrow
        arrow = Part.makeCompound([line, cone])

        return arrow
    def Activated(self):
        sel = FreeCADGui.Selection.getSelection()
        if not sel:
            FreeCAD.Console.PrintMessage("Error: no meshes selected\n")
            return
        for obj in FreeCADGui.Selection.getSelection():
            if "Mesh" not in obj.PropertiesList:
                FreeCAD.Console.PrintMessage("Error: " + obj.Name + " is not an object of type 'Mesh::Feature'\n")
                continue
            # export facets
            arrows = []
            condName = obj.Label.replace(" ", "_")
            for facet in obj.Mesh.Facets:
                center = Vector(0.0, 0.0, 0.0)
                avgSideLen = 0.0
                for j, point in enumerate(facet.Points):
                            # 'point' is a tuple, transform in vector
                            center = center + Vector(point)
                            # get side length
                            side = Vector(facet.Points[(j + 1) % 3]) - Vector(point)
                            avgSideLen += side.Length
                            # calculate the reference point
                            # (there should be a better way to divide a vector by a scalar..)
                center.multiply(1.0 / len(facet.Points))
                            # and now move along the normal, proportional to the average facet dimension
                scaledNormal = Vector(facet.Normal)
                scaledNormal.multiply(avgSideLen / len(facet.Points))
                refpoint = center + scaledNormal
                arrows.append(self.make_arrow__(center, refpoint))
            # add the vector normals visualization to the view
            # Note: could also use Part.show(normals) but in this case we could
            # not give the (permanent) name to the object, only change the label afterwards
            normals = Part.makeCompound(arrows)
            normalobj = FreeCAD.ActiveDocument.addObject("Part::Feature", obj.Name + "_normals")
            normalobj.Shape = normals
    def GetResources(self):
        return {'Pixmap': os.path.join(path_icons, 'showNormalsIcon.png'), 'MenuText': 'Show surface normals to mesh', 'ToolTip': 'Generates a new object containing the surface normal of every panel in the currently selected mesh. Use before defining inperm and outperm when exporting'}


FreeCADGui.addCommand('showNormals_Cmd', showNormalsCmd())
