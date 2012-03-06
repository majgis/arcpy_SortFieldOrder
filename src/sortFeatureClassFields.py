# Copyright 2012, Michael A. Jackson
# Attribution 3.0 Unported (CC BY 3.0)
# http://creativecommons.org/licenses/by/3.0/

""" Create a new feature class with sorted fields.
    
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
        
    inFeatureClassPath = arcpy.GetParameterAsText(0).strip('"')
    outFeatureClassPath = arcpy.GetParameterAsText(1).strip('"')
    putTheseFirst = arcpy.GetParameterAsText(2).lower().split(";")
    
    outWorkspace = os.path.dirname(outFeatureClassPath)
    outName = os.path.basename(outFeatureClassPath)
    
    fieldMappings = arcpyh.getSortedFieldMappings(arcpy, inFeatureClassPath, putTheseFirst)

    arcpy.FeatureClassToFeatureClass_conversion(inFeatureClassPath, outWorkspace, outName, None, fieldMappings)
    

if __name__ == "__main__":
    main()
    