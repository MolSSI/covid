# Analysis relevant to COVID-19 disease

## To add new resources

Contribute a separate [YAML file](https://yaml.org/) for each entry.

### YAML schema

Each entry has the following required and optional keys:
```
title: (required)
description: (required)
creator: (required)
organization: (optional)
lab: (optional)
institute: (optional)
models: (required) must point to model in `models` dir
    - modelname_1
    - ...
proteins: (required) must be a valid protein (see `proteins` dir) 
    - protein_1
    - ...
structures: (required) must point to structure which could be in `structure` dir
    - structure_1
    - ...
molecule: (optional) must point to a valid molecule which could be in `molecules` dir
    - molecule_1
    - ...
rating: (optional) int on domain [1,5], 5 is better
input_files: (required) URLs to input files needed to run `compute_files`
    - file_1
    - ...
compute_files: (required) URLs to executable files that run the computational analysis
    - file_1
    - ...
output_files: (optional) URLs to output files produced by `compute_files`
    - file_1
    - ...
dependencies: (required) list of software/code/language dependencies along with (optionally) version specification e.g. `numpy >= 1.16.3`
    - dependency_1 >= X.X.X
    - ...
references: (optional) List of references associated with the programs and methods you want to mention. For publications tied to this exact simulation, use the `publicaton` and `preprint` categories
    - ref1
    - ref2
publication: (optional) URL of the publication which includes THIS simulation
preprint: (optional) URL of the preprint for the publication. Can also be used to note if submitted to a peer reviewed journal by the exact word "Submitted"
```
