# Microsatellite Matcher
## What it does:
Searches microsatellite excel workbooks for matching entries.
Be warned, the tool is fairly specific to our labs workbook format. It has not
been extended to work with microsatellites with lengths less than 100.  That
being said, it works well for quick superficial analysis of large workbooks.
## How to run it:
###In Python:
```python
import microsatellite_matcher as mm
mm.match("filename.xlsx")
```
###In Bash:
```Bash
python microsatellite_matcher.py [file_name_0] [file_name_1]
```
