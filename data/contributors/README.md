# People who have contributed to the site

## To add new resources as a top level organization

Contribute a separate [YAML file](https://yaml.org/) for each entry.

Right now all the contributors are on a master list in the `people.yml` file.

### YAML schema

Each entry has the following required and optional keys:
```
name: (required) Top level grouping name (can be blank)
members: (required) A list of...
    - name: (required) Contributor's name
      url: (optional) A URL link to associate with the contributor
      organization: (optional) the name of the orgainzation matching the base file name in /data/orgainzations (i.e. no .yml)
```
