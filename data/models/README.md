# Structural models for COVID-19 targets

## To add new resources

Contribute a separate [YAML file](https://yaml.org/) for each entry.

### YAML schema

Each entry has the following required and optional keys:
```
name: (required)
description: (required)
url: (required) Link to where the model and supporting info can be found
pdb_url: (optional) Link to the physical PDF file the model is contained in (used to render on page), if present
pdbids: (Optional) Valid options are files in /data/structures
  - pdbid1
  - ...
proteins: (required) Valid options in /data/proteins
  - protein id
  - ...
creator: (required) Name of person or group who created it
organization: (optional)
institution: (optional)
lab: (optional) If more information beyond `creator` is requred to properly cite, use this field
rating: (optional) int on range [1,5]. 1=worst, 5=best
publication: (optional) URL of the publication
preprint: (optional) URL of the preprint for the publication. Can also be used to note if submitted to a peer reviewed journal by the exact word "Submitted"
```
