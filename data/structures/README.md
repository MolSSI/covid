# External links to information resources related to COVID-19

## To add new resources

Contribute a separate [YAML file](https://yaml.org/) for each entry.

### YAML schema

Each entry has the following required and optional keys:
```
pdbid: (One of this or unpublished_pdbid required) Use if on the RCSB, else LEAVE EMPTY
unpublished_pdbid: (One of this or pdbid required) Use if NOT on the RCSB.
    WARNING: If this is set, it will OVERWRITE the pdbid due to technical limiations on constructiong the site
    If this is ever fixed upstream, this behavior will be reverted (and this key likely removed and foled into pdbid)
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
  - Helicase
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
publication: (optional) URL of the publication if not fetchable from RCSB (RCSB prioritized)
preprint: (optional) URL of the preprint for the publication. Can also be used to note if submitted by the exact word "Submitted"
```

## Notes
* The fields provided here are necessary to cross-link data among categories.
* Information that can be fetched directly from the PDB via the `pdbid` does not need to be populated.
  Only annotation information is needed. The rest can be scraped from the PDB via the API or by retrieving the PDB file.
  This includes resolution, method, name, publication DOI.
* `data_type` is not needed because the directory organization will identify that this is a structure.
