# Simulations relevant to COVID-19 disease

## To add new resources

Contribute a separate [YAML file](https://yaml.org/) for each entry.

### YAML schema

Each entry has the following required and optional keys:
```
type: one of [docking, md, mc, mdmc, mdmd]
title: (required)
description: (required)
creator: (required)
organization: (optional)
lab: (optional)
institute: (optional)
models: (required) must point to model in `models` dir
    - modelname_1
    - ...
proteins: (required) Must be a valid protein (see `proteins` dir) 
    - protein 1
    - ...
structures: (required) must point to structure which could be in `structure` dir
    - structure 1
    - ...
rating: (optional) int on domain [1,5], 5 is better
files: (optional) URLs to input and supporting files (not trajectory itself)
    - file 1
    - ...
trajectory: (required) URL to trajectory file. It is acceptable to have it be a compressed object with additional supporting files
size: (required) Size of trajectory file, please include units
length: (required) elapsed real time trajectory covers, please include units
ensemble: one of [NPT, NVT, NVE, Other]
temperature: (required) in Kelvin, can be N/A
pressure: (required) in Atm, can be N/A  
solvent: (required) can also be none or vacuum
salinity: (optional) in Molar
forcefields: (required) List of forcefields, can be simple names
    - FF 1
    - ...
references: (optional) List of referfences
    - ref1
    - ref2
```
