import datetime as dt
import glob
from pathlib import Path
from contextlib import ExitStack

data = {}

earliest = dt.datetime.max
latest = dt.datetime.min
directories = glob.glob("./*", recursive=False)
d_and_t = directories + ["total"]
d_and_t = [Path(i).name for i in d_and_t if "entries_by" not in i]
entries = Path("entries_by_time")
for d_name in d_and_t:
    data_file = entries / Path(d_name + "_entries.txt")
    data[d_name] = {}
    with data_file.open("r") as f:
        for line in f.readlines():
            count, date_str = line.split()
            count = int(count)
            date = dt.datetime.strptime(date_str, '%Y-%m-%d')
            if date > latest:
                latest = date
            if date < earliest:
                earliest = date
            data[d_name][date] = count

delta = latest - earliest

with ExitStack() as stack:
    files = {directory: stack.enter_context((entries / Path(directory + "_entries_complete.txt")).open("w"))
             for directory in d_and_t
             }
    for day_count in range(delta.days + 1):
        day = earliest + dt.timedelta(days=day_count)
        str_day = day.strftime('%B %d, %Y')
        for d_name in d_and_t:
            count = data[d_name].get(day, 0)
            files[d_name].write(f"{str_day}-{count}\n")
