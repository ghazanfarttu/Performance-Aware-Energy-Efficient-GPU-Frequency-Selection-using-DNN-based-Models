# 

import pandas as pd
HPC_DataPath = "C:/Users/Ghazanfar/OneDrive - Texas Tech University/2023/POST_IPDPS/AE/datasets/hpc/v100/"
df = pd.read_csv(HPC_DataPath+'mean_fp_data_HPC_apps.csv',index_col=0)

app = 'LAMMPS'
print('**************************************---'+app+'---**************************************')
lmp = df.loc[df['application'] == app]
lmp = lmp.copy()
lmp.reset_index(drop=True,inplace=True)
lmp.to_csv(HPC_DataPath+'GV100-dvfs-'+app+'-dcgm.csv',index=False)
print(lmp)

app = 'NAMD'
print('**************************************---'+app+'---**************************************')
namd = df.loc[df['application'] == app]
namd = namd.copy()
namd.reset_index(drop=True,inplace=True)
namd.to_csv(HPC_DataPath+'GV100-dvfs-'+app+'-dcgm.csv',index=False)
print(namd)

app = 'LSTM'
print('**************************************---'+app+'---**************************************')
namd = df.loc[df['application'] == app]
namd = namd.copy()
namd.reset_index(drop=True,inplace=True)
namd.to_csv(HPC_DataPath+'GV100-dvfs-'+app+'-dcgm.csv',index=False)
print(namd)
