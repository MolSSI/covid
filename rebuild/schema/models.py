from pydantic import BaseModel, AnyUrl
from typing import Union, Optional, List, Dict, Any
from enum import Enum


class GoodBadMeh(str, Enum):
    good = 'good'
    bad = 'bad'
    ok = 'questionable'
    unreviwed = 'unreviwed'


# Helper for anything which points to a URL or a file
pointer = Union[AnyUrl, str]
op_pointer = Optional[pointer]
pointer_list = List[pointer]
op_pointer_list = Optional[List[pointer]]


class SubEntrySchema(BaseModel):
    """
    'Models' entry for the
    """
    id: str  # Unique ID within the list of entries
    description: str
    pointers: pointer_list
    citations: op_pointer_list
    author: Optional[str]
    submitting: Optional[str]


class InputsEntrySchema(SubEntrySchema):
    """
    Schema for input files
    """
    ref: Optional[Union[str, List[str]]]


class RecordSchema(BaseModel):
    """Top level entry for each table"""
    id: str
    description: str
    image: op_pointer
    origin: op_pointer
    author: str
    submitting: Optional[str]
    tags: Optional[List[str]]
    citations: op_pointer_list
    models: Optional[List[SubEntrySchema]]
    structure_data: Optional[List[SubEntrySchema]]
    inputs: Optional[List[InputsEntrySchema]]
    trajectories: Optional[List[InputsEntrySchema]]
    analysis: Optional[List[InputsEntrySchema]]
    algorithms: Optional[List[InputsEntrySchema]]


class RecordReview(BaseModel):
    reviewer: str
    structure: GoodBadMeh = GoodBadMeh.unreviwed
    biology: GoodBadMeh = GoodBadMeh.unreviwed
    models: Optional[Dict[str, GoodBadMeh]]
    structure_data: Optional[Dict[str, GoodBadMeh]]
    inputs: Optional[Dict[str, GoodBadMeh]]
    trajectories: Optional[Dict[str, GoodBadMeh]]
    analysis: Optional[Dict[str, GoodBadMeh]]
    algorithms: Optional[Dict[str, GoodBadMeh]]


tag_samples = ["sample", "more sample", "even more", "random thing", "nothing"]
model_samples = ["A", "B", "C", "D", "E"]
letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
gbm = [GoodBadMeh.good.value, GoodBadMeh.bad.value, GoodBadMeh.ok.value, GoodBadMeh.unreviwed.value]
sample_record = []
for i in range(4):
    new_dict = {
        "id": i,
        "description": f"Some descriptor of {i}",
        "image": "",
        "origin": f"PDB XXX{i}",
        "author": "Levi N. Naden",
        "tags": [sample for sample in tag_samples[:i+1]],
        "citations": ["Waffles", "DOI:XXXX.yyyy/ZZZZ"],
        "models": [{
            "id": f"{i}-sub-{letters[0]}",
            "description": " ".join("Some model description or such".split()[i:]),
            "pointers": [sample for sample in tag_samples[:i+1]],
            "citations": ["Model Waffles", "Syrup:XXXX.yyyy/ZZZZ"],
            "author": "Levi Naden and Python",
            "submitting": "Levi Naden"
        }],
        "structure_data": [{
            "id": f"{i}-sub-{letters[1]}",
            "description": " ".join("Some model description or such".split()[i:]),
            "pointers": [sample for sample in tag_samples[:i + 1]],
            "citations": ["Structural Waffles"],
        }],
        "inputs": [{
            "id": f"{i}-sub-{letters[2]}",
            "description": " ".join("Some model description or such".split()[i:]),
            "pointers": [sample for sample in tag_samples[:i + 1]],
            "ref": f"{i}-sub-{letters[1]}"
        }],
        "trajectories": [{
            "id": f"{i}-sub-{letters[3]}",
            "description": " ".join("Some model description or such".split()[i:]),
            "pointers": [sample for sample in tag_samples[:i + 1]],
            "ref": [f"{i}-sub-{letters[2]}", f"{i}-sub-{letters[1]}"]
        }],
    }
    sample_record.append(new_dict)

sample_review = {
    "reviewer": f"Levi N. Naden",
    "structure": gbm[0],
    "biology": gbm[1],
    "models": {f"{0}-sub-{letters[0]}": gbm[0]},
    "structure_data": {f"{1}-sub-{letters[1]}": gbm[1]},
    "inputs": {f"{2}-sub-{letters[2]}": gbm[2]},
    "trajectories": {f"{3}-sub-{letters[3]}": gbm[3]},
}
