# Organizations for common reference

## To add new resources

Contribute a separate [YAML file](https://yaml.org/) for each entry.

### YAML schema

Each entry has the following required and optional keys:
```
name: (required) Organization Name
short: (optional) Short name or acronym if people want it
logo: (optional) name of the logo file in the /static/images/org-logos directory
url: (optional) Link to the organization
endorsement_logo: (optional) Indicates that this org is endorsing the Hub, and then uses this logo path in /static/images/org-logos
```

### Visual Display Caveat

The logo for the organization, when referenced on the Collaborators page will be scaled to 57x43, 
but aspect ratios are preserved.
Please make sure your logo is appropriate at that scale (you can use the site preview when you make a
PR to check this).

The `endorsement_logo` is also scaled, but not to a size where visibility should be an issue.

If your logo cannot be rendered at that size or makes the quality unacceptable, please not that in an 
issue and we can work to resolve it together.
