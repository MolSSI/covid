# MD simulations relevant to COVID-19 disease

## To add new resources

Contribute a separate [YAML file](https://yaml.org/) for each entry.

### YAML schema

Each entry has the following required and optional keys:
```
simulation: (required)
description: (required)
author: (required)
target: (required)
ensemble: one of [npt, nvt, nve, other]
forcefields: (required)
files: (required)
pdb: (optional)
trajectory: optional
solvent: (optional)
temp: (optional) in kelvin
pressure: (optional) in atm
salinity: (optional)
references: (optional)
```
