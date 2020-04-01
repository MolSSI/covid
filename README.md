# COVID-19 Molecular Mechanics Exchange (CoVMME)

![MolSSI and the Community VS. COVID-19](repo_management/MolSSI-Logo-covid.png "MolSSI and the Community VS. COVID-19")

A community data repository and curation service for Molecular Mechanics (MM) and Molecular Dynamics (MD) 
related computations for research into the SARS-CoV-2 / COVID-19 / ”Coronavirus” pandemic maintained 
by The Molecular Sciences Software Institute (MolSSI). 
This virus has spurred the entire scientific world into action looking for treatments and answers to 
help minimize its spread, its symptoms, and its fatalities. 
To help researchers and the community quickly provide their resources and expertise, 
this repository is meant to serve as a curated central repository of MM and MD input files, 
trajectories, analysis scripts, well-validated algorithms, and related data for immediate community 
access.

This project may serve as a prototype into a future, more general Molecular Mechanics Exchange of Data 
project. There may come a time as this project evolves that it naturally does become more general (or 
change to another specific focus), however, this project focuses on the SARS-CoV-2 pandemic for now and 
future evolutions can dealt with as they arise. 

## [Go to the Website](https://molssi.github.io/CoVMME/)

## A Central Reference for Community Simulation Data

The nature of this pandemic requires rapid, and flexible response. This repository, and the data 
within are designed to get the information out quickly. The repo seeks to provide the following information
in a centralized location:

* Provide Simulation input files (structures, configurations, scripts, Jupyter notebooks) 
  to the community in an organized structure. Sorting done by Research Group, Target (spike protein, protease, etc), 
  Simulation Program, Hardware/platform (cluster, cloud, local, etc).
* Provide Trajectories to the community for analysis. Due to the nature of the trajectories’ sizes, 
  we may only be able to provide pointers to the trajectories where possible. As the data, repository, 
  and available resources evolve, MolSSI may be able to provide a central location for full trajectories
  in the future.
* Provide analysis files and quantitative numbers associated with inputs and trajectories.
* Pointers to preprint servers such as arXiv, bioRxiv, and ChemRxiv on biomolecular simulation research in regards 
  SARS-CoV-2.
* Where appropriate, well-validated and easily deployable algorithms such as functional Monte Carlo, machine 
  learning methods, and heuristic property calculators.
  
This exchange is a community resource as well as community driven tool. Suggestions as to changes for 
the folder structure, types of content accepted, regulation of the content, etc. are all welcome and 
encouraged through issues and pull requests.

## Types of Data Stored

The following classes of data are accepted in the Exchange currently (Note: This is a **flexible** and 
 broad list. New suggestions can be made through issues). Please note that all data in each category 
 should have the subsequent information associated with it to be accepted. All submissions should also 
 have contributing information in the form of a README.md

* Structures
    * Provenance of structure including any modifications made. Will accept manually written provenance. 
      If modifications made by program, please include script along with pre-modified files and list of required 
      programs to re-generate.
* Simulation Configuration Files
    * Programs required to run (minimal subset which gets all dependencies, with minimal versions), 
    * Basic script and/or working instructions to execute these configuration files, 
    * Structure files (required for non-internet accessible structures, e.g. not required for things on the 
      [Protien Data Bank](https://www.rcsb.org/))
* Program Structure Files - Structures formatted uniquely for a specific simulation program or run 
    * Same requirements as Simulation Configuration Files
* Analysis Data 
    * Complete set of any of the previous data and exact details for replication
    * Analysis scripts with placeholders for output trajectory files.
    * Pointers to the trajectories if possible
* Trajectories - Not accepted in their entirety to the GitHub repository, 
    * Pointers will be accepted and noted. (contact information, where it’s stored, how to request, URLs, etc)
    * Program used to generate this trajectory.
    * Structures (or links there to) which were used to initiate the simulation which yielded this trajectory.
    * Config files and or scripts which were used to run the simulation that generate the trajectory (if possible)
* Papers - as links
    * Links to preprints and publications
    * Inclusion of the files for the paper if they fall into the other categories above.
    * Notation of any simulation package or software used to get the data in the paper
    * Papers from multiple groups should be added in multiple folders (see [Contributing](#contributing) below)
* Movies - hyperlinks only, please do not include full movie files.
    * Links to long term-hosted movies (e.g. YouTube).
    * Structures (or links there to) which were used to initiate this movie.
    * Config files and or scripts which were used to run the simulation that generate the trajectory (if possible)
    * The trajectory which this movie references (if possible, see rules on Trajectories above)
* Algorithms - Well-validated and easily deployable algorithms such as functional Monte Carlo and machine learning methods and heuristic property calculators
    * Code Snippets
    * Programing Language (if restricted)
    * List of required software and minimal dependencies (if any)

Due to the rapidly evolving nature of this exchange, organization and requirements may change with time. However, 
no changes to the repository will remove user-submitted data. The maintainers may reach out to the original 
contributor to ask for additional information as needed.  


## Contributing

The exchange gladly accepts any of the above types of data (and others if you propose an organization). 
Simply open a PR with the data you wish to submit with the following folder structure (omit any directories 
for types you are not submitting):

```
sorted_by_group
└──YOUR_GROUP_NAME
   ├── README.md
   └── TARGET
       ├── algorithms
       ├── analysis
       ├── movies
       ├── papers
       ├── program_specific_structures
       │   └── SIMULATION_SOFTWARE
       ├── simulation_configs
       │   └── SIMULATION_SOFTWARE
       ├── structures
       └── trajectories
           └── SIMULATION_SOFTWARE
```

Create a folder for your group within the `sorted_by_group` directory. This will serve as the main storage location for all of your submissions. Within this folder, create a README.md file and include information about your contributing group(s):
* Author: The user(s) who produced the data associated with the submission.
* Group: The group(s) of the author(s) of the submission.
* Organization: The organization(s) of the author(s).
* Reference_Information: If desired, include websites for the associated groups.
* Contact_Information: If desired, include ways that the author(s) can be contacted about their submission.

Note that for submissions by collaborations of multiple groups, create a folder within the `sorted_by_group` folder for your collaboration. Within the README.md include all authors and groups associated with this collaboration.

For each new submission made the the repository, please create a folder, within your groups folder, with a unique `SUBMISSION_ID` as its name. Ideally, submission names should represent the order of submissions, allowing each submission to be processed in the order it is received.

Each submission should include a folder representing the `TARGET` of the submission and a `README.md` for the submission. The `TARGET` folder should be named to represent the target type of your submission. We ask that you include all fields under Contributor Information above along with information requested for the type of data in your submission.
Within the `TARGET` folder, create a subfolder for each type of data within this submission. These folders should contain all relevant files to the data types along with any meta data, such as provenance information, for the data.

(Not required) If possible, please also create symlinks in the folders of the root directory as well. If you do not 
wish to, symlinks will be created for each of the other folders in the root directory of the exchange by a maintainer.
The current plan is to move 

This structure is subject to change, but all changes will be made by a maintainer and the instructions 
updated accordingly.

## Exchange Maintainers 

* [The Molecular Sciences Software Institute (MolSSI)](molssi.org)
* [Levi N. Naden (MolSSI)](https://github.com/lnaden)
* [Sam Ellis (MolSSI)](https://github.com/sjayellis)
* [Andrew Abi-Mansour (MolSSI)](https://github.com/Andrew-AbiMansour)
