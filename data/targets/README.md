# Therapeutic targeting modalities for COVID-19

## To add new resources

Contribute a separate [YAML file](https://yaml.org/) for each entry.

### YAML schema

Each entry has the following required and optional keys:
```
target: (required unique keyword)
name: (required)
description: (required)
proteins: (required)
protein_subunits: (optional)
    {name_of_protien_from_proteins}:
        {name_of_subunit_category}:
            - subunit 1
            - ...
therapeutic_modalities: one or ore of [small molecule, antibody, peptide, vaccine]
```
