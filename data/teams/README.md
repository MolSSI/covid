# Data curation and review teams

## To add new resources

Contribute a separate [YAML file](https://yaml.org/) for each entry.

### YAML schema
First, populate the people.yml file with any missing people from your team, with the following required and optional keys:
```
lab: (required lab / institution)
members:
  - name: (required)
    url: (optional)
    twitter: (optional)
    email: (optional)
  - ...


```
Then, each team entry has the following required and optional keys:
```
name: (required team name)
members:
  - name: (required)
    role: (optional)
  - ...

```
