from pydantic import BaseModel, ValidationError, validator, AnyUrl, StrictInt
from typing import Optional, List, Union, Dict, AnyStr
from yaml import safe_load
from enum import Enum
from os import walk
from os.path import join
import re

# Custom types


class MailTo(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: str):
        if not isinstance(v, str):
            raise TypeError("Not a valid mailto Email format")
        v = v.strip()
        re.match(r"mailto:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", v)
        if not re.match(r"mailto:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", v):
            raise ValueError("mailto URL is not a valid mailto link")


class ValidProteins(str, Enum):
    antibody = 'antibody'
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
    RdRP = 'RdRP'
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
    Macrodomain = 'Macrodomain'
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
    virion = "virion"


def prevent_unhandled_subdomains(proteins: List[str]) -> List[str]:
    unhandled_subdomains = {
        ValidProteins.RBD: ValidProteins.spike,
        ValidProteins.S1: ValidProteins.spike,
        ValidProteins.S2: ValidProteins.spike
    }

    base_error = ("Subdomain proteins are not correctly implemented yet. At least 1 protein listed was a subdomain.{}"
                  "Please use the base protein instead (e.g. RBD -> spike).")
    caught_subdomains = []

    for protein in proteins:
        if protein in unhandled_subdomains:
            parent = unhandled_subdomains[protein]
            if parent not in proteins:
                caught_subdomains.append(protein)
        else:
            # There is at least some protein known
            # Reset the building list
            caught_subdomains = []
            break
    if caught_subdomains:
        str_caught_subdomains = "\n\t- " + "\n\t- ".join(caught_subdomains) + "\n"
        full_error = base_error.format(str_caught_subdomains)
        raise ValueError(full_error)
    return proteins


# Check that proteins have not been given other names
common_names = {
    '3CLpro': ['mpro', 'nsp5', '3c-like', '3c-l', 'mprotease', '3cl-pro'],
    'PLpro': ['nsp3', 'p-l', 'papin', 'papin-like', 'pl-pro', 'pl2pro'],
    'Macrodomain': ['x'],
    'E protein': ['e-protein', 'envelope', 'e-pro', 'epro', 'orf4'],
    'Helicase': ['hel', 'nsp13'],
    'M protein': ['membrane', 'mem', 'm-protein', 'm-pro', 'orf5'],
    'N protein': ['nucleoprotein', 'nucleocapsid', 'nuc', 'orf9'],
    'RdRP': ['nsp12', 'rna prot', 'rna', 'rna-prot', 'rna-dir']
    }
# make a reverse map.
alt_names = {}
for common, alts in common_names.items():
    for alt in alts:
        alt_names[alt] = common
# Check for overlap
overlap_map = []
for prot in ValidProteins:
    value = prot.value  # IDE's complain, its a valid property for Enum objects.
    if value.lower() in alt_names:
        overlap_map.append([value, alt_names[value.lower()]])
if overlap_map:
    err_string = "A protein was defined in the ValidProtein's schema, but already has a more common name. Please " \
                 "changing the following item(s) to its/their more common name(s):\n"
    for value, common in overlap_map:
        err_string += f"\t{value} -> {common}\n"
    err_string += "If you think this is in error, please raise the issue on GitHub"
    raise ValueError(err_string)


class ValidDomains(str, Enum):
    """ Valid Protein Domains """
    virion = 'virion'
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
    mouse = 'mouse'
    sars_cov = 'SARS-CoV'
    sars_cov_2 = 'SARS-CoV-2'
    hcov_oc43 = 'HCoV-OC43'


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


class DOIModel(BaseModel):
    name: str
    url: Optional[AnyUrl]
    doi: str
    description: str
    creator: str
    owner: str
    content: List[str]
    file_types: List[str]
    files: List[str]
    size: str
    purpose: str
    license: Optional[str]


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

    _no_subdomains = validator("proteins", allow_reuse=True)(prevent_unhandled_subdomains)


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

    _no_subdomains = validator("protein", allow_reuse=True)(prevent_unhandled_subdomains)


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


class TrajectoryDataEntry(BaseModel):
    label: str
    location: str
    size: str
    type: Optional[str]


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
    trajectory: Optional[AnyUrl]
    size: Optional[str]
    trajectory_data: Optional[List[Dict[AnyStr, List[TrajectoryDataEntry]]]]
    length: Optional[str]
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

    @validator('length')
    def length_valid(cls, v, values, **kwargs):
        if v is None:
            if values.get('type') == ('docking'):
                return v
            else:
                raise ValueError(f'Length must be the elapsed real time for the trajectory with units unless it is of '
                                 f'type "docking", is {v}.')
        elif isinstance(v, str):
            return v
        else:
            raise ValueError(f'Length must be the elapsed real time for the trajectory with units unless it is of type'
                             f' "docking", is {v}.')

    @validator("trajectory_data", pre=True, always=True)
    def correct_trajectory_setup(cls, v, values, **kwargs):
        traj = values.get("trajectory")
        size = values.get("size")
        # Check if not set
        if not traj and not v:
            raise ValueError("One of ('trajectory' and 'size') or ('trajectory_data') is required.")
        # Check if both set
        if v and (traj is not None or size is not None):
            raise ValueError("'trajectory_data' cannot be set at the same time as ('trajectory' and 'size'), "
                             "please choose one or the other.")
        return v

    @validator("trajectory_data")
    def top_list_is_one_lenth(cls, v):
        if v is not None:
            for list_item in v:
                len_list = len(list_item)
                if len_list != 1:
                    raise ValueError(f"Entry in 'trajectory_data' does not have the right number of top-level keys. "
                                     f"Must have 1, it had {len_list}."
                                     f"\n\t Entry with keys: {list_item.keys()}")
        return v

    @validator("size", pre=True, always=True)
    def size_and_traj_set(cls, v, values, **kwargs):
        traj = values.get("trajectory")
        if (v and not traj) or (traj and not v):  # XOR
            raise ValueError("Both ('trajectory' and 'size') must be set, or use the 'trajectory_data' entry")
        return v

    _no_subdomains = validator("proteins", allow_reuse=True)(prevent_unhandled_subdomains)
    
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

    _no_subdomains = validator("proteins", allow_reuse=True)(prevent_unhandled_subdomains)


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

    _no_subdomains = validator("proteins", allow_reuse=True)(prevent_unhandled_subdomains)


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
    alt_names: Optional[List[str]]


class ContributorMemberModel(BaseModel):
    name: str
    url: Optional[Union[AnyUrl, MailTo]]
    organization: Optional[str]


class ContributorsModel(BaseModel):
    name: Optional[str]
    members: List[ContributorMemberModel]


class ToolsTypeModel(str, Enum):
    analysis = 'analysis'
    construction = 'construction'
    productivity = 'productivity'
    workflows = 'workflows'
    machine_learning = 'machine learning'


class ToolsInputModel(str, Enum):
    structure = 'structure'
    trajectory = 'trajectory'


class ToolsOutputModel(str, Enum):
    structure = 'structure'
    trajectory = 'trajectory'
    visualization = 'visualization'
    analytics = 'analytics'


class ToolsModel(BaseModel):
    name: str
    url: AnyUrl
    description: str
    organization: Optional[str]
    institution: Optional[str]
    lab: Optional[str]
    type: List[ToolsTypeModel]
    input_data: Optional[List[ToolsInputModel]]
    output: Optional[List[ToolsOutputModel]]
    api: Optional[AnyUrl]

    @validator("input_data", "output", always=True)
    def tools_io_data_check(cls, v, values, field):
        if ((ToolsTypeModel.analysis in values.get('type') or ToolsTypeModel.construction in values.get('type'))
                and not v):
            raise ValueError(f'{field} can only be null/not present/empty if type does not have '
                             f'"{ToolsTypeModel.analysis}" or "{ToolsTypeModel.construction}"'
                             f'Instead, types are {values.get("type")}')
        return v


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
                   'dois': DOIModel,
                   'models': ModelsModel,
                   'molecules': MoleculesModel,
                   'proteins': ProteinsModel,
                   'simulations': SimulationsModel,
                   'structures': StructuresModel,
                   'targets': TargetsModel,
                   'teams': TeamsModel,
                   'glossary': GlossaryModel,
                   'organizations': OrganizationModel,
                   'contributors': ContributorsModel,
                   'tools': ToolsModel
                   }

    total_errors = 0
    # Iterate over each directory.
    for directory, model in directories.items():

        # Generate a set of files for the given directory.
        f = []
        for (dirpath, dirnames, filenames) in walk(join("../data", directory)):
            f.extend(filenames)

        # Filter out non ".yml" files from the directory
        f_filter = filter_yaml(f, ["yml", "yaml"])

        # For each yml file in the directory, perform validation against its associated model.
        for filename in f_filter:
            total_errors += validate(join("../data", directory, filename), model)

    if total_errors:
        raise RuntimeError(f"There were {total_errors} validation errors! Check the log for what")
