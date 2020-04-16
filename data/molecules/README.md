# Bioactivity data for molecules (or sets of molecules) against COVID-19 targets or related targets

## To add new resources

Contribute a separate [YAML file](https://yaml.org/) for each entry.

### YAML schema

Each entry has the following required and optional keys:
```
name: (required)
description: (required)

therapeutic: (required, one or more)
target: (required, one or more)
proteins: (required, one or more)
protein_subunits: (optional)
    {name_of_protien_from_proteins}:
        {name_of_subunit_category}:
            - subunit 1
            - ...
links: (optional)
  wikipedia: (optional) omit leading https://en.wikipedia.org/wiki/
  drugbank: (optional) omit leading https://www.drugbank.ca/drugs/
  pubchem: (optional) will be inserted into http://www.chemspider.com/Chemical-Structure.{{ .data.links.chemspider }}.html
  chemspider: (optional) omit leading https://pubchem.ncbi.nlm.nih.gov/compound/
mechanism: (optional) description of how this drug attacks the targets
url: (optional) URL to drug data, if none of the above link options are acceptable
```
