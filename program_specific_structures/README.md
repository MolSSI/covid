# Program Specific Structures

This directory contains the pointers and references for any structure submitted the Exchange which works 
only with a specific MM or MD program.
Raw files are not placed in this directory and only linked to through:
```
sorted_by_group
└──GROUP_NAME
   └── SUBMISSION_ID
       └── TARGET
           └── program_specific_structures
               └── SIMULATION_SOFTWARE
```

The links here will be referenced by the simulation software itself, so this shares a fair amount of 
overlap with `sorted_by_program`, but the sort might come out differently. Other non-program-specific 
structures which are referenced or that these are derived from are also linked.
