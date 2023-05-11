# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision D, 05/10/2023

Verified working on: Python 2.7, 3.8 for Windows 8.1, 10 64-bit and Raspberry Pi Buster (does not work on Mac).
'''

__author__ = 'reuben.brewer'

#########################################################
from ZeroAndSnapshotData_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *
from MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class import *
#########################################################

#########################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
#########################################################

#########################################################
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
#########################################################

#########################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
#########################################################

###########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def TellWhichFileWereIn():

    #We used to use this method, but it gave us the root calling file, not the class calling file
    #absolute_file_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    #filename = absolute_file_path[absolute_file_path.rfind("\\") + 1:]

    frame = inspect.stack()[1]
    filename = frame[1][frame[1].rfind("\\") + 1:]
    filename = filename.replace(".py","")

    return filename
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def IsInputList(input, print_result_flag = 0):

    result = isinstance(input, list)

    if print_result_flag == 1:
        print("IsInputList: " + str(result))

    return result
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
def ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(input, number_of_leading_numbers = 4, number_of_decimal_places = 3):

    number_of_decimal_places = max(1, number_of_decimal_places) #Make sure we're above 1

    ListOfStringsToJoin = []

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if isinstance(input, str) == 1:
        ListOfStringsToJoin.append(input)
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    elif isinstance(input, int) == 1 or isinstance(input, float) == 1:
        element = float(input)
        prefix_string = "{:." + str(number_of_decimal_places) + "f}"
        element_as_string = prefix_string.format(element)

        ##########################################################################################################
        ##########################################################################################################
        if element >= 0:
            element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1)  # +1 for sign, +1 for decimal place
            element_as_string = "+" + element_as_string  # So that our strings always have either + or - signs to maintain the same string length
        else:
            element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1 + 1)  # +1 for sign, +1 for decimal place
        ##########################################################################################################
        ##########################################################################################################

        ListOfStringsToJoin.append(element_as_string)
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    elif isinstance(input, list) == 1:

        if len(input) > 0:
            for element in input: #RECURSION
                ListOfStringsToJoin.append(ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

        else: #Situation when we get a list() or []
            ListOfStringsToJoin.append(str(input))

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    elif isinstance(input, tuple) == 1:

        if len(input) > 0:
            for element in input: #RECURSION
                ListOfStringsToJoin.append("TUPLE" + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

        else: #Situation when we get a list() or []
            ListOfStringsToJoin.append(str(input))

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    elif isinstance(input, dict) == 1:

        if len(input) > 0:
            for Key in input: #RECURSION
                ListOfStringsToJoin.append(str(Key) + ": " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(input[Key], number_of_leading_numbers, number_of_decimal_places))

        else: #Situation when we get a dict()
            ListOfStringsToJoin.append(str(input))

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    else:
        ListOfStringsToJoin.append(str(input))
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if len(ListOfStringsToJoin) > 1:

        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        StringToReturn = ""
        for Index, StringToProcess in enumerate(ListOfStringsToJoin):

            ################################################
            if Index == 0: #The first element
                if StringToProcess.find(":") != -1 and StringToProcess[0] != "{": #meaning that we're processing a dict()
                    StringToReturn = "{"
                elif StringToProcess.find("TUPLE") != -1 and StringToProcess[0] != "(":  # meaning that we're processing a tuple
                    StringToReturn = "("
                else:
                    StringToReturn = "["

                StringToReturn = StringToReturn + StringToProcess.replace("TUPLE","") + ", "
            ################################################

            ################################################
            elif Index < len(ListOfStringsToJoin) - 1: #The middle elements
                StringToReturn = StringToReturn + StringToProcess + ", "
            ################################################

            ################################################
            else: #The last element
                StringToReturn = StringToReturn + StringToProcess

                if StringToProcess.find(":") != -1 and StringToProcess[-1] != "}":  # meaning that we're processing a dict()
                    StringToReturn = StringToReturn + "}"
                elif StringToProcess.find("TUPLE") != -1 and StringToProcess[-1] != ")":  # meaning that we're processing a tuple
                    StringToReturn = StringToReturn + ")"
                else:
                    StringToReturn = StringToReturn + "]"

            ################################################

        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

    elif len(ListOfStringsToJoin) == 1:
        StringToReturn = ListOfStringsToJoin[0]

    else:
        StringToReturn = ListOfStringsToJoin

    return StringToReturn
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ConvertDictToProperlyFormattedStringForPrinting(DictToPrint, NumberOfDecimalsPlaceToUse = 3, NumberOfEntriesPerLine = 1, NumberOfTabsBetweenItems = 3):

    ProperlyFormattedStringForPrinting = ""
    ItemsPerLineCounter = 0

    for Key in DictToPrint:

        if isinstance(DictToPrint[Key], dict): #RECURSION
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                 Key + ":\n" + \
                                                 ConvertDictToProperlyFormattedStringForPrinting(DictToPrint[Key], NumberOfDecimalsPlaceToUse, NumberOfEntriesPerLine, NumberOfTabsBetweenItems)

        else:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                 Key + ": " + \
                                                 ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(DictToPrint[Key], 0, NumberOfDecimalsPlaceToUse)

        if ItemsPerLineCounter < NumberOfEntriesPerLine - 1:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\t"*NumberOfTabsBetweenItems
            ItemsPerLineCounter = ItemsPerLineCounter + 1
        else:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\n"
            ItemsPerLineCounter = 0

    return ProperlyFormattedStringForPrinting
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG
    global DebuggingInfo_Label

    global ZeroAndSnapshotData_ReubenPython2and3ClassObject
    global ZeroAndSnapshotData_OPEN_FLAG
    global SHOW_IN_GUI_ZeroAndSnapshotData_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MYPRINT_OPEN_FLAG
    global SHOW_IN_GUI_MYPRINT_FLAG

    global ZeroAndSnapshotData_MostRecentDict

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            DebuggingInfo_Label["text"] = ConvertDictToProperlyFormattedStringForPrinting(ZeroAndSnapshotData_MostRecentDict, NumberOfDecimalsPlaceToUse = 3, NumberOfEntriesPerLine = 1, NumberOfTabsBetweenItems = 3)
            #########################################################

            #########################################################
            if ZeroAndSnapshotData_OPEN_FLAG == 1 and SHOW_IN_GUI_ZeroAndSnapshotData_FLAG == 1:
                ZeroAndSnapshotData_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            #########################################################
            if MYPRINT_OPEN_FLAG == 1 and SHOW_IN_GUI_MYPRINT_FLAG == 1:
                MyPrint_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback():
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_TABS_IN_GUI_FLAG
    global DebuggingInfo_Label
    global TestButton

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
    #################################################
    #################################################

    #################################################
    #################################################
    global TabControlObject
    global Tab_MainControls
    global Tab_ZeroAndSnapshotData
    global Tab_MyPrint

    if USE_TABS_IN_GUI_FLAG == 1:
        #################################################
        TabControlObject = ttk.Notebook(root)

        Tab_ZeroAndSnapshotData = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_ZeroAndSnapshotData, text='   ZeroAndSnapshotData   ')

        Tab_MainControls = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MainControls, text='   Main Controls   ')

        Tab_MyPrint = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MyPrint, text='   MyPrint Terminal   ')

        TabControlObject.pack(expand=1, fill="both")  # CANNOT MIX PACK AND GRID IN THE SAME FRAME/TAB, SO ALL .GRID'S MUST BE CONTAINED WITHIN THEIR OWN FRAME/TAB.

        ############# #Set the tab header font
        TabStyle = ttk.Style()
        TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        #############
        #################################################
    else:
        #################################################
        Tab_MainControls = root
        Tab_ZeroAndSnapshotData = root
        Tab_MyPrint = root
        #################################################

    #################################################
    #################################################

    #################################################
    DebuggingInfo_Label = Label(Tab_MainControls, text="Device Info", width=120, font=("Helvetica", 10))
    DebuggingInfo_Label.grid(row=1, column=0, padx=1, pady=1, columnspan=10, rowspan=1)
    #################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_ZeroAndSnapshotData_ReubenPython2and3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    #################################################
    #################################################
    global my_platform

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)
    #################################################
    #################################################

    #################################################
    #################################################
    global USE_ZeroAndSnapshotData_FLAG
    USE_ZeroAndSnapshotData_FLAG = 1

    global USE_MYPRINT_FLAG
    USE_MYPRINT_FLAG = 1

    global USE_PLOTTER_FLAG
    USE_PLOTTER_FLAG = 1

    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_TABS_IN_GUI_FLAG
    USE_TABS_IN_GUI_FLAG = 1

    global USE_SINUSOIDAL_INPUT_FLAG
    USE_SINUSOIDAL_INPUT_FLAG = 0

    global USE_SPECKLE_NOISE_FLAG
    USE_SPECKLE_NOISE_FLAG = 1

    global USE_PrintMostRecentDictForDebuggingFlag
    USE_PrintMostRecentDictForDebuggingFlag = 0
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_ZeroAndSnapshotData_FLAG
    SHOW_IN_GUI_ZeroAndSnapshotData_FLAG = 1

    global SHOW_IN_GUI_MYPRINT_FLAG
    SHOW_IN_GUI_MYPRINT_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_ZeroAndSnapshotData
    global GUI_COLUMN_ZeroAndSnapshotData
    global GUI_PADX_ZeroAndSnapshotData
    global GUI_PADY_ZeroAndSnapshotData
    global GUI_ROWSPAN_ZeroAndSnapshotData
    global GUI_COLUMNSPAN_ZeroAndSnapshotData
    GUI_ROW_ZeroAndSnapshotData = 1

    GUI_COLUMN_ZeroAndSnapshotData = 0
    GUI_PADX_ZeroAndSnapshotData = 1
    GUI_PADY_ZeroAndSnapshotData = 1
    GUI_ROWSPAN_ZeroAndSnapshotData = 1
    GUI_COLUMNSPAN_ZeroAndSnapshotData = 1

    global GUI_ROW_MYPRINT
    global GUI_COLUMN_MYPRINT
    global GUI_PADX_MYPRINT
    global GUI_PADY_MYPRINT
    global GUI_ROWSPAN_MYPRINT
    global GUI_COLUMNSPAN_MYPRINT
    GUI_ROW_MYPRINT = 2

    GUI_COLUMN_MYPRINT = 0
    GUI_PADX_MYPRINT = 1
    GUI_PADY_MYPRINT = 1
    GUI_ROWSPAN_MYPRINT = 1
    GUI_COLUMNSPAN_MYPRINT = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global LastTime_MainLoopThread_PLOTTER
    LastTime_MainLoopThread_PLOTTER = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -11111.0

    global root

    global root_Xpos
    root_Xpos = 900

    global root_Ypos
    root_Ypos = 0

    global root_width
    root_width = 1920 - root_Xpos

    global root_height
    root_height = 1020 - root_Ypos

    global TabControlObject
    global Tab_MainControls
    global Tab_ZeroAndSnapshotData
    global Tab_MyPrint

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30

    global SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle
    SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle = 1.0

    global SINUSOIDAL_MOTION_INPUT_MinValue
    SINUSOIDAL_MOTION_INPUT_MinValue = -1.0

    global SINUSOIDAL_MOTION_INPUT_MaxValue
    SINUSOIDAL_MOTION_INPUT_MaxValue = 1.0

    global NoiseCounter
    NoiseCounter = 0

    global NoiseAmplitude_Percent0to1OfSinuisoidalInputAmplitude
    NoiseAmplitude_Percent0to1OfSinuisoidalInputAmplitude = 0.05
    #################################################
    #################################################

    #################################################
    #################################################
    global ZeroAndSnapshotData_ReubenPython2and3ClassObject

    global ZeroAndSnapshotData_OPEN_FLAG
    ZeroAndSnapshotData_OPEN_FLAG = -1

    global ZeroAndSnapshotData_MostRecentDict
    ZeroAndSnapshotData_MostRecentDict = dict()

    global ZeroAndSnapshotData_MostRecentDict_DataUpdateNumber
    ZeroAndSnapshotData_MostRecentDict_DataUpdateNumber = -11111

    global ZeroAndSnapshotData_MostRecentDict_LoopFrequencyHz
    ZeroAndSnapshotData_MostRecentDict_LoopFrequencyHz = -11111

    global ZeroAndSnapshotData_MostRecentDict_OnlyVariablesAndValuesDictOfDicts
    ZeroAndSnapshotData_MostRecentDict_OnlyVariablesAndValuesDictOfDicts = dict()

    global ZeroAndSnapshotData_MostRecentDict_desired_angle_deg_1__Raw_CurrentValue
    ZeroAndSnapshotData_MostRecentDict_desired_angle_deg_1__Raw_CurrentValue = -11111

    global ZeroAndSnapshotData_MostRecentDict_desired_angle_deg_1__Raw_CurrentValue_Zeroed
    ZeroAndSnapshotData_MostRecentDict_desired_angle_deg_1__Raw_CurrentValue_Zeroed = -11111

    global ZeroAndSnapshotData_MostRecentDict_desired_angle_deg_1__Raw_ZeroOffsetValue
    ZeroAndSnapshotData_MostRecentDict_desired_angle_deg_1__Raw_Raw_ZeroOffsetValue = -11111
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_ReubenPython2and3ClassObject

    global MYPRINT_OPEN_FLAG
    MYPRINT_OPEN_FLAG = -1
    #################################################
    #################################################

    ####################################################
    ####################################################
    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject

    global PLOTTER_OPEN_FLAG
    PLOTTER_OPEN_FLAG = -1
    ####################################################
    ####################################################

    #################################################  KEY GUI LINE
    #################################################
    if USE_GUI_FLAG == 1:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread)
        GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        GUI_Thread_ThreadingObject.start()
        time.sleep(0.5)  #Allow enough time for 'root' to be created that we can then pass it into other classes.
    else:
        root = None
        Tab_MainControls = None
        Tab_ZeroAndSnapshotData = None
        Tab_MyPrint = None
    #################################################
    #################################################

    #################################################
    #################################################
    global ZeroAndSnapshotData_ReubenPython2and3ClassObject_Variables_ListOfDicts
    ZeroAndSnapshotData_ReubenPython2and3ClassObject_Variables_ListOfDicts = [dict([("Variable_Name", "desired_angle_deg_1"),("DataCollectionDurationInSecondsForSnapshottingAndZeroing", 5.5)]),
                                                                              dict([("Variable_Name", "B"),("DataCollectionDurationInSecondsForSnapshottingAndZeroing", 7.5)]),
                                                                              dict([("Variable_Name", "C"),("DataCollectionDurationInSecondsForSnapshottingAndZeroing", 9.0)])]


    global ZeroAndSnapshotData_ReubenPython2and3ClassObject_GUIparametersDict
    ZeroAndSnapshotData_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_ZeroAndSnapshotData_FLAG),
                                    ("root", Tab_ZeroAndSnapshotData),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 1),
                                    ("GUI_ROW", GUI_ROW_ZeroAndSnapshotData),
                                    ("GUI_COLUMN", GUI_COLUMN_ZeroAndSnapshotData),
                                    ("GUI_PADX", GUI_PADX_ZeroAndSnapshotData),
                                    ("GUI_PADY", GUI_PADY_ZeroAndSnapshotData),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_ZeroAndSnapshotData),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_ZeroAndSnapshotData)])

    global ZeroAndSnapshotData_ReubenPython2and3ClassObject_setup_dict
    ZeroAndSnapshotData_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", ZeroAndSnapshotData_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                ("NameToDisplay_UserSet", "Reuben's Test ZeroAndSnapshotData"),
                                                                ("Variables_ListOfDicts", ZeroAndSnapshotData_ReubenPython2and3ClassObject_Variables_ListOfDicts)])

    if USE_ZeroAndSnapshotData_FLAG == 1:
        try:
            ZeroAndSnapshotData_ReubenPython2and3ClassObject = ZeroAndSnapshotData_ReubenPython2and3Class(ZeroAndSnapshotData_ReubenPython2and3ClassObject_setup_dict)
            ZeroAndSnapshotData_OPEN_FLAG = ZeroAndSnapshotData_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("ZeroAndSnapshotData_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1:

        MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MYPRINT_FLAG),
                                                                        ("root", Tab_MyPrint),
                                                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                        ("GUI_ROW", GUI_ROW_MYPRINT),
                                                                        ("GUI_COLUMN", GUI_COLUMN_MYPRINT),
                                                                        ("GUI_PADX", GUI_PADX_MYPRINT),
                                                                        ("GUI_PADY", GUI_PADY_MYPRINT),
                                                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MYPRINT),
                                                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MYPRINT)])

        MyPrint_ReubenPython2and3ClassObject_setup_dict = dict([("NumberOfPrintLines", 10),
                                                                ("WidthOfPrintingLabel", 200),
                                                                ("PrintToConsoleFlag", 1),
                                                                ("LogFileNameFullPath", os.getcwd() + "//TestLog.txt"),
                                                                ("GUIparametersDict", MyPrint_ReubenPython2and3ClassObject_GUIparametersDict)])

        try:
            MyPrint_ReubenPython2and3ClassObject = MyPrint_ReubenPython2and3Class(MyPrint_ReubenPython2and3ClassObject_setup_dict)
            MYPRINT_OPEN_FLAG = MyPrint_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPlotterPureTkinter_MostRecentDict
    MyPlotterPureTkinter_MostRecentDict = dict()

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = -1



    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict = dict([("EnableInternal_MyPrint_Flag", 1),
                                                                                                ("NumberOfPrintLines", 10),
                                                                                                ("GraphCanvasWidth", 1280),
                                                                                                ("GraphCanvasHeight", 700),
                                                                                                ("GraphCanvasWindowStartingX", 0),
                                                                                                ("GraphCanvasWindowStartingY", 0),
                                                                                                ("GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents", 20)])

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                                        ("ParentPID", os.getpid()),
                                                                                        ("WatchdogTimerExpirationDurationSeconds_StandAlonePlottingProcess", 5.0),
                                                                                        ("MarkerSize", 3),
                                                                                        ("CurvesToPlotNamesAndColorsDictOfLists", dict([("NameList", ["raw", "zeroed", "offset"]),("ColorList", ["blue", "red", "green"])])),
                                                                                        ("NumberOfDataPointToPlot", 50),
                                                                                        ("XaxisNumberOfTickMarks", 10),
                                                                                        ("YaxisNumberOfTickMarks", 10),
                                                                                        ("XaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("YaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("XaxisAutoscaleFlag", 1),
                                                                                        ("YaxisAutoscaleFlag", 1),
                                                                                        ("X_min", 0.0),
                                                                                        ("X_max", 20.0),
                                                                                        ("Y_min", 1.1*SINUSOIDAL_MOTION_INPUT_MinValue),
                                                                                        ("Y_max", 1.1*SINUSOIDAL_MOTION_INPUT_MaxValue),
                                                                                        ("XaxisDrawnAtBottomOfGraph", 0),
                                                                                        ("XaxisLabelString", "Time (sec)"),
                                                                                        ("YaxisLabelString", "Y-units (units)"),
                                                                                        ("ShowLegendFlag", 1)])

    if USE_PLOTTER_FLAG == 1:
        try:
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class(MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict)
            time.sleep(0.25)
            PLOTTER_OPEN_FLAG = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject, exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_ZeroAndSnapshotData_FLAG == 1 and ZeroAndSnapshotData_OPEN_FLAG != 1:
        print("Failed to open ZeroAndSnapshotData_ReubenPython2and3Class.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1 and MYPRINT_OPEN_FLAG != 1:
        print("Failed to open MyPrint_ReubenPython2and3ClassObject.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_PLOTTER_FLAG == 1 and PLOTTER_OPEN_FLAG != 1:
        print("Failed to open MyPlotterPureTkinterClass_Object.")
        ExitProgram_Callback()
    #################################################
    #################################################

    ####################################################
    ####################################################
    random.seed()
    ####################################################
    ####################################################

    #################################################
    #################################################
    print("Starting main loop 'test_program_for_ZeroAndSnapshotData_ReubenPython2and3Class.")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0):

        ###################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ###################################################

        ################################################### GET's
        ###################################################
        if ZeroAndSnapshotData_OPEN_FLAG == 1:

            ZeroAndSnapshotData_MostRecentDict = ZeroAndSnapshotData_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "DataUpdateNumber" in ZeroAndSnapshotData_MostRecentDict:
                ZeroAndSnapshotData_MostRecentDict_DataUpdateNumber = ZeroAndSnapshotData_MostRecentDict["DataUpdateNumber"]
                ZeroAndSnapshotData_MostRecentDict_LoopFrequencyHz = ZeroAndSnapshotData_MostRecentDict["LoopFrequencyHz"]
                ZeroAndSnapshotData_MostRecentDict_OnlyVariablesAndValuesDictOfDicts = ZeroAndSnapshotData_MostRecentDict["OnlyVariablesAndValuesDictOfDicts"]

                ZeroAndSnapshotData_MostRecentDict_desired_angle_deg_1__Raw_CurrentValue = ZeroAndSnapshotData_MostRecentDict_OnlyVariablesAndValuesDictOfDicts["desired_angle_deg_1"]["Raw_CurrentValue"]
                ZeroAndSnapshotData_MostRecentDict_desired_angle_deg_1__Raw_CurrentValue_Zeroed = ZeroAndSnapshotData_MostRecentDict_OnlyVariablesAndValuesDictOfDicts["desired_angle_deg_1"]["Raw_CurrentValue_Zeroed"]
                ZeroAndSnapshotData_MostRecentDict_desired_angle_deg_1__Raw_ZeroOffsetValue = ZeroAndSnapshotData_MostRecentDict_OnlyVariablesAndValuesDictOfDicts["desired_angle_deg_1"]["Raw_ZeroOffsetValue"]

                #print("ZeroAndSnapshotData_MostRecentDict_desired_angle_deg_1__Raw_ZeroOffsetValue: " + str(ZeroAndSnapshotData_MostRecentDict_desired_angle_deg_1__Raw_ZeroOffsetValue))

                #"Raw_CurrentValue"
                #"Filtered_CurrentValue"
                #"Raw_CurrentValue_Zeroed"
                #"Filtered_CurrentValue_Zeroed"
                #"Raw_SnapshottedValue"
                #"Filtered_SnapshottedValue"
                #"Raw_ZeroOffsetValue"
                #"Filtered_ZeroOffsetValue"
                #"Raw_DataForSnapshottingQueueSize"
                #"Filtered_DataForSnapshottingQueueSize"

            if USE_PrintMostRecentDictForDebuggingFlag == 1:
                print("ZeroAndSnapshotData_MostRecentDict: " + ConvertDictToProperlyFormattedStringForPrinting(ZeroAndSnapshotData_MostRecentDict, NumberOfDecimalsPlaceToUse=3))

        ###################################################
        ###################################################

        ################################################### SET's
        ###################################################
        if ZeroAndSnapshotData_OPEN_FLAG == 1:

            ####################################################
            ZeroAndSnapshotData_ReubenPython2and3ClassObject.CheckStateMachine()
            ####################################################

            ####################################################
            if USE_SINUSOIDAL_INPUT_FLAG == 1:
                time_gain = math.pi / (2.0 * SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle)
                desired_angle_deg_1 = 0.5*(SINUSOIDAL_MOTION_INPUT_MaxValue + SINUSOIDAL_MOTION_INPUT_MinValue) + abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue) * math.sin(time_gain * CurrentTime_MainLoopThread)  # AUTOMATIC SINUSOIDAL MOVEMENT
            else:
                desired_angle_deg_1 = 5.0
            ####################################################

            ####################################################
            if USE_SPECKLE_NOISE_FLAG == 1:
                NoiseCounter = NoiseCounter + 1
                if NoiseCounter == 1:
                    NoiseAmplitude = NoiseAmplitude_Percent0to1OfSinuisoidalInputAmplitude*abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue)
                    NoiseValue = random.uniform(-1.0*NoiseAmplitude, NoiseAmplitude)
                    desired_angle_deg_1 = desired_angle_deg_1 + NoiseValue
                    NoiseCounter = 0
            ####################################################

            desired_angle_deg_1_ListOfDicts = [dict([("Variable_Name", "desired_angle_deg_1"), ("Raw_CurrentValue", desired_angle_deg_1 )]),
                dict([("Variable_Name", "B"), ("Raw_CurrentValue", desired_angle_deg_1 + 1.0)]),
                dict([("Variable_Name", "C"), ("Raw_CurrentValue", desired_angle_deg_1 - 1.0)])]

            ZeroAndSnapshotData_ReubenPython2and3ClassObject.UpdateData(desired_angle_deg_1_ListOfDicts)
        ###################################################
        ###################################################

        ################################################### SETs
        ###################################################
        if PLOTTER_OPEN_FLAG == 1:

            ####################################################
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "StandAlonePlottingProcess_ReadyForWritingFlag" in MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict:
                MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict["StandAlonePlottingProcess_ReadyForWritingFlag"]

                if MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag == 1:
                    if CurrentTime_MainLoopThread - LastTime_MainLoopThread_PLOTTER >= 0.040:
                        #MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["raw"], [CurrentTime_CalculatedFromMainThread], [Tension_ActualValue_grams])
                        MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["raw", "zeroed", "offset"],
                                                                                                                                [CurrentTime_MainLoopThread, CurrentTime_MainLoopThread, CurrentTime_MainLoopThread],
                                                                                                                                [ZeroAndSnapshotData_MostRecentDict_desired_angle_deg_1__Raw_CurrentValue, ZeroAndSnapshotData_MostRecentDict_desired_angle_deg_1__Raw_CurrentValue_Zeroed, ZeroAndSnapshotData_MostRecentDict_desired_angle_deg_1__Raw_CurrentValue - ZeroAndSnapshotData_MostRecentDict_desired_angle_deg_1__Raw_ZeroOffsetValue])

                        LastTime_MainLoopThread_PLOTTER = CurrentTime_MainLoopThread
            ####################################################

        ###################################################
        ###################################################

        time.sleep(0.002)
    #################################################
    #################################################

    ################################################# THIS IS THE EXIT ROUTINE!
    #################################################
    print("Exiting main program 'test_program_for_ZeroAndSnapshotData_ReubenPython2and3Class.")

    #################################################
    if ZeroAndSnapshotData_OPEN_FLAG == 1:
        ZeroAndSnapshotData_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if MYPRINT_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if PLOTTER_OPEN_FLAG == 1:
        MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    #################################################

##########################################################################################################
##########################################################################################################