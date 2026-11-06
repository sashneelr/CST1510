"""
RECORD CHECK  -  my version
===========================

Name  :  Sashneel Ramiah
Lane  :  IT      (delete two)
Date  :  05/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
def parse_line(raw_line):
            """Clean and parse an IT server record into a dictionary."""
            clean_line = raw_line.strip()
            hostname_part, rest = clean_line.split(",", 1)
            hostname = hostname_part.strip().lower()
            pieces = rest.split(",")
            data = {"hostname": hostname}
            for piece in pieces:            
                key, value = piece.split("=")
                key = key.strip()
                value = value.strip()
                data[key] = float(value)
            return data

def status_of(record):
      """Determine the usuage status of an IT server"""
      used = record["used"]
      total = record["total"]
      if used > total:
            return "OVER LIMIT"
      elif used >= total * 0.90:
            return "WARNING"
      else:
            return "OK"

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = ["Srv-01,used=65,total=100",   # replace with your code
               "SRV-03,used=45,total=100",
               "srv-04,used=95,total=100",
               " Srv-05 , used=80 , total=100 ",
               "SRV-06,used=120,total=100"
            
]

# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)
    print(record, status)


# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it against at least 5 genuinely messy raw records
#    [x] Run it with a value that will not convert to a number - write the
#        error down
#    [x] Check every function does one job, with a docstring
