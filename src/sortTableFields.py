# Copyright 2012, Michael A. Jackson
# Attribution 3.0 Unported (CC BY 3.0)
# http://creativecommons.org/licenses/by/3.0/

""" Create a new table with sorted fields.
    
    Option to move selected fields to the front.
    ArcGIS 10 toolbox script

"""

import arcpy
import sys
import os

import arcpyh

def main(argv = None):
    
    if argv == None:
        argv = sys.argv
    
    #Input Arguments
    inTablePath = arcpy.GetParameterAsText(0).strip('"')
    outTablePath = arcpy.GetParameterAsText(1).strip('"')
    putTheseFirst = arcpy.GetParameterAsText(2).lower().split(";")
    
    outWorkspace = os.path.dirname(outTablePath)
    outName = os.path.basename(outTablePath)
    
    fieldMappings = arcpyh.getSortedFieldMappings(arcpy, inTablePath, putTheseFirst)
    
    arcpy.TableToTable_conversion(inTablePath, outWorkspace, outName, None, fieldMappings)


if __name__ == "__main__":
    main()
    