"""
This file is meant to be run from the simulations directory, but it cannot live there or Hugo breaks
"""

from pint import UnitRegistry
import re
import yaml
from os import listdir
from os.path import isfile

ureg = UnitRegistry()

total_size = 0 * ureg.bytes
total_length = 0 * ureg.second
fah_length = 0 * ureg.second
total_simulations = 0


def compute_size(size, length, filename):
    global total_size, total_length, fah_length, total_simulations
    # Size fixes
    if size is not None:
        # Fix big O notation
        if size[0] == "O":
            sizes = size.split("(")
            size = sizes[-1].split(")")[0]
        # Fix plural units
        trailing_s = re.search(r'\w\ws$', size)
        if trailing_s:
            size = size[:-1]

    # Length Fixes
    if length is not None:
        # Fix replicates
        if "replicates" in length:
            lengths = length.split(",")
            replicates = int(lengths[0].split()[0])
            rep_lengths = lengths[-1].split("each")[0]
            rep_data = rep_lengths.split()
            rep_total = int(rep_data[0]) * replicates
            length = f"{rep_total} {rep_data[-1]}"
        # Fix multiplicative trajectories
        multi_notation = re.search(r'(\d+ ?)x ?(\d+ ?)(\w\w) ?', length)
        if multi_notation:
            first_number = int(multi_notation.group(1))
            second_number = int(multi_notation.group(2))
            unit = multi_notation.group(3)
            length = f"{first_number * second_number} {unit}"

    try:
        increment = 0
        if size is not None and size != "None":
            total_size += ureg(size)
            increment = 1
        if length is not None and length != "None":
            if "FAH" in filename or "fah" in filename:
                fah_length += ureg(length)
            total_length += ureg(length)
            increment = 1
        total_simulations += increment
    except:
        breakpoint()


def coerece_size_length(data):
    try:
        size = str(data["size"]).replace("μ", "u").replace("K", "k")
    except KeyError:
        size = None
    try:
        length = str(data["length"]).replace("μ", "u")
    except KeyError:
        length = None
    return size, length


for filename in listdir("."):
    if not isfile(filename) or ("yml" not in filename and "yaml" not in filename) or ("fake" in filename):
        continue

    with open(filename, 'r') as f:
        data = yaml.safe_load(f)

    if "trajectory_data" in data:
        for arbitrary_header in data["trajectory_data"]:
            for arbitrary_data_list in arbitrary_header.values():
                for entry_data in arbitrary_data_list:
                    size, length = coerece_size_length(entry_data)
                    compute_size(size, length, filename)

    size, length = coerece_size_length(data)

    compute_size(size, length, filename)


print(f"Total Size: {total_size.to(ureg.TB)}")
print(f"Total Length: {total_length.to(ureg.ms)}")
print(f"F@H Length: {fah_length.to(ureg.ms)}")
print(f"Total Simulations: {total_simulations}")

