# Bioactivity data for molecules (or sets of molecules) against COVID-19 targets or related targets

## To add new resources

Contribute a separate [YAML file](https://yaml.org/) for each entry.

### YAML schema

Each entry has the following required and optional keys:
```
name: (required)
description: (required)
url: (required)
therapeutic: (required, one or more)
target: (required, one or more)
protein: (required, one or more)
links: (optional)
  wikipedia: (optional) omit leading https://en.wikipedia.org/wiki/
  drugbank: (optional) omit leading https://www.drugbank.ca/drugs/
  pubchem: (optional) will be inserted into http://www.chemspider.com/Chemical-Structure.{{ .data.links.chemspider }}.html
  chemspider: (optional) omit leading https://pubchem.ncbi.nlm.nih.gov/compound/

```
