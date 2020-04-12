# Structural models for COVID-19 targets

## To add new resources

Contribute a separate [YAML file](https://yaml.org/) for each entry.

### YAML schema

Each entry has the following required and optional keys:
```
name: (required)
description: (required)
url: (required) Link to where the model and supporting info can be found
pdb_url: Link to the physical PDF file the model is contained in (used to render on page)
pdbids: (required)
  - pdbid1
  - ...
proteins: (required) Valid options in /data/proteins
  - protein id
  - ...
creator: (required) Name of person or group who created it
organization: (optional)
institution: (optional)
lab: (optional) If more information beyond `creator` is requred to properly cite, use this field
resources: one or more of [structures, models]
rating: (optional) int on range [1,5]. 1=worst, 5=best
```
