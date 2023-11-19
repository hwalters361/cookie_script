# Cookie Activity Script
highest frequency usage cookies coding challenge, in Python. 

A command line program in Python to process a CSV log file and return the most active cookie for specified day. The script is run using the command specified in the prompt.

Unit tests can be run by navigating to the top-level directory of the codebase and running `python -m unittest`

The program uses a dictionary to store the cookie names and their corresponding frequency, then iterates over this dictionary and compiles the most used cookies into a set, which is printed to the output. 

<h4><b>Time complexity:</b></h4> O(n) (one iteration per line in the file, then one iteration per cookie afterwards)
<h4><b>Space complexity:</b></h4> O(n) (one dictionary entry per cookie)
