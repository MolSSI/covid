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
target: (optional)
subunits: (optional)
```

## Notes
* The `target` field lists one or more drug targeting modalities from the `targets/` data directory
