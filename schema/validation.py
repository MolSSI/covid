from pydantic import BaseModel, ValidationError, validator, AnyUrl, StrictInt
from typing import Optional, List, Union, Dict
from yaml import safe_load
from enum import Enum
from os import walk
from os.path import join


class ValidProteins(str, Enum):
    spike = 'spike'
    RBD = 'RBD'
    S1 = 'S1'
    S2 = 'S2'
    ACE2 = 'ACE2'
    NSP1 = 'NSP1'
    NSP2 = 'NSP2'
    NSP4 = 'NSP4'
    NSP6 = 'NSP6'
    NSP7 = 'NSP7'
    NSP8 = 'NSP8'
    NSP9 = 'NSP9'
    NSP10 = 'NSP10'
    NSP11 = 'NSP11'
    Helicase = 'Helicase'
    NSP14 = 'NSP14'
    NSP15 = 'NSP15'
    NSP16 = 'NSP16'
    fusion_core = 'fusion core'
    HR1 = 'HR1'
    HR2 = 'HR2'
    TMPRSS2 = 'TMPRSS2'
    Mpro = '3CLpro'
    PLpro = 'PLpro'
    RdRP = 'RdRP'
    BoAT1 = 'BoAT1'
    FcR = 'Fc receptor'
    Furin = 'Furin'
    IL6R = 'IL6R'
    p38 = 'p38'
    ORF3a = 'ORF3a'
    ORF6 = 'ORF6'
    ORF7b = 'ORF7b'
    ORF7a = 'ORF7a'
    ORF8 = 'ORF8'
    ORF10 = 'ORF10'
    M_protein = 'M protein'
    N_protein = 'N protein'
    E_protein = 'E protein'
    PD_1 = 'PD-1'


class ValidDomains(str, Enum):
    """ Valid Protein Domains """
    spike = 'spike'
    nsp = 'nsp'
    orf = 'orf'
    membrane = 'membrane'
    envelope = 'envelope'
    nucleocapsid = 'nucleocapsid'


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


class ResourcesEnum(str, Enum):
    structures = 'structures'
    models = 'models'
    publications = 'publications'
    therapeutics = 'therapeutics'
    biology = 'biology'


class ValidSimulations(str, Enum):
    docking = 'docking'
    md = 'md'
    mc = 'mc'
    mdcg = 'md-cg'
    mdwe = 'md-we'
    mccg = 'mc-cg'

class ValidEnsembles(str, Enum):
    NPT = 'NPT'
    NVT = 'NVT'
    NVE = 'NVE'
    Other = 'Other'


class Submitted(str, Enum):
    submitted = "Submitted"


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
    resources: List[ResourcesEnum]


class ModelsModel(BaseModel):
    name: str
    description: str
    url: AnyUrl
    pdb_url: Optional[AnyUrl]
    pdbids: Optional[List[str]]
    proteins: List[ValidProteins]
    creator: str
    organization: Optional[str]
    institution: Optional[str]
    lab: Optional[str]
    rating: Optional[StrictInt]
    publication: Optional[AnyUrl]
    preprint: Optional[Union[AnyUrl, Submitted]]

    @validator('rating')
    def rating_valid(cls, v):
        if v is not None:
            if v < 1 or v > 5:
                raise ValueError(f'Rating must be on domain [1,5], is {v}')
        return v


class ValidTherapeutic(str, Enum):
    antiviral = "antiviral"
    small_molecule = "small molecule"
    peptide = "peptide"
    immunotherapy = "immunotherapy"
    antibody = "antibody"


class MoleculesModel(BaseModel):
    name: str
    description: str
    therapeutic: List[ValidTherapeutic]
    target: Union[ValidTargets, List[ValidTargets]]
    protein: Optional[Union[ValidProteins, List[ValidProteins]]]
    links: Optional[LinkOutKeys]
    url: Optional[AnyUrl]


class ProteinsModel(BaseModel):
    protein: str
    organism: ValidOrganisms
    name: str
    description: str
    uniprot: Optional[str]
    target: Optional[Union[str, List[str]]]
    subunits: Optional[Dict[str, List[str]]]
    domain: Optional[ValidDomains]

    @validator('domain')
    def domain_is_virus(cls, v, values, **kwargs):
        if v is None and values.get('organism') != 'human':
            raise ValueError("Domains for virus must be set!")
        elif values.get('organism') == 'human' and v is not None:
            raise ValueError(f"Domain is set but Organism is 'human' so does not apply. This could be a case of the "
                             f"wrong organism. If this is a human organism, please unset domain.")
        return v


class SimulationsModel(BaseModel):
    type: ValidSimulations
    title: str
    description: str
    creator: str
    organization: Optional[str]
    lab: Optional[str]
    institute: Optional[str]
    models: Optional[List[str]]
    proteins: List[ValidProteins]
    structures: List[str]
    rating: Optional[int]
    files: Optional[List[AnyUrl]]
    trajectory: AnyUrl
    size: str
    length: str
    ensemble: ValidEnsembles
    temperature: Optional[float]
    pressure: Optional[float]
    solvent: str
    salinity: Optional[float]
    forcefields: List[str]
    references: Optional[List[str]]
    publication: Optional[AnyUrl]
    preprint: Optional[Union[AnyUrl, Submitted]]

    @validator('rating')
    def rating_valid(cls, v):
        if v is not None:
            if v < 1 or v > 5:
                raise ValueError(f'Rating must be on domain [1,5], is {v}')
        return v

    # @validator('pressure')
    # def pressure_valid(cls, v):
        # if isinstance(v, str):
            # if v.equals('N/A'):
                # raise ValueError(f'Pressure must be a valid float or N/A, is {v}')
        # if not isinstance(v, float):
            # raise ValueError(f'Pressure must be a valid float or N/A, is {v}')
        # return v


class StructuresModel(BaseModel):
    pdbid: Optional[str]
    unpublished_pdbid: Optional[str]
    proteins: Union[ValidProteins, List[ValidProteins]]
    targets: Union[ValidTargets, List[ValidTargets]]
    annotation: Optional[str]
    organisms: Union[ValidOrganisms, List[ValidOrganisms]]
    ligands: Optional[Union[str, List[str]]]
    rating: Optional[StrictInt]
    publication: Optional[AnyUrl]
    preprint: Optional[Union[AnyUrl, Submitted]]

    @validator('rating')
    def rating_valid(cls, v):
        if v is not None:
            if v < 1 or v > 5:
                raise ValueError(f'Rating must be on domain [1,5], is {v}')
        return v

    @validator('unpublished_pdbid', pre=True, always=True)
    def at_least_one_of(cls, v, values, **kwargs):
        """
        Ensure at least one of pdbid or unpublished_pdbid is set
        """
        if not values.get('pdbid') and not v:
            raise ValueError("At least one of pdbid or unpublished_pdbid must be set!")
        return v


class PapersModel(BaseModel):
    title: str
    doi: Optional[str]
    pmid: Optional[str]

    @validator('pmid', always=True, pre=True)
    def needs_one_of(cls, v, values, **kwargs):
        """
        Note: order of attributes is important here! always validate against the _last_ key otherwise it wont appear
              in the "values" arg. Its a subtle nuance to how pydantic does its validation population.
        """
        if not values.get('doi') and not v:
            raise ValueError("At least one of doi or pmid must be set!")
        return v


class TargetsModel(BaseModel):
    target: str
    name: str
    description: str
    proteins: Union[ValidProteins, List[ValidProteins]]
    therapeutic_modalities: Union[str, List[str]]
    papers: Optional[List[PapersModel]]


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


class OrganizationModel(BaseModel):
    name: str
    short: Optional[str]
    logo: Optional[str]
    url: Optional[AnyUrl]
    endorsement_logo: Optional[str]


class ContributorMemberModel(BaseModel):
    name: str
    url: Optional[AnyUrl]
    organization: Optional[str]


class ContributorsModel(BaseModel):
    name: Optional[str]
    members: List[ContributorMemberModel]
                
    
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
            return 1


if __name__ == "__main__":
    # Contains a list of directory names as keys and models as values. Each pair is a directory and the model to
    # validate files within that directory.
    directories = {'links': LinksModel,
                   'models': ModelsModel,
                   'molecules': MoleculesModel,
                   'proteins': ProteinsModel,
                   'simulations': SimulationsModel,
                   'structures': StructuresModel,
                   'targets': TargetsModel,
                   'teams': TeamsModel,
                   'glossary': GlossaryModel,
                   'organizations': OrganizationModel,
                   'contributors': ContributorsModel
                   }

    total_errors = 0
    # Iterate over each directory.
    for directory, model in directories.items():

        # Generate a set of files for the given directory.
        f = []
        for (dirpath, dirnames, filenames) in walk(join("../data", directory)):
            f.extend(filenames)

        # Filter out non ".yml" files from the directory
        f_filter = filter_yaml(f, ["yml"])

        # For each yml file in the directory, perform validation against its associated model.
        for filename in f_filter:
            total_errors += validate(join("../data", directory, filename), model)

    if total_errors:
        raise RuntimeError("There we validation errors! Check the log for what")
