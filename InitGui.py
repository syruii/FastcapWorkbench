
class FastCapWorkBench(Workbench):
    MenuText = "Fastcap Workbench"
    ToolTip = "Contains tool to process meshes for input into Fastcap"
    Icon = FreeCAD.getUserAppDataDir()+"Mod" + "/Fastcap/icons/fastcapWorkbenchIcon.png"

    def Initialize(self):
        "This function is executed when FreeCAD starts"
        import exportCondMesh, exportDielectricMesh, importMesh, showNormals # import here all the needed files that create your FreeCAD commands
        self.list = ["exportCondMesh_Cmd", "exportDielectricMesh_Cmd", "importMesh_Cmd", "showNormals_Cmd"]  # A list of command names created in the line above
        self.appendToolbar("My Commands", self.list)  # creates a new toolbar with your commands
        #self.appendMenu("My New Menu", self.list)  # creates a new menu
        #self.appendMenu(["An existing Menu", "My submenu"], self.list)  # appends a submenu to an existing menu

    #def Activated(self):
    #    "This function is executed when the workbench is activated"
    #    return

    #def Deactivated(self):
    #    "This function is executed when the workbench is deactivated"
    #    return

    def ContextMenu(self, recipient):
    #    "This is executed whenever the user right-clicks on screen"
    #    # "recipient" will be either "view" or "tree"
        self.appendContextMenu("My commands", self.list)  # add commands to the context menu

    def GetClassName(self):
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"


Gui.addWorkbench(FastCapWorkBench())
