# Proteins involved in COVID-19 disease

## To add new resources

Contribute a separate [YAML file](https://yaml.org/) for each entry.

### YAML schema

Each entry has the following required and optional keys:
```
protein: (required)
organism: one of [SARS-CoV-2, SARS-CoV, human]
name: (required)
interest: (required) one of [active, low]
description: (required)
uniprot: (optional)
target: (optional)
subunits: (optional) Dict of {<unit name>: List[proteins/short descriptors]}
```

## Notes
* The `target` field lists one or more drug targeting modalities from the `targets/` data directory
* The `uniprot` field will link to enormously useful information at Uniprot (e.g. [ACE2](https://www.uniprot.org/uniprot/Q9BYF1))
* The `interest` field indicates whether there is `active` interest in this protein with respect to drug discovery purposes, or `low` interest.
