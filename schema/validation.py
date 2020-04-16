from pydantic import BaseModel, ValidationError, validator, AnyUrl, StrictInt, create_model
from typing import Optional, List, Union, Dict
from yaml import safe_load
from enum import Enum
from os import walk
from os.path import join


def build_file_list(walk_dir):
    file_names = []
    for (_, _, names) in walk(join("../data", walk_dir)):
        file_names.extend(names)
    return file_names


def filter_files(strings, substr):
    """ Function to filter for strings that contain one or more of the substrings.

    This function returns a list of strings that contain at least one of the strings from the list substr.

    Parameters
    ----------
    string : List[str]
        A list containing the strings to be filtered.

    substr : List[str]
        A list of substrings to look for in the strings.
    """
    return [x for x in strings if any(sub in x for sub in substr)]


# Build out valid proteins and valid subunits
class StrEnum(str, Enum):
    pass


protein_files = filter_files(build_file_list('proteins'), ['yml', 'yaml'])
protein_dict = {}
subunit_master = {}
for file in protein_files:
    with open(join('../data', 'proteins', file)) as f:
        y = safe_load(f)
    protein_name = y['protein']
    protein_dict[protein_name] = protein_name
    # Handle Subunits
    if 'subunits' in y and y['subunits'] is not None:
        subunit_master[protein_name] = y['subunits']
ValidProteins = StrEnum('ValidProteins', protein_dict)
protein_subunits_entry = Optional[Dict[ValidProteins, Dict[str, List[str]]]]


def check_subunits_are_of_protein_and_valid(v, values):
    """Helper function for protein subunits"""
    # Cycle through dict
    for protein, subunits in v.items():
        if protein != values['proteins'] and protein not in values['proteins']:
            raise ValueError(f'Protein Subunit {protein} is not also in the list of proteins for this molecule!')
        # Ensure every subunit key is valid, ensure every subunit value of each key is valid
        if protein not in subunit_master:
            raise ValueError(f'Protein {protein} does not have subunits defined but it was attempted to be '
                             f'used here!')
        subunit_dict = subunit_master[protein]
        for subunit_category, subunits_values in subunits.items():
            if subunit_category not in subunit_dict:
                raise ValueError(f'Protein {protein}\'s does not have a {subunit_category}!, valid options for '
                                 f'this protein are: {subunit_dict.keys()}')
            master_subunit_set = set(subunit_dict[subunit_category])
            current_subunit_set = set(subunits_values)
            in_current_not_master = current_subunit_set - master_subunit_set
            if in_current_not_master:
                raise ValueError(f'Protein {protein}\'s subunit category of {subunit_category} does not have '
                                 f'the subunits: {in_current_not_master}! Valid options for this subunit category '
                                 f'are {master_subunit_set}')
    return v


class ValidTargets(str, Enum):
    spike_binding = 'spike binding'
    spike_cleavage = 'spike cleavage'
    viral_replication = 'viral replication'
    Pro3CL_protease_activity = '3CLpro protease activity'
    PLpro_protease_activity = 'PLpro protease activity'
    viral_fusion = 'viral fusion'
    host_immune_response = 'host immune response'
    cell_cyle_inhibitors = 'cell cycle inhibitors'


class ValidOrganisms(str, Enum):
    human = 'human'
    sars_cov = 'SARS-CoV'
    sars_cov_2 = 'SARS-CoV-2'


class ValidInterest(str, Enum):
    active = 'active'
    low = 'low'


class ResourcesEnum(str, Enum):
    structures = 'structures'
    models = 'models'


class ValidSimulations(str, Enum):
    docking = 'docking'
    md = 'md'
    mc = 'mc'
    mdcg = 'mdcg'
    mdmc = 'mdcm'


class ValidEnsembles(str, Enum):
    NPT = 'NPT'
    NVT = 'NVT'
    NVE = 'NVE'
    Other = 'Other'


class LinkOutKeys(BaseModel):
    wikipedia: Optional[str]
    drugbank: Optional[str]
    pubchem: Optional[str]
    chemspider: Optional[str]


class LinksModel(BaseModel):
    name: str
    url: AnyUrl
    description: str
    organization: Optional[str]
    institution: Optional[str]
    lab: Optional[str]
    resources: Union[ResourcesEnum, List[ResourcesEnum]]


class ModelsModel(BaseModel):
    name: str
    description: str
    url: AnyUrl
    pdb_url: Optional[AnyUrl]
    pdbids: List[str]
    proteins: List[ValidProteins]
    creator: str
    organization: Optional[str]
    institution: Optional[str]
    lab: Optional[str]
    rating: Optional[StrictInt]

    @validator('rating')
    def rating_valid(cls, v):
        if v is not None:
            if v < 1 or v > 5:
                raise ValueError(f'Rating must be on domain [1,5], is {v}')
        return v


class MoleculesModel(BaseModel):
    name: str
    description: str
    therapeutic: Union[str, List[str]]
    target: Union[ValidTargets, List[ValidTargets]]
    proteins: Optional[Union[ValidProteins, List[ValidProteins]]]
    protein_subunits: protein_subunits_entry
    links: Optional[LinkOutKeys]
    url: Optional[AnyUrl]

    @validator('protein_subunits')
    def subunits_are_of_protein_and_valid(cls, v, values, **kwargs):
        return check_subunits_are_of_protein_and_valid(v, values)


class ProteinsModel(BaseModel):
    protein: str
    organism: ValidOrganisms
    name: str
    interest: ValidInterest
    description: str
    uniprot: Optional[str]
    target: Optional[Union[str, List[str]]]
    subunits: Optional[Dict[str, List[str]]]


class SimulationsModel(BaseModel):
    type: ValidSimulations
    title: str
    description: str
    creator: str
    organization: Optional[str]
    lab: Optional[str]
    institute: Optional[str]
    models: List[str]
    proteins: List[ValidProteins]
    structures: List[str]
    rating: Optional[int]
    files: Optional[List[AnyUrl]]
    trajectory: AnyUrl
    size: str
    length: str
    ensemble: ValidEnsembles
    temperature: float
    pressure: float
    solvent: str
    salinity: float
    forcefields: List[str]
    references: Optional[List[str]]

    @validator('rating')
    def rating_valid(cls, v):
        if v is not None:
            if v < 1 or v > 5:
                raise ValueError(f'Rating must be on domain [1,5], is {v}')
        return v


class StructuresModel(BaseModel):
    pdbid: str
    proteins: Union[ValidProteins, List[ValidProteins]]
    protein_subunits: protein_subunits_entry
    targets: Union[ValidTargets, List[ValidTargets]]
    annotation: Optional[str]
    organisms: Union[ValidOrganisms, List[ValidOrganisms]]
    ligands: Optional[Union[str, List[str]]]
    rating: Optional[StrictInt]

    @validator('rating')
    def rating_valid(cls, v):
        if v is not None:
            if v < 1 or v > 5:
                raise ValueError(f'Rating must be on domain [1,5], is {v}')
        return v

    @validator('protein_subunits')
    def subunits_are_of_protein_and_valid(cls, v, values, **kwargs):
        return check_subunits_are_of_protein_and_valid(v, values)


class TargetsModel(BaseModel):
    target: str
    name: str
    description: str
    proteins: Union[ValidProteins, List[ValidProteins]]
    therapeutic_modalities: Union[str, List[str]]
    protein_subunits: protein_subunits_entry

    @validator('protein_subunits')
    def subunits_are_of_protein_and_valid(cls, v, values, **kwargs):
        return check_subunits_are_of_protein_and_valid(v, values)


class TeamsModel(BaseModel):
    name: str
    members: List[Dict]

    @validator('members')
    def members_valid(cls, v):
        for member in v:
            if 'name' not in member.keys():
                raise ValueError(f'Missing field: name')


class GlossaryModel(BaseModel):
    term: str
    short: str
    long: str
    url: Optional[str]


def validate(filepath, model):
    """Function to perform validation on a file and a model.

    This function takes in a file path to a yaml file and a model. It opens the file and safely loads the yaml file
    into a dictionary. It will only allow simple types currently to avoid arbitrary code execution. The dictionary from
    the yaml file is validated against the given model.

    Parameters
    ----------
    filepath : str
        Path to a yaml file.
    model : BaseModel
        Path to a model that inherits from Pydantic BaseModel

    """
    with open(filepath, 'r') as stream:
        yml_dict = safe_load(stream)
        try:
            model(**yml_dict)
            return 0
        except ValidationError as e:
            print(f"File failed validation: {filepath}")
            print(e)
            print("---")  # Divider line for clarity
            return 1


if __name__ == "__main__":
    # Contains a list of directory names as keys and models as values. Each pair is a directory and the model to
    # validate files within that directory.
    directories = {'links': LinksModel, 'models': ModelsModel, 'molecules': MoleculesModel, 'proteins': ProteinsModel,
                   'simulations': SimulationsModel, 'structures': StructuresModel, 'targets': TargetsModel,
                   'teams': TeamsModel}

    total_errors = 0
    # Iterate over each directory.
    for directory, model in directories.items():

        # Generate a set of files for the given directory.
        f = []
        for (dirpath, dirnames, filenames) in walk(join("../data", directory)):
            f.extend(filenames)

        # Filter out non ".yml" files from the directory
        f_filter = filter_files(f, ["yml"])

        # For each yml file in the directory, perform validation against its associated model.
        for filename in f_filter:
            total_errors += validate(join("../data", directory, filename), model)

    if total_errors:
        raise RuntimeError(f"There were {total_errors} validation errors! Check the log for what")
