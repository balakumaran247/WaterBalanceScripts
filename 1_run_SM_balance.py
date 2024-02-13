# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:28:21 2020

@author: esa
"""
import os
os.chdir(r"C:\bhargavi\ACIWRM\Water Accounting\WAPlus_Sashi\2020_training\day1\scripts")
from WA.model_SMBalance import run_SMBalance

basin = 'Menasagi'
MAIN_FOLDER = r"C:\bhargavi\ACIWRM\Water Accounting\WAPlus_Sashi\2020_training\day1\Menasagi\Netcdf_files"
p_in = os.path.join(MAIN_FOLDER,'%s_P_CHIRPS.nc' %(basin)) # Monthly Precipitation
e_in = os.path.join(MAIN_FOLDER,'%s_ETa_SSEBop.nc'%(basin)) # Monthly Actual Evapotranspiration
i_in = os.path.join(MAIN_FOLDER,'i_monthly.nc') # Monthly Interception
nrd_in = os.path.join(MAIN_FOLDER,'nRD_monthly.nc') # Monthly Number of Rainy days
lu_in = os.path.join(MAIN_FOLDER,'%s_LU_WA.nc'%(basin)) # Yearly WaPOR Land Cover Map
smsat_file = os.path.join(MAIN_FOLDER,'%s_SMsat_HiHydroSoils.nc'%(basin)) #Saturated Water Content (%)


start_year=2010 
end_year = 2018

    
#default
f_perc=0.9 # percolation factor
f_Smax=0.70 #threshold for percolation
cf =  50 #f_Ssat soil mositure correction factor to componsate the variation in filling up and drying in a month
chunks=[1,300,300]
f_bf = 0.10
deep_perc_f = 0.01
root_depth_version = '1.0'

run_SMBalance(MAIN_FOLDER,p_in,e_in,i_in,nrd_in,lu_in,smsat_file, start_year, end_year, f_perc,f_Smax, cf, f_bf, deep_perc_f, root_depth_version, chunks)