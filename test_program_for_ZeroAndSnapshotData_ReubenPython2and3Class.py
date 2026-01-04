# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision E, 12/26/2025

Verified working on: Python 3.11/12/13 for Windows 10/11 64-bit and Raspberry Pi Bookworm (does not work on Mac).
'''

__author__ = 'reuben.brewer'

##########################################################################################################
##########################################################################################################

#################################################
import ReubenGithubCodeModulePaths #Replaces the need to have "ReubenGithubCodeModulePaths.pth" within "C:\Anaconda3\Lib\site-packages".
ReubenGithubCodeModulePaths.Enable()
#################################################

#################################################
from MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *
from ZeroAndSnapshotData_ReubenPython2and3Class import *
#################################################

#################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
import random
import math
import traceback
import keyboard
#################################################

#################################################
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
#################################################

#################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
#################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
def GetLatestWaveformValue(CurrentTime, MinValue, MaxValue, Period, WaveformTypeString="Sine"):
    
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        try:

            ##########################################################################################################
            ##########################################################################################################
            OutputValue = 0.0
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            WaveformTypeString_ListOfAcceptableValues = ["Sine", "Cosine", "Triangular", "Square"]
        
            if WaveformTypeString not in WaveformTypeString_ListOfAcceptableValues:
                print("GetLatestWaveformValue: Error, WaveformTypeString must be in " + str(WaveformTypeString_ListOfAcceptableValues))
                return -11111.0
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            if WaveformTypeString == "Sine":
    
                TimeGain = math.pi/Period
                OutputValue = (MaxValue + MinValue)/2.0 + 0.5*abs(MaxValue - MinValue)*math.sin(TimeGain*CurrentTime)
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            elif WaveformTypeString == "Cosine":
    
                TimeGain = math.pi/Period
                OutputValue = (MaxValue + MinValue)/2.0 + 0.5*abs(MaxValue - MinValue)*math.cos(TimeGain*CurrentTime)
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            elif WaveformTypeString == "Triangular":
                TriangularInput_TimeGain = 1.0
                TriangularInput_MinValue = -5
                TriangularInput_MaxValue = 5.0
                TriangularInput_PeriodInSeconds = 2.0
        
                #TriangularInput_Height0toPeak = abs(TriangularInput_MaxValue - TriangularInput_MinValue)
                #TriangularInput_CalculatedValue_1 = abs((TriangularInput_TimeGain*CurrentTime_CalculatedFromMainThread % PeriodicInput_PeriodInSeconds) - TriangularInput_Height0toPeak) + TriangularInput_MinValue
        
                A = abs(MaxValue - MinValue)
                P = Period
    
                #https://stackoverflow.com/questions/1073606/is-there-a-one-line-function-that-generates-a-triangle-wave
                OutputValue = (A / (P / 2)) * ((P / 2) - abs(CurrentTime % (2 * (P / 2)) - P / 2)) + MinValue
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            elif WaveformTypeString == "Square":
    
                TimeGain = math.pi/Period
                MeanValue = (MaxValue + MinValue)/2.0
                SinusoidalValue =  MeanValue + 0.5*abs(MaxValue - MinValue)*math.sin(TimeGain*CurrentTime)
                
                if SinusoidalValue >= MeanValue:
                    OutputValue = MaxValue
                else:
                    OutputValue = MinValue
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            else:
                OutputValue = 0.0
            ##########################################################################################################
            ##########################################################################################################
            
            return OutputValue

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        except:
            exceptions = sys.exc_info()[0]
            print("GetLatestWaveformValue: Exceptions: %s" % exceptions)
            #return -11111.0
            traceback.print_exc()
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

##########################################################################################################
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
                                                 str(Key) + ":\n" + \
                                                 ConvertDictToProperlyFormattedStringForPrinting(DictToPrint[Key], NumberOfDecimalsPlaceToUse, NumberOfEntriesPerLine, NumberOfTabsBetweenItems)

        else:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                 str(Key) + ": " + \
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

    global ZeroAndSnapshotData_Object
    global ZeroAndSnapshotData_OPEN_FLAG
    global SHOW_IN_GUI_ZeroAndSnapshotData_FLAG

    global MyPrint_Object
    global MyPrint_OPEN_FLAG
    global SHOW_IN_GUI_MyPrint_FLAG

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
                ZeroAndSnapshotData_Object.GUI_update_clock()
            #########################################################

            #########################################################
            if MyPrint_OPEN_FLAG == 1 and SHOW_IN_GUI_MyPrint_FLAG == 1:
                MyPrint_Object.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback(OptionalArugment = 0):
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

    global ZeroAndSnapshotData_Object
    global ZeroAndSnapshotData_OPEN_FLAG

    global MyPrint_Object
    global MyPrint_OPEN_FLAG

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
    
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_ZeroAndSnapshotData_ReubenPython2and3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
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
    #################################################
    DebuggingInfo_Label = Label(Tab_MainControls, text="Device Info", width=120, font=("Helvetica", 10))
    DebuggingInfo_Label.grid(row=1, column=0, padx=1, pady=1, columnspan=10, rowspan=1)
    #################################################
    #################################################

    #################################################
    #################################################
    if ZeroAndSnapshotData_OPEN_FLAG == 1:
        ZeroAndSnapshotData_Object.CreateGUIobjects(TkinterParent=Tab_ZeroAndSnapshotData)
    #################################################
    #################################################

    #################################################
    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_Object.CreateGUIobjects(TkinterParent=Tab_MyPrint)
    #################################################
    #################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    #################################################
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    #################################################
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################
    #################################################

##########################################################################################################
##########################################################################################################

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

    global USE_MyPrint_FLAG
    USE_MyPrint_FLAG = 1

    global USE_MyPlotterPureTkinterStandAloneProcess_FLAG
    USE_MyPlotterPureTkinterStandAloneProcess_FLAG = 1

    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_TABS_IN_GUI_FLAG
    USE_TABS_IN_GUI_FLAG = 1

    global USE_PeriodicInput_FLAG
    USE_PeriodicInput_FLAG = 1

    global USE_SPECKLE_NOISE_FLAG
    USE_SPECKLE_NOISE_FLAG = 1

    global USE_PrintMostRecentDictForDebuggingFlag
    USE_PrintMostRecentDictForDebuggingFlag = 0

    global USE_KEYBOARD_FLAG
    USE_KEYBOARD_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_ZeroAndSnapshotData_FLAG
    SHOW_IN_GUI_ZeroAndSnapshotData_FLAG = 1

    global SHOW_IN_GUI_MyPrint_FLAG
    SHOW_IN_GUI_MyPrint_FLAG = 1
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

    global GUI_ROW_MyPrint
    global GUI_COLUMN_MyPrint
    global GUI_PADX_MyPrint
    global GUI_PADY_MyPrint
    global GUI_ROWSPAN_MyPrint
    global GUI_COLUMNSPAN_MyPrint
    GUI_ROW_MyPrint = 2

    GUI_COLUMN_MyPrint = 0
    GUI_PADX_MyPrint = 1
    GUI_PADY_MyPrint = 1
    GUI_ROWSPAN_MyPrint = 1
    GUI_COLUMNSPAN_MyPrint = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess
    LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess = -11111.0

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

    global PeriodicInput_AcceptableValues
    PeriodicInput_AcceptableValues = ["GUI", "Sine", "Cosine", "Triangular", "Square"]

    global PeriodicInput_Type_1
    PeriodicInput_Type_1 = "Sine"

    global PeriodicInput_MinValue_1
    PeriodicInput_MinValue_1 = 2.0

    global PeriodicInput_MaxValue_1
    PeriodicInput_MaxValue_1 = 3.0

    global PeriodicInput_Period_1
    PeriodicInput_Period_1 = 1.0

    global PeriodicInput_CalculatedValue_1
    PeriodicInput_CalculatedValue_1 = 0.0

    global NoiseCounter
    NoiseCounter = 0

    global NoiseCounter_FireEveryNth
    NoiseCounter_FireEveryNth = 5

    global NoiseAmplitude_Percent0to1OfPeriodicInputAmplitude
    NoiseAmplitude_Percent0to1OfPeriodicInputAmplitude = 0.25
    #################################################
    #################################################

    #################################################
    #################################################
    global ZeroAndSnapshotData_Object

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

    global ZeroAndSnapshotData_MostRecentDict_DesiredAngleDeg1__Raw_CurrentValue
    ZeroAndSnapshotData_MostRecentDict_DesiredAngleDeg1__Raw_CurrentValue = -11111

    global ZeroAndSnapshotData_MostRecentDict_DesiredAngleDeg1__Raw_CurrentValue_Zeroed
    ZeroAndSnapshotData_MostRecentDict_DesiredAngleDeg1__Raw_CurrentValue_Zeroed = -11111

    global ZeroAndSnapshotData_MostRecentDict_DesiredAngleDeg1__Raw_ZeroOffsetValue
    ZeroAndSnapshotData_MostRecentDict_DesiredAngleDeg1__Raw_Raw_ZeroOffsetValue = -11111
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_Object

    global MyPrint_OPEN_FLAG
    MyPrint_OPEN_FLAG = -1
    #################################################
    #################################################

    ####################################################
    ####################################################
    global MyPlotterPureTkinterStandAloneProcess_Object

    global MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG
    MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = -1

    global MyPlotterPureTkinter_MostRecentDict
    MyPlotterPureTkinter_MostRecentDict = dict()

    global MyPlotterPureTkinterStandAloneProcess_MostRecentDict_ReadyForWritingFlag
    MyPlotterPureTkinterStandAloneProcess_MostRecentDict_ReadyForWritingFlag = -1
    ####################################################
    ####################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global ZeroAndSnapshotData_Variables_ListOfDicts
    ZeroAndSnapshotData_Variables_ListOfDicts = [dict([("Variable_Name", "DesiredAngleDeg1"),("DataCollectionDurationInSecondsForSnapshottingAndZeroing", 5.5)]),
                                                  dict([("Variable_Name", "B"),("DataCollectionDurationInSecondsForSnapshottingAndZeroing", 7.5)]),
                                                  dict([("Variable_Name", "C"),("DataCollectionDurationInSecondsForSnapshottingAndZeroing", 9.0)])]


    global ZeroAndSnapshotData_GUIparametersDict
    ZeroAndSnapshotData_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_ZeroAndSnapshotData_FLAG),
                                            ("EnableInternal_MyPrint_Flag", 1),
                                            ("NumberOfPrintLines", 10),
                                            ("UseBorderAroundThisGuiObjectFlag", 1),
                                            ("GUI_ROW", GUI_ROW_ZeroAndSnapshotData),
                                            ("GUI_COLUMN", GUI_COLUMN_ZeroAndSnapshotData),
                                            ("GUI_PADX", GUI_PADX_ZeroAndSnapshotData),
                                            ("GUI_PADY", GUI_PADY_ZeroAndSnapshotData),
                                            ("GUI_ROWSPAN", GUI_ROWSPAN_ZeroAndSnapshotData),
                                            ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_ZeroAndSnapshotData)])

    global ZeroAndSnapshotData_SetupDict
    ZeroAndSnapshotData_SetupDict = dict([("GUIparametersDict", ZeroAndSnapshotData_GUIparametersDict),
                                            ("NameToDisplay_UserSet", "Reuben's Test ZeroAndSnapshotData"),
                                            ("Variables_ListOfDicts", ZeroAndSnapshotData_Variables_ListOfDicts)])

    if USE_ZeroAndSnapshotData_FLAG == 1:
        try:
            ZeroAndSnapshotData_Object = ZeroAndSnapshotData_ReubenPython2and3Class(ZeroAndSnapshotData_SetupDict)
            ZeroAndSnapshotData_OPEN_FLAG = ZeroAndSnapshotData_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("ZeroAndSnapshotData_Object __init__: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_ZeroAndSnapshotData_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if ZeroAndSnapshotData_OPEN_FLAG != 1:
                print("Failed to open ZeroAndSnapshotData_Object.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global MyPrint_GUIparametersDict
    MyPrint_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MyPrint_FLAG),
                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                        ("GUI_ROW", GUI_ROW_MyPrint),
                                        ("GUI_COLUMN", GUI_COLUMN_MyPrint),
                                        ("GUI_PADX", GUI_PADX_MyPrint),
                                        ("GUI_PADY", GUI_PADY_MyPrint),
                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MyPrint),
                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MyPrint)])

    global MyPrint_SetupDict
    MyPrint_SetupDict = dict([("NumberOfPrintLines", 10),
                            ("WidthOfPrintingLabel", 200),
                            ("PrintToConsoleFlag", 1),
                            ("LogFileNameFullPath", os.path.join(os.getcwd(), "TestLog.txt")),
                            ("GUIparametersDict", MyPrint_GUIparametersDict)])

    if USE_MyPrint_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            MyPrint_Object = MyPrint_ReubenPython2and3Class(MyPrint_SetupDict)
            MyPrint_OPEN_FLAG = MyPrint_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_Object __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if MyPrint_OPEN_FLAG != 1:
                print("Failed to open MyPrint_Object.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global MyPlotterPureTkinterStandAloneProcess_GUIparametersDict
    MyPlotterPureTkinterStandAloneProcess_GUIparametersDict = dict([("EnableInternal_MyPrint_Flag", 1),
                                                                    ("NumberOfPrintLines", 10),
                                                                    ("GraphCanvasWidth", 900),
                                                                    ("GraphCanvasHeight", 700),
                                                                    ("GraphCanvasWindowStartingX", 0),
                                                                    ("GraphCanvasWindowStartingY", 0),
                                                                    ("GraphCanvasWindowTitle", "My plotting example!"),
                                                                    ("GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents", 30)])


    global MyPlotterPureTkinterStandAloneProcess_SetupDict
    MyPlotterPureTkinterStandAloneProcess_SetupDict = dict([("GUIparametersDict", MyPlotterPureTkinterStandAloneProcess_GUIparametersDict),
                                                            ("ParentPID", os.getpid()),
                                                            ("WatchdogTimerDurationSeconds_ExpirationWillEndStandAlonePlottingProcess", 5.0),
                                                            ("CurvesToPlotNamesAndColorsDictOfLists", dict([("NameList", ["raw", "zeroed", "offset"]),
                                                                                                        ("MarkerSizeList", [2]*3),
                                                                                                        ("LineWidthList", [2]*3),
                                                                                                        ("IncludeInXaxisAutoscaleCalculationList", [1]*3),
                                                                                                        ("IncludeInYaxisAutoscaleCalculationList", [1]*3),
                                                                                                        ("ColorList", ["Blue", "Red", "Green"])])),
                                                            ("SmallTextSize", 7),
                                                            ("LargeTextSize", 12),
                                                            ("NumberOfDataPointToPlot", 100),
                                                            ("XaxisNumberOfTickMarks", 10),
                                                            ("YaxisNumberOfTickMarks", 10),
                                                            ("XaxisNumberOfDecimalPlacesForLabels", 3),
                                                            ("YaxisNumberOfDecimalPlacesForLabels", 3),
                                                            ("XaxisAutoscaleFlag", 1),
                                                            ("YaxisAutoscaleFlag", 1),
                                                            ("X_min", 0.0),
                                                            ("X_max", 5.0),
                                                            ("Y_min", -5.0),
                                                            ("Y_max", 5.0),
                                                            ("XaxisDrawnAtBottomOfGraph", 0),
                                                            ("XaxisLabelString", "Time (sec)"),
                                                            ("YaxisLabelString", "Y-units (units)"),
                                                            ("ShowLegendFlag", 1),
                                                            ("GraphNumberOfLeadingZeros", 0),
                                                            ("GraphNumberOfDecimalPlaces", 3),
                                                            ("SavePlot_DirectoryPath", os.path.join(os.getcwd(), "SavedImagesFolder")),
                                                            ("KeepPlotterWindowAlwaysOnTopFlag", 0),
                                                            ("RemoveTitleBorderCloseButtonAndDisallowWindowMoveFlag", 0),
                                                            ("AllowResizingOfWindowFlag", 1)])

    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            MyPlotterPureTkinterStandAloneProcess_Object = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class(MyPlotterPureTkinterStandAloneProcess_SetupDict)
            MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = MyPlotterPureTkinterStandAloneProcess_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPlotterPureTkinterStandAloneProcess_Object, exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG != 1:
                print("Failed to open MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if USE_KEYBOARD_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        keyboard.on_press_key("esc", ExitProgram_Callback)
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## KEY GUI LINE
    ##########################################################################################################
    ##########################################################################################################
    if USE_GUI_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread, daemon=True) #Daemon=True means that the GUI thread is destroyed automatically when the main thread is destroyed
        GUI_Thread_ThreadingObject.start()
    else:
        root = None
        Tab_MainControls = None
        Tab_ZeroAndSnapshotData = None
        Tab_MyPrint = None
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    random.seed()
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if EXIT_PROGRAM_FLAG == 0:
        print("Starting main loop 'test_program_for_ZeroAndSnapshotData_ReubenPython2and3Class.")
        StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    while(EXIT_PROGRAM_FLAG == 0):

        ###################################################
        ###################################################
        ###################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ###################################################
        ###################################################
        ###################################################
        
        ################################################### GET's
        ###################################################
        ###################################################
        if ZeroAndSnapshotData_OPEN_FLAG == 1:

            ZeroAndSnapshotData_MostRecentDict = ZeroAndSnapshotData_Object.GetMostRecentDataDict()

            if "DataUpdateNumber" in ZeroAndSnapshotData_MostRecentDict:
                ZeroAndSnapshotData_MostRecentDict_DataUpdateNumber = ZeroAndSnapshotData_MostRecentDict["DataUpdateNumber"]
                ZeroAndSnapshotData_MostRecentDict_LoopFrequencyHz = ZeroAndSnapshotData_MostRecentDict["LoopFrequencyHz"]
                ZeroAndSnapshotData_MostRecentDict_OnlyVariablesAndValuesDictOfDicts = ZeroAndSnapshotData_MostRecentDict["OnlyVariablesAndValuesDictOfDicts"]

                ZeroAndSnapshotData_MostRecentDict_DesiredAngleDeg1__Raw_CurrentValue = ZeroAndSnapshotData_MostRecentDict_OnlyVariablesAndValuesDictOfDicts["DesiredAngleDeg1"]["Raw_CurrentValue"]
                ZeroAndSnapshotData_MostRecentDict_DesiredAngleDeg1__Raw_CurrentValue_Zeroed = ZeroAndSnapshotData_MostRecentDict_OnlyVariablesAndValuesDictOfDicts["DesiredAngleDeg1"]["Raw_CurrentValue_Zeroed"]
                ZeroAndSnapshotData_MostRecentDict_DesiredAngleDeg1__Raw_ZeroOffsetValue = ZeroAndSnapshotData_MostRecentDict_OnlyVariablesAndValuesDictOfDicts["DesiredAngleDeg1"]["Raw_ZeroOffsetValue"]

                #print("ZeroAndSnapshotData_MostRecentDict_DesiredAngleDeg1__Raw_ZeroOffsetValue: " + str(ZeroAndSnapshotData_MostRecentDict_DesiredAngleDeg1__Raw_ZeroOffsetValue))

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
        ###################################################

        ################################################### SET's
        ###################################################
        ###################################################
        if ZeroAndSnapshotData_OPEN_FLAG == 1:

            ###################################################
            ###################################################
            ZeroAndSnapshotData_Object.CheckStateMachine()
            ###################################################
            ###################################################

            ###################################################
            ###################################################
            if USE_PeriodicInput_FLAG == 1:

                ####################################################
                PeriodicInput_CalculatedValue_1 = GetLatestWaveformValue(CurrentTime_MainLoopThread, 
                                                                    PeriodicInput_MinValue_1, 
                                                                    PeriodicInput_MaxValue_1, 
                                                                    PeriodicInput_Period_1, 
                                                                    PeriodicInput_Type_1)
                ###################################################
                
                ###################################################
                NoiseCounter = NoiseCounter + 1
                if NoiseCounter == NoiseCounter_FireEveryNth:
                    NoiseAmplitude = NoiseAmplitude_Percent0to1OfPeriodicInputAmplitude * abs(PeriodicInput_MaxValue_1 - PeriodicInput_MinValue_1)
                    NoiseValue = random.uniform(-1.0 * NoiseAmplitude, NoiseAmplitude)
                    PeriodicInput_CalculatedValue_1 = PeriodicInput_CalculatedValue_1 + NoiseValue
                    NoiseCounter = 0
                ###################################################

                ###################################################
                DesiredAngleDeg1 = PeriodicInput_CalculatedValue_1
                ###################################################
                
            ###################################################
            ###################################################

            ###################################################
            ###################################################
            DesiredAngleDeg1_ListOfDicts = [dict([("Variable_Name", "DesiredAngleDeg1"), ("Raw_CurrentValue", DesiredAngleDeg1)]),
                                            dict([("Variable_Name", "B"), ("Raw_CurrentValue", DesiredAngleDeg1 + 1.0)]),
                                            dict([("Variable_Name", "C"), ("Raw_CurrentValue", DesiredAngleDeg1 - 1.0)])]

            ZeroAndSnapshotData_Object.UpdateData(DesiredAngleDeg1_ListOfDicts)
            ###################################################
            ###################################################

        ###################################################
        ###################################################
        ###################################################

        ################################################### SETs
        ###################################################
        ###################################################
        if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:

            ###################################################
            ###################################################
            MyPlotterPureTkinterStandAloneProcess_MostRecentDict = MyPlotterPureTkinterStandAloneProcess_Object.GetMostRecentDataDict()

            if "StandAlonePlottingProcess_ReadyForWritingFlag" in MyPlotterPureTkinterStandAloneProcess_MostRecentDict:
                MyPlotterPureTkinterStandAloneProcess_MostRecentDict_ReadyForWritingFlag = MyPlotterPureTkinterStandAloneProcess_MostRecentDict["StandAlonePlottingProcess_ReadyForWritingFlag"]

                if MyPlotterPureTkinterStandAloneProcess_MostRecentDict_ReadyForWritingFlag == 1:
                    if CurrentTime_MainLoopThread - LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess >= MyPlotterPureTkinterStandAloneProcess_GUIparametersDict["GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents"]/1000.0 + 0.001:

                        MyPlotterPureTkinterStandAloneProcess_Object.ExternalAddPointOrListOfPointsToPlot(["raw", "zeroed", "offset"],
                                                                                                        [CurrentTime_MainLoopThread, CurrentTime_MainLoopThread, CurrentTime_MainLoopThread],
                                                                                                        [ZeroAndSnapshotData_MostRecentDict_DesiredAngleDeg1__Raw_CurrentValue, ZeroAndSnapshotData_MostRecentDict_DesiredAngleDeg1__Raw_CurrentValue_Zeroed, ZeroAndSnapshotData_MostRecentDict_DesiredAngleDeg1__Raw_CurrentValue - ZeroAndSnapshotData_MostRecentDict_DesiredAngleDeg1__Raw_ZeroOffsetValue])

                        LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess = CurrentTime_MainLoopThread
            ###################################################
            ###################################################

        ###################################################
        ###################################################
        ###################################################

        time.sleep(0.002) #unicorn
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## THIS IS THE EXIT ROUTINE!
    ##########################################################################################################
    ##########################################################################################################
    print("Exiting main program 'test_program_for_ZeroAndSnapshotData_ReubenPython2and3Class.")

    #################################################
    if ZeroAndSnapshotData_OPEN_FLAG == 1:
        ZeroAndSnapshotData_Object.ExitProgram_Callback()
    #################################################

    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_Object.ExitProgram_Callback()
    #################################################

    #################################################
    if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:
        MyPlotterPureTkinterStandAloneProcess_Object.ExitProgram_Callback()
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################