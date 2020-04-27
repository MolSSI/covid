---
title: Contributing Data to the Hub
description: Instructions for Contributing
draft: false
---

<div style="text-align: justify"> 

## Data Publication Indicator System

All data submitted to the website is flagged based on the data's current state of publication.

{{< partial "marker-info-header" >}}

## Data discussion
Data are open for community discussion through the [Github Projects](https://github.com/MolSSI/covid/projects) 
and [Issues](https://github.com/MolSSI/covid/issues"). All discussions will be tagged so they can be seen by the 
review teams and the broader community. 

## Contributing

The COVID-19 Molecular Structure and Therapeutics Hub gladly accepts any of the types of data hosted on the website 
(and others if you propose a schema). Simply open a Pull Request on the [Github repository](https://github.com/MolSSI/covid) 
with the data you wish to submit  following the Schema in each of the `/data/{TYPE}/README.md` files.
Data is submitted as YAML files into the `/data/{TYPE}/README.md` directory.

A new YAML file should be created for *every* new piece of data.
Upon opening the pull request, submitted files will be automatically validated against the appropriate schemas. If a 
failure occurs during validation, please check the logs to determine the cause of the failure.

This structure is subject to change, but all changes will be made by a maintainer and the instructions 
updated accordingly.

## Contributing large files (disk space) and large datasets (number of entries)

If you have data such as multi-GB trajectories, million entry AI training molecules, or other "large" 
data not suitable for manual entry or storage on GitHub  Please fill out 
[this Form](https://docs.google.com/forms/d/e/1FAIpQLSf1gtN4yts8D9QfQlnZUWpjHvs86Zgz3AJHmTug-ehpYYiGPA/viewform?usp=sf_link)
so we can get in touch with you and figure out the best way to upload your data to the site. We may simply 
link out to your data if its hosted somewhere, or we may coordinate transferring the data to our servers 
so we can link to it there (you retain full rights!)

## Data Curation Teams

The Hub is actively looking for people willing to help curate and review data as it comes in. Specifically, 
we need people willing to contribute some time to look over submissions in the each of the major categories:
* Targets
* Structures
* Models
* Therapeutics
* Simulations
* Website Information

Duties are to look over data and give an assessment as to relative usefulness in expanding research into the 
SARS-CoV-2 virus. The discussions are meant to happen on the issues on the 
[GitHub Issue Tracker](https://github.com/MolSSI/covid/issues) and grouped by tags. 
These reviews differ from a standard journal publication review in a few ways: The reviews are not 
blinded nor double blinded, the reviews and discussions are held in a public space, data do not have to 
be supported by written publication. However, the review process itself helps reinforce that data coming 
into the site from the community has been approved by that same community is hopes to serve.

Please contact a site maintainer if you are willing to help contribute your expertise to helping on one of the 
review teams!<!--[teams](/teams)!-->

## Contributing Non-Scientific Efforts and Website Changes

The Hub is more than just the data: its a community *driven* website and all the resources needed to power that 
as well. If you have suggestions or comments about the website design and how to make it better, let us know 
on the [Github repository](https://github.com/MolSSI/) where the data from this website is pulled from!

Are you an expert in Hugo, Static Web pages, or UX and want to help make this site better? Reach out to us, ping the 
GitHub. We'd love feed back on how we can make this Hub a better experience for its visitors.
