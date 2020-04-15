---
title: Contributing Data to the Hub
description: Instructions for Contributing
draft: false
---

## Contributing

The exchange gladly accepts any of the types of data hosted on the website (and others if you propose a schema). 
Simply open a Pull Request on the [Github repository](https://github.com/MolSSI/covid) with the data you wish to submit 
following the Schema in each of the `/data/{TYPE}/README.md` files.
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
