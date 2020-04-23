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
therapeutic_modalities: one or ore of [small molecule, antibody, peptide, vaccine]
papers: (optional) List of 
    - title: First paper title
      doi: First paper DOI (optional, but at least one of this OR pmid is required, both accepted)
      pmid: First paper PubMed ID (optional, at least one of this OR doi is required, both accepted)
    - title: ...
      doi: ...
      pmid: ...
```
