# Meant to be run in the data dir, cannot live there or the site wont build

#git ls-tree -r --name-only HEAD -z | TZ=UTC xargs -0n1 -I_ git --no-pager log -1 --date=iso-local --format="%ad _" -- _ | gcut -d ' ' -f 1 | sort | uniq -c

mkdir entries_by_time

echo "Processing all entries..."
alldata=$(git ls-tree -r --name-only HEAD -z | TZ=UTC xargs -0n1 -I_ git --no-pager log -1 --date=iso-local --format="%ad _" -- _)

# Put in quotes to get proper line chopping
echo "$alldata" | gcut -d ' ' -f 1 | sort | uniq -c > entries_by_time/total_entries.txt

for field in */
do
  field=${field%*/}  # Remove trailing /
  echo "Processing $field entries..."
  echo "$alldata" | grep $field | gcut -d ' ' -f 1 | sort | uniq -c > entries_by_time/${field}_entries.txt
done
