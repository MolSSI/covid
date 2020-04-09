---
title: MolSSI and BioExcel COVID-19 Computational Molecular Data Exchange
description: What is This Exchange?
draft: false
---

![MolSSI, BioExcel, and the Community VS. COVID-19](/images/MolSSI-BioExcel-covid.png "MolSSI, BioExcel, and the Community VS. COVID-19")

This is all subject to change, its placeholder

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

## [Go to the Website](https://covid.molssi.org)

## A Central Reference for Community Simulation Data

The nature of this pandemic requires rapid, and flexible response. This repository, and the data 
within are designed to get the information out quickly. The repo seeks to provide the following information
in a centralized location:

* Provide Simulation input files (structures, configurations, scripts, Jupyter notebooks) 
  to the community in an organized structure. Sorting done by Research Group, proteins (spike protein, protease, etc), 
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

The following classes of data are currently accepted in the Exchange (Note: This is a **flexible** and 
 broad list. New suggestions can be made through [issues](https://github.com/MolSSI/CoVMME/issues)). Please note that all data in each category should have the subsequent information associated with it to be accepted. All submissions should also 
 have contributing information in the form of a README.md

* Structures
    * Provenance of structure including any modifications made. Will accept manually written provenance. 
      If modifications made by program, please include script along with pre-modified files and list of required 
      programs to re-generate.
* Simulation Configuration Files
    * Programs required to run (minimal subset which gets all dependencies, with minimal versions), 
    * Basic script and/or working instructions to execute these configuration files, 
    * Structure files (required for non-internet accessible structures, e.g. not required for things on the 
      [Protein Data Bank](https://www.rcsb.org/))
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