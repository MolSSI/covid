from pydantic import BaseModel, ValidationError, validator
from typing import Optional, List, Union, Dict
from yaml import safe_load
from os import walk
from os.path import join

class LinksModel(BaseModel):
    name: str
    url: str
    description: str
    organization: Optional[str]
    institution: Optional[str]
    lab: Optional[str]
    resources: Union[str, List]

class ModelsModel(BaseModel):
    name: str
    description: str
    url: str
    pdbids: List[str]
    organization: Optional[str]
    institution: Optional[str]
    lab: Optional[str]
    resources: Union[str, List[str]]

class MoleculesModel(BaseModel):
    name: str
    description: str
    url: str
    therapeutic: Union[str, List[str]]
    target: Union[str, List[str]]
    protein: Union[str, List[str]]
    links: Optional[Dict]
    
    @validator('links')
    def links_valid(cls, v):
        if v is None:
            return v
        else:
            for key, value in v.items():
                if key not in ['wikipedia', 'drugbank', 'pubchem', 'chemspider']:
                    raise ValueError(f'{key} not valid site link.')

class ProteinsModel(BaseModel):
    protein: str
    organism: str
    name: str
    interest: str
    description: str
    uniprot: Optional[str]
    target: Optional[Union[str, List[str]]]
    subunits: Optional[str]

    @validator('interest')
    def interest_valid(cls, v):
        if v in ['active', 'low']:
            return v
        else:
            raise ValueError(f'{v} is not a valid interest type.')

    @validator('organism')
    def organism_valid(cls, v):
        if v in ['SARS-CoV-2', 'SARS-CoV', 'human']:
            return v
        else:
            raise ValueError(f'{v} is not a valid organism type.')
    
class SimulationsModel(BaseModel):
    simulation: str
    name: str
    description: str
    url: str
    type: str
    
    @validator('type')
    def type_valid(cls, v):
        if v in ['docking', 'md', 'mc', 'cg']:
            return v
        else:
            raise ValidationError(f'{v} not a valid simulation type.')
    
class StructuresModel(BaseModel):
    pdbid: str
    proteins: Union[str, List[str]]
    targets: Union[str, List[str]]
    annotation: str
    rating: int
    organisms: Union[str, List[str]]
    ligands: Optional[Union[str, List[str]]]
    
    @validator('proteins')
    def proteins_valid(cls, v):
        valid_proteins = ['spike', 'RBD', 'S1', 'S2', 'ACE2', 'NSP1', 'NSP2', 'NSP3', 'NSP4', 'NSP5', 'NSP6', 'NSP7', 'NSP8', 'NSP9', 'NSP10', 'NSP11', 'NSP12', 'NSP13', 'NSP14', 'NSP15', 'fusion core', 'HR1', 'HR2', 'TMPRSS2', '3CLpro', 'PLpro', 'RdRP']
        if isinstance(v, str):
            if v in valid_proteins:
                return v
            else:
                raise ValueError(f'{v} not a valid protein type.')
        elif isinstance(v, list):
            invalid_items = []
            for item in v:
                if item not in valid_proteins:
                    invalid_items.append(item)
            if invalid_items:
                raise ValueError(f'{invalid_items} are not valid protein types.')
                
    @validator('targets')
    def targets_valid(cls, v):
        valid_targets = ['spike binding', 'spike cleavage', 'viral replication','3CLpro protease activity', 'PLpro protease activity', 'viral fusion', 'host immune response', 'cell cycle inhibitors']
        if isinstance(v, str):
            if v in valid_targets:
                return v
            else:
                raise ValueError(f'{v} not a valid target type.')
        elif isinstance(v, list):
            invalid_items = []
            for item in v:
                if item not in valid_targets:
                    invalid_items.append(item)
            if invalid_items:
                raise ValueError(f'{invalid_items} are not valid target types.')
                
    @validator('organisms')
    def organism_valid(cls, v):
        valid_organisms = ['SARS-CoV-2', 'SARS-CoV', 'human']
        if isinstance(v, str):
            if v in valid_organisms:
                return v
            else:
                raise ValueError(f'{v} not a valid organism type.')
        
        elif isinstance(v, list):
            invalid_items = []
            for item in v:
                if item not in valid_organisms:
                    invalid_items.append(item)
            if invalid_items:
                raise ValueError(f'{invalid_items} are not valid organism types.')
    
class TargetsModel(BaseModel):
    target: str
    name: str
    description: str
    proteins: Union[str, List[str]]
    therapeutic_modalities: Union[str, List[str]]
    
    @validator('proteins')
    def proteins_valid(cls, v):
        valid_proteins = ['spike', 'RBD', 'S1', 'S2', 'ACE2', 'NSP1', 'NSP2', 'NSP3', 'NSP4', 'NSP5', 'NSP6', 'NSP7', 'NSP8', 'NSP9', 'NSP10', 'NSP11', 'NSP12', 'NSP13', 'NSP14', 'NSP15', 'fusion core', 'HR1', 'HR2', 'TMPRSS2', '3CLpro', 'PLpro', 'RdRP']
        if isinstance(v, str):
            if v in valid_proteins:
                return v
            else:
                raise ValueError(f'{v} not a valid protein type.')
        elif isinstance(v, list):
            invalid_items = []
            for item in v:
                if item not in valid_proteins:
                    invalid_items.append(item)
            if invalid_items:
                raise ValueError(f'{invalid_items} are not valid protein types.')
                
    @validator('therapeutic_modalities')
    def therapeutics_valid(cls, v):
        valid_therapeutics = ['small molecule', 'antibody', 'peptide', 'vaccine']
        if isinstance(v, str):
            if v in valid_therapeutics:
                return v
            else:
                raise ValueError(f'{v} not a valid therapeutic modality.')
        elif isinstance(v, list):
            invalid_items = []
            for item in v:
                if item not in valid_therapeutics:
                    invalid_items.append(item)
            if invalid_items:
                raise ValueError(f'{invalid_items} are not valid therapeutic modalities.')
    
class TeamsModel(BaseModel):
    name: str
    members: List[Dict]
    
    @validator('members')
    def members_valid(cls, v):
        for member in v:
            if 'name' not in member.keys():
                raise ValueError(f'Missing field: name')
                
    
def filter_yaml(string, substr):
    """ Function to filter for strings that contain one or more of the substrings.
    
    This function returns a list of strings that contain at least one of the strings from the list substr.
    
    Parameters
    ----------
    string : List[str]
        A list containing the strings to be filtered.
        
    substr : List[str]
        A list of substrings to look for in the strings.
    """
    return [str for str in string if
             any(sub in str for sub in substr)]
             

def validate(filepath, model):
    """Function to perform validation on a file and a model.
    
    This function takes in a file path to a yaml file and a model. It opens the file and safely loads the yaml file into a dictionary. It will only allow simple types currently to avoid arbitrary code execution. The dictionary from the yaml file is validated against the given model.
    
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
        except ValidationError as e:
            print(f"File failed validation: {filepath}")
            print(e.json())

if __name__ == "__main__":
    # Contains a list of directory names as keys and models as values. Each pair is a directory and the model to validate files within that directory.
    directories = {'links': LinksModel, 'models': ModelsModel,'molecules': MoleculesModel, 'proteins': ProteinsModel, 'simulations': SimulationsModel, 'structures': StructuresModel, 'targets': TargetsModel, 'teams': TeamsModel}
    
    # Iterate over each directory.
    for directory, model in directories.items():
        
        # Generate a set of files for the given directory.
        f = []    
        for (dirpath, dirnames, filenames) in walk(join(".", directory)):
            f.extend(filenames)
        
        # Filter out non ".yml" files from the directory
        f_filter = filter_yaml(f, ["yml"])
        
        # For each yml file in the directory, perform validation against its associated model.
        for filename in f_filter:
            validate(join(".", directory, filename), model)