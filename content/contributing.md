---
title: Contributing Data to the Exchange
description: Instructions for Contributing
draft: false
---

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

(Not required) If possible, please also create symlinks in the folders of the root directory as well. If you do not 
wish to, symlinks will be created for each of the other folders in the root directory of the exchange by a maintainer.
The current plan is to move 

This structure is subject to change, but all changes will be made by a maintainer and the instructions 
updated accordingly.