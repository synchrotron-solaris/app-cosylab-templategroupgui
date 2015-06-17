
from PyQt4 import QtGui
from TemplateGroup import Ui_MainWindow

# Returns QDialog
def getGuiWidget(argv):

    gui_groups = {}
    additional_configuration = None
    title = None
    for i in range(0,len(argv)):

        # READ GROUP NAME FROM CONF
        if "--" in argv[i] and ":" in argv[i]:
            [groupName, elementName] = argv[i][2:].split(":")
            if groupName.upper() in gui_groups.keys():
                gui_groups[groupName.upper()].append([elementName, argv[i+1], argv[i+2]])
            else:
                gui_groups[groupName.upper()] = [[elementName, argv[i+1], argv[i+2]]]

        # PREDEFINED GROUP NAME (--IPC -> group name = "ION PUMPS" ...)
        elif "--ID1" in argv[i]:
            if "ELEMENTS1" in gui_groups.keys():
                gui_groups["ELEMENTS1"].append([argv[i], argv[i+1], argv[i+2]])
            else:
                gui_groups["ELEMENTS1"] = [[argv[i], argv[i+1], argv[i+2]]]

            i += 2

        # PREDEFINED GROUP NAME ...
        elif "--ID2" in argv[i]:
            if "ELEMENTS2" in gui_groups.keys():
                gui_groups["ELEMENTS2"].append([argv[i], argv[i+1], argv[i+2]])
            else:
                gui_groups["ELEMENTS2"] = [[argv[i], argv[i+1], argv[i+2]]]
            i += 2

        #elif "--ID3" in argv[i]:
        #    if "ELEMENTS3" in gui_groups.keys():
        #        gui_groups["ELEMENTS3"].append([argv[i], argv[i+1], argv[i+2]])
        #    else:
        #        gui_groups["ELEMENTS3"] = [[argv[i], argv[i+1], argv[i+2]]]
        #    i += 2
        # ..

        # TITLE/LABEL
        elif "--LAB" in argv[i]:
            title = argv[i+1]
            i += 1

        # ADDITIONAL INFO FROM GROUP CONFIGURATION
        elif "--ADD" in argv[i]:
            additional_configuration = argv[i+1].replace("\r","").split("\n")
            i += 1



    MainWindow = QtGui.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, gui_groups, additional_configuration)
    if title:
        MainWindow.setWindowTitle(title)

    MainWindow.ui = ui #To keep UI in memory
    return MainWindow