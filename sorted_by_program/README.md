# Data Sorted by MM or MD Program

This directory contains pointers to all data submitted to the Exchange, but sorted by Molecular 
Mechanics or Molecular Dynamics program
Raw files are not placed in this directory and only linked to through:
```
sorted_by_group
└──GROUP_NAME
   └── TARGET
       ├── program_specific_structures
       │   └── SIMULATION_SOFTWARE
       ├── simulation_configs
       │   └── SIMULATION_SOFTWARE
       └── trajectories
           └── SIMULATION_SOFTWARE
``` 

Structures which are needed to run the configs files or referenced by trajectories will also be linked.
Papers which reference particular programs will also be linked in here. 
Data which is not related to the software itself (such as papers which do not include software) are not relinked here.
