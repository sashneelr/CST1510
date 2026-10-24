"""
RECORD CHECK  -  my version
===========================

Name  :  Sashneel Ramiah
Lane  :  Cyber      (delete two)
Date  :  22/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here
class Record:
     def __init__(self, label, value, limit):
        """the source IP address, failed login count, and total login attemps for a record are stored"""
        self.label = label
        self.value = value
        self.limit = limit

     def summary(self):
        return f" IP {self.label} - {self.value} failed attempts, {self.limit} total attempts"

     def status(self):
        """checks the percentage of failed login attempts and determines whether the record is OK, WARNING or OVER LIMIT"""
        percentage = (self.value / self.limit) * 100
        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"
    


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

records = []   # replace with your code
Record1 = Record("114.111.1.21", 8, 12)
records.append(Record1)
Record2 = Record("111.166.10.22", 9, 10)
records.append(Record2)






# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here
    print("Source IP:", record.label)
    print("Failed logins:", record.value)
    print("Total attempts:", record.limit)
    print("Status:", record.status())

        
          

    print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
