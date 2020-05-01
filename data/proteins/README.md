# Proteins involved in COVID-19 disease

## To add new resources

Contribute a separate [YAML file](https://yaml.org/) for each entry.

### YAML schema

Each entry has the following required and optional keys:
```
protein: (required)
organism: one of [SARS-CoV-2, SARS-CoV, human]
name: (required)
description: (required)
uniprot: (optional)
target: (optional)
subunits: (optional) Dict of {<unit name>: List[proteins/short descriptors]}
domain: (required if SARS-CoV-2 or SARS-CoV, optional if human) one of [nsp, spike, membrane, envelope, nucleocapsid, orf]
```

## Notes
* The `target` field lists one or more drug targeting modalities from the `targets/` data directory
* The `uniprot` field will link to enormously useful information at Uniprot (e.g. [ACE2](https://www.uniprot.org/uniprot/Q9BYF1))
* The `domain` filed indicates what subunit of the viral protein categories the protein falls under.
