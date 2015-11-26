# =================================================================
#
# Terms and Conditions of Use
#
# Unless otherwise noted, computer program source code of this
# distribution is covered under Crown Copyright, Government of
# Canada, and is distributed under the MIT License.
#
# The Canada wordmark and related graphics associated with this
# distribution are protected under trademark law and copyright law.
# No permission is granted to use them outside the parameters of
# the Government of Canada's corporate identity program. For
# more information, see
# http://www.tbs-sct.gc.ca/fip-pcim/index-eng.asp
#
# Copyright title to all 3rd party software distributed with this
# software is held by the respective copyright holders as noted in
# those files. Users are asked to read the 3rd Party Licenses
# referenced with those assets.
#
# Copyright (c) 2015 Government of Canada
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

# TotalOzone reader example 1

import csv
from StringIO import StringIO
from woudc_extcsv import Reader, load, loads


# Using data from:
# http://woudc.org/archive/Archive-NewFormat/TotalOzone_1.0_1/
# stn031/dobson/2014/20140401.Dobson.Beck.076.NOAA-CMDL.csv
# Content copied below
'''
* This file was generated by WODC_TO_CSX v1.4
using WODC 80-column formatted data.
* 'na' is used where Instrument Model or
 Number are not available.

#CONTENT
Class,Category,Level,Form
WOUDC,TotalOzone,1.0,1

#DATA_GENERATION
Date,Agency,Version,ScientificAuthority
2008-11-12,IMD,0.0,

#PLATFORM
Type,ID,Name,Country,GAW_ID
STN,400,Maitri,ATA,

#INSTRUMENT
Name,Model,Number
Brewer,MKIV,153

#LOCATION
Latitude,Longitude,Height
-70.45,11.45,330

#TIMESTAMP
UTCOffset,Date,Time
+00:00:00,2006-12-01,

#DAILY
Date,WLCode,ObsCode,ColumnO3,StdDevO3,UTC_Begin,UTC_End,UTC_Mean,nObs,mMu,ColumnSO2
2006-12-01,0,0,202,,,,,32,,07
2006-12-02,0,0,207,,,,,35,,04
2006-12-03,0,0,220,,,,,31,,03
2006-12-04,0,0,219,,,,,15,,02
2006-12-05,0,0,215,,,,,25,,05
2006-12-06,0,0,227,,,,,33,,03
2006-12-07,0,0,230,,,,,15,,01
2006-12-08,0,0,214,,,,,34,,05
2006-12-09,0,0,217,,,,,34,,05
2006-12-10,0,0,219,,,,,37,,07
2006-12-11,0,0,218,,,,,33,,07
2006-12-14,0,0,218,,,,,12,,03
2006-12-18,0,0,238,,,,,31,,08
2006-12-19,0,0,238,,,,,33,,07
2006-12-20,0,0,241,,,,,33,,05
2006-12-21,0,0,244,,,,,25,,08
2006-12-22,0,0,247,,,,,30,,08
2006-12-23,0,0,265,,,,,18,,04
2006-12-24,0,0,268,,,,,13,,04
2006-12-25,0,0,259,,,,,23,,05
2006-12-29,0,0,266,,,,,27,,05
2006-12-30,0,0,260,,,,,25,,05
2006-12-31,0,0,270,,,,,35,,04

*  MEAN  235  ::S=8 CLOUDY SKY/HAZE:XXX=OZONE                    1  2  153

#TIMESTAMP
UTCOffset,Date,Time
+00:00:00,2006-12-31,

#MONTHLY
Date,ColumnO3,StdDevO3,Npts
2006-12-01,235,21.4,23
'''

# load file into memory from local path
extcsv_to = load('../tests/data/20061201.brewer.mkiv.153.imd.csv')

# access all tables
# multiple occurance of tables are indexed as per order of occurance
tables = extcsv_to.sections.keys()
print ('All tables:')
print (tables)
print ('')
# get fields for a talbe
CONTENT = extcsv_to.sections['CONTENT'].keys()
print ('CONTENT fields:')
print (CONTENT)
print ('')
# get field value
CONTENT_Category = extcsv_to.sections['CONTENT']['Category']
print ('CONTENT.Category value:')
print (CONTENT_Category)
print ('')
DATA_GENERATION_Agency = extcsv_to.sections['DATA_GENERATION']['Agency']
print ('DATA_GENERATION.Agency value:')
print (DATA_GENERATION_Agency)
print ('')
# second TIMESTAMP
TIMESTAMP2_Date = extcsv_to.sections['TIMESTAMP2']['Date']
print ('TIMESTAMP2.Date value:')
print (TIMESTAMP2_Date)
print ('')
# get profile/payload table values; these are tables with multiple rows
# in the case of TotalOzone, the profile table is DAILY
DAILY_raw = extcsv_to.sections['DAILY']['_raw']
print ('DAILY table and content:')
print (DAILY_raw)
DAILY = StringIO(DAILY_raw)
DAILY_rows = csv.reader(DAILY)
DAILY_header = DAILY_rows.next()
print ('DAILY fields:')
print (DAILY_header)
print ('')
# get first row of values
DAILY_row_1 = DAILY_rows.next()
print ('DAILY row 1 values:')
print (DAILY_row_1)
print ('')
# get second row of values
DAILY_row_2 = DAILY_rows.next()
print ('DAILY row 2 values:')
print (DAILY_row_2)
print ('')
# get secon row WLCode'
DAILY_row_2_WLCode = DAILY_row_2[DAILY_header.index('WLCode')]
print ('DAILY row 2 WLCode values:')
print (DAILY_row_2_WLCode)
print ('')
# get all ColumnO3
DAILY = StringIO(DAILY_raw)
DAILY_rows = csv.reader(DAILY)
DAILY_header = DAILY_rows.next()
print ('All DAILY ColumnO3 values:')
for row in DAILY_rows:
    DAILY_ColumnO3 = row[DAILY_header.index('ColumnO3')]
    print (DAILY_ColumnO3)
