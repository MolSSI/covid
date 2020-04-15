# External links to information resources related to COVID-19

## To add new resources

Contribute a separate [YAML file](https://yaml.org/) for each entry.

### YAML schema

Each entry has the following required and optional keys:
```
pdbid: (required)
proteins: (one or more of the following options)
  - spike
  - RBD
  - S1
  - S2
  - ACE2
  - NSP1
  - NSP2
  - NSP3
  - NSP4
  - NSP5
  - NSP6
  - NSP7
  - NSP8
  - NSP9
  - NSP10
  - NSP11
  - NSP12
  - NSP13
  - NSP14
  - NSP15
  - fusion core
  - HR1
  - HR2
  - TMPRSS2
  - 3CLpro
  - PLpro
  - RdRP
  - ORF3a
  - ORF6
  - ORF8
  - ORF7b
  - ORF10
  - M protein
targets: (one or more of the following options)
  - spike binding
  - spike cleavage
  - viral replication
  - 3CLpro protease activity
  - PLpro protease activity
  - viral fusion
  - host immune response
  - cell cycle inhibitors
annotation: (optional) Otherwise will be set to RCSB PDB Title
rating: (optinal) (1= poor quality to 5=best quality)
organisms: (required) (one or more fo the following options as a list)
  - SARS-CoV-2
  - SARS-CoV
  - human
ligands: (optional)
```

## Notes
* The fields provided here are necessary to cross-link data among categories.
* Information that can be fetched directly from the PDB via the `pdbid` does not need to be populated.
  Only annotation information is needed. The rest can be scraped from the PDB via the API or by retrieving the PDB file.
  This includes resolution, method, name, publication DOI.
* `data_type` is not needed because the directory organization will identify that this is a structure.
