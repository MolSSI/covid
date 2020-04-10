# External links to information resources related to COVID-19

## To add new resources

Contribute a separate [YAML file](https://yaml.org/) for each entry.

### YAML schema

Each entry has the following required and optional keys:
```
pdbid: (required)
protein: (required)
target: (possible options listed)
  - spike binding
  - spike cleavage
  - viral replication
  - 3CLpro protease activity
  - PLpro protease activity
  - viral fusion
ligands: (optional)
annotation: (required)
rating: (required)
```

**Possible Tag Options:**

| **protein**  | **pdb_id**  | **therapeutic**   | **organism**   | **validation**   | **organization**   | **campaign**   | **target**   | **clinical_stage**   | **data_type**   | **method**   |  **resolution**   | **publication_doi**   | **pdb_doi**|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| `spike` `RBD` `S1` `S2` `ACE2` `NSP1` `NSP2` `NSP3` `NSP4` `NSP5` `NSP6` `NSP7` `NSP8` `NSP9` `NSP10` `NSP11` `NSP12` `NSP13` `NSP14` `NSP15` `fusion core` `HR1` `HR2` `TMPRSS2` `3CLpro` `PLpro` `RdRP`  |   |`antibody` `small molecule` `peptide` `antiviral (broad spectrum)` `antiviral (non-specific)` `antiviral (antiretroviral)` `antiviral (other)` `antimalarial` `antibiotic` `antiparasites` `anti-inflammatory` `kinase inhibitors` `others` `immunosuppressive` `protein binder` `vaccine` `immunotherapy`   | `Host` `Viral` `SARS-CoV-2` `SARS`  | `Neutralization` `Pseudovirus Infection` `Mouse Challenge` `Patient Monoclonal` `Crystal Soaks` `Computational Screen`   | `DiamondMX` `F@h` `Coronavirus Structural Biology Task Force`  | `COVID-19 Moonshot`  | `spike binding` `spike cleavage` `viral replication` `3CLpro protease activity` `PLpro protease activity` `viral fusion` `host immune response` `cell cycle inhibitors`  | `Phase I` `Phase II` `Phase III` `HIV Drug`  | `structure` `input files` `structure database`  | `x-ray diffraction` `cryo-EM`  |   |   |   |



## Notes
* The fields provided here are necessary to cross-link data among categories.
* Information that can be fetched directly from the PDB via the `pdbid` does not need to be populated.
  Only annotation information is needed. The rest can be scraped from the PDB via the API or by retrieving the PDB file.
  This includes resolution, method, name, publication DOI.
* `data_type` is not needed because the directory organization will identify that this is a structure.
* `organism` is not needed because the `protein` tag uniquely identifies an organism
