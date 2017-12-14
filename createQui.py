import random, os
import FreeCAD, FreeCADGui, Mesh, Part, MeshPart
from FreeCAD import Vector

DEF_FOLDER = "."

def export_mesh(filename, meshobj=None, isDiel=False, folder=DEF_FOLDER, groupName=None):
   
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
        if groupName is None:
            condName = meshobj.Label.replace(" ","_")
        else:
            condName = groupName
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


