# Simulation Configuration Files

This directory contains the pointers and references for any configuration files for MM or MD programs submitted to the Exchange.
Raw files are not placed in this directory and only linked to through:
```
sorted_by_group
└──GROUP_NAME
   └── TARGET
       └── simulation_configs
           └── SIMULATION_SOFTWARE
```

The default sort will be by which particular software is used. 
Any structure file referenced by the configs will also be included in the link.
