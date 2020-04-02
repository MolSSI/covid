# COVID-19 Molecular Mechanics Exchange (CoVMME)

![MolSSI, BioExcel, and the Community VS. COVID-19](repo_management/MolSSI-BioExcel-covid.png "MolSSI, BioExcel, and the Community VS. COVID-19")

A community data repository and curation service for Molecular Mechanics (MM) and Molecular Dynamics (MD) 
related computations for research into the SARS-CoV-2 / COVID-19 / ”Coronavirus” pandemic maintained 
by [The Molecular Sciences Software Institute (MolSSI)](https://molssi.org) and 
[BioExcel](https://bioexcel.eu/). 
This virus has spurred the entire scientific world into action looking for treatments and answers to 
help minimize its spread, its symptoms, and its fatalities. 
To help researchers and the community quickly provide their resources and expertise, 
this repository is meant to serve as a curated central repository of MM and MD input files, 
trajectories, analysis scripts, well-validated algorithms, and related data for immediate community 
access.

This project may serve as a prototype into a future, more general Molecular Mechanics Exchange of Data 
project. There may come a time as this project evolves that it naturally does become more general (or 
change to another specific focus), however, this project focuses on the SARS-CoV-2 pandemic for now and 
future evolutions can be dealt with as they arise.

## Get the Data Now

<center>
<a href="./targets/spike.html" class="btn2">Spike Protien</a>
<a href="./targets/protease.html" class="btn2">Protease(s)</a>
<a href="./targets/membrane.html" class="btn2">Membrane Protein</a>
<a href="./targets/envelope.html" class="btn2">Envelope Protein</a>
<a href="./targets/nucleocapsid.html" class="btn2">Nucleocapsid Protein</a>
</center>

## A Central Reference for Community Simulation Data

The nature of this pandemic requires rapid, and flexible response. This repository, and the data 
within are designed to get the information out quickly. The repo seeks to provide the following information
in a centralized location:

* COVID-19 target proteins (viral and host)
* Structural data (continually updated, prioritized by utility/quality)
* High-quality simulation-ready models (unsolvated and solvated) that correct flaws in structural-data (continually updated, prioritized by quality)
* Input files, simulation ensembles (for ensemble docking), etc. with all info needed for provenance/reproducibility
* Small molecules and antibodies that are known to have affinity/activity for various targets/structures
* Corresponding literature DOIs that are associated with all of the above
* Trajectories are accepted by [filling out the intake form](https://forms.gle/xp8hNXtVK6PPnghe8), or contacting a maintainer directly. Links to trajectories and how to access them with all info needed for provenance
* Where appropriate, well-validated and easily deployable algorithms such as functional Monte Carlo, machine 
  learning methods, and heuristic property calculators.

Any researchers can submit changes via PRs, core teams will review PRs for quality and merge them.
  
This exchange is a community resource as well as community driven tool. Suggestions as to changes for 
the folder structure, types of content accepted, regulation of the content, etc. are all welcome and 
encouraged through issues and pull requests.

## Types of Data Stored

The following classes of data are accepted in the Exchange currently (Note: This is a flexible and broad list. 
New suggestions can be made through [issues](https://github.com/MolSSI/CoVMME/issues)). Please note that all data in each category should have the subsequent 
information associated with it to be accepted. All submissions should also have contributing information included in 
their records.

### Contributor Information

The following information should be included with all submissions

* Author: The user(s) who produced the data associated with the submission.
* Group: The group(s) of the author(s) of the submission.
* Organization: The organization(s) of the author(s).
* Abstract: A short description of the data included in the submission.
* Full Description: If desired, include a more detailed description of the data being submitted and the process used to create it.
* Tags: Include any additional tags and keywords to be associated with the submission.
* Reference: How the information can be cited. Include papers to cite here.
* Licensing information


### Structures

Contributed structures should include any provenance information, such as initial structure, 
any modifications made to the structure, the process by which modifications were made. 
If modifications were performed using a program, please include the relevant script along with pre-modified files, 
and a list of required programs needed to run the script.

### High-quality simulation-ready models

These are subject to the same rules as Structures, but with the addition that all modifications and 
routines should be tracked and recorded. 

### Simulation Configuration Files

Simulation configuration files should include a list of programs required to utilize the configuration files. 
Ideally this will contain the minimal subset of programs that gets all dependencies. Version numbers, either the 
version used or the minimal version that will produce the correct results, should also be included for each program.

Submission should also either a script or a set of working instructions to execute the included configuration files and 
any structure files not available through internet-accessible storage. (subject to the rules of Structures)

### Program Structure Files

Structures formatted uniquely for a specific simulation program or run. 
These require the same information as the Simulation Configuration Files. 

### Analysis Data 

Analysis data should include the complete set of any of the previous data and exact details for replication.
Analysis scripts with placeholders for output trajectory files can be provided if no trajectory is available.
Please include pointers to the trajectories if possible.

### Trajectories

Trajectories are accepted through [filling out the intake form](https://forms.gle/xp8hNXtVK6PPnghe8) and will be 
hosted by the maintainers and you retain full rights. They are not accepted on GitHub directly. You may also submit links to 
trajectories if you are hosting them elsewhere (please provide the same information as is on the 
[intake form](https://forms.gle/xp8hNXtVK6PPnghe8)).

If possible, please also provide any of the previous categories of information along with the Trajectory so they can 
be cross referenced.

### Papers

Papers, preprints, and all other manuscripts are accepted as links to their hosted location. They are not 
accepted on the GitHub repo directly.

If possible, please also provide any of the previous categories of information along with the Trajectory so they can 
be cross referenced.

### Movies 

Movies are accepted as hyperlinks only, please do not include full movie files. 

If possible, please also provide any of the previous categories of information along with the Trajectory so they can 
be cross referenced.

### Algorithms 

Well-validated and easily deployable algorithms such as functional Monte Carlo and machine learning methods and 
heuristic property calculators. Data included should be code snippets, programing language (if restricted), and a list 
of required software and minimal dependencies (if any).


### Disclaimer

Due to the rapidly evolving nature of this exchange, organization and requirements may change with time. However, 
no changes to the repository will remove user-submitted data. The maintainers may reach out to the original 
contributor to ask for additional information as needed.  


## Contributing

SUBJECT TO CHANGE

The exchange gladly accepts any of the above types of data (and others if you propose an organization). 
Simply open a PR with the data you wish to submit with the following folder structure (omit any directories 
for types you are not submitting):

```
sorted_by_group
└──YOUR_GROUP_NAME
   ├── README.md
   └── SUBMISSION_ID
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

Create a folder for your group within the `sorted_by_group` directory. This will serve as the main storage location for all of your submissions. Within this folder, create a `README.md` file and include information about your contributing group(s):
* Author: The user(s) who produced the data associated with the submission.
* Group: The group(s) of the author(s) of the submission.
* Organization: The organization(s) of the author(s).
* Reference_Information: If desired, include websites for the associated groups.
* Contact_Information: If desired, include ways that the author(s) can be contacted about their submission.

Note that for submissions by collaborations of multiple groups, create a folder within the `sorted_by_group` folder for your collaboration. Within the `README.md` include all authors and groups associated with this collaboration.

For each new submission made to the repository, please create a folder, within your groups folder, with a unique `SUBMISSION_ID` as its name. Ideally, submission names should represent the order of submissions, allowing each submission to be processed in the order it is received.

Each submission should include a folder representing the `TARGET` of the submission and a `README.md` for the submission. The `TARGET` folder should be named to represent the target type of your submission. We ask that you include all fields under Contributor Information above along with information requested for the type of data in your submission within the `README.md` file.
Within the `TARGET` folder, create a subfolder for each type of data within this submission. These folders should contain all relevant files to the data types along with any meta data, such as provenance information, for the data.

This structure is subject to change, but all changes will be made by a maintainer and the instructions 
updated accordingly.

## Want to join the collaboration?

MolSSI and BioExcel are working together on this project to de-duplicate efforts and to reach the broadest 
community possible. We are activley looking for other institutes, collaborators, consortia, and anyone who wants 
to be an active contributor to join us! 

Reach out to any of the maintainers below and lets work together to make this as helpful as possible!  

## Exchange Maintainers 

* [The Molecular Sciences Software Institute (MolSSI)](https://molssi.org)
* [BioExcel](https://bioexcel.eu/)
* [Levi N. Naden (MolSSI)](https://github.com/lnaden)
* [Sam Ellis (MolSSI)](https://github.com/sjayellis)
* [Andrew Abi-Mansour (MolSSI)](https://github.com/Andrew-AbiMansour)
