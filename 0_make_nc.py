# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:01:05 2020

@author: cmi001
"""

#%% netCDF files from 
import os
import glob
os.chdir(r'H:\onedrive\ACIWRM\H_drive\water_accounting\workshop_3\day1\scripts')
from createNC_cmi import make_netcdf

# water year Karnataka June --> May

basedir = r"E:\AAA_Karnataka\Accounts\SM_Balance\Data"

pathET = os.path.join(basedir,'ET')
pathP = os.path.join(basedir,'P','monthly')
pathPday = os.path.join(basedir,'P','daily')

pathLAI = os.path.join(basedir,'LAI')

pathSMsat = os.path.join(basedir,'ThetaSat')
pathLU = r"E:\AAA_Karnataka\Training_3-5Aug\DAY2_WB\Data\LU"

template = r"E:\AAA_Karnataka\Training_3-5Aug\DAY2_WB\Data\LU\LU_1011_Menasagi_2010.06.01.tif"

shp_path = r"E:\AAA_Karnataka\Training_3-5Aug\DAY2_WB\Data\Boundaries\Menasagi.shp"
save_location = r"E:\AAA_Karnataka\Training_3-5Aug\DAY2_WB\Menasagi"


name = 'Menasagi'
datasets = {
               'ET'    : [pathET, 
                                   ('time','latitude', 'longitude'), 
                                   {'units': 'mm/month', 'source': 'SSEBop', 'quantity':'ETa'}],
               'P'    : [pathP, 
                                   ('time','latitude', 'longitude'), 
                                   {'units': 'mm/month', 'source': 'CHIRPS', 'quantity':'P'}],
             'LAI' : [pathLAI,
                                 ('time','latitude', 'longitude'), 
                                 {'units': 'None', 'source': 'MOD15', 'quantity':'LAI'}],
                 'dailyP' : [pathPday,
                                   ('time','latitude', 'longitude'), 
                                   {'units': 'mm/d', 'source': 'CHIRPS', 'quantity':'dailyP'}],
               'SMsat' : [pathSMsat,
                                   ('time','latitude', 'longitude'), 
                                   {'units': 'None', 'source': 'HiHydroSoils', 'quantity':'SMsat'}],
             'LU' : [pathLU,
                                 ('time','latitude', 'longitude'), 
                                 {'units': 'None', 'source': 'WA', 'quantity':'LU'}]

        }


# Make netCDF from tiff files
nc_files = []

for d in datasets:
    filesAll = glob.glob(os.path.join(datasets[d][0],'*.tif'))
    dataset = {d: datasets[d]}
    fname = name+'_'+datasets[d][2]['quantity']+'_'+ datasets[d][2]['source']+'.nc'
    nc_file = os.path.join(save_location, fname)
    nc_files.append(nc_file)
    succes = make_netcdf(nc_file, dataset, shp_path, template, name)
    
#%% prepare additional data for running SMBalance

import pre_proc_sm_balance

nc_files = glob.glob(r'H:\onedrive\ACIWRM\H_drive\water_accounting\workshop_3\day1\Menasagi\Netcdf_files\*.nc')

dailyp_nc = nc_files[4]
p_nc = nc_files[4]
n_nc = pre_proc_sm_balance.rainy_days(dailyp_nc, p_nc)

lai_nc = nc_files[2]
i_nc = pre_proc_sm_balance.interception(lai_nc, p_nc, n_nc)











