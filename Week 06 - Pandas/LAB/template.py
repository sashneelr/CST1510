"""
RECORD CHECK  -  my version
===========================

Name  :  Sashneel Ramiah
Lane  :  IT      (delete two)
Date  :  03/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df =  pd.read_csv("it_storage.csv") # replace with pd.read_csv("your_file.csv")


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

# your column(s) go here
# Calculate storage usage percentage
df["percent"] = (df["used_gb"] / df["total_gb"]) * 100
print(df[["hostname", "percent"]])
# Display the percentage for each server
# Classify each server by storage usage
df["status"] = df["percent"].apply(
        lambda x: "OVER LIMIT" if x > 100
            else "WARNING" if x >= 90
    else "OK"
)

# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

print(df)

# Display servers that need attention
# Filter rows where status is not "OK"
attention = df[df["status"] != "OK"]
print(attention)


# ==========================================================================
# 4. Before you finish:
#    [x] Run it and check the percent/status columns by hand for one row
#    [x] Check you used & (not "and") if you combined more than one condition
#    [x] Check every column your code refers to actually exists - watch case
