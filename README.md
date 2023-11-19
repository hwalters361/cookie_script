# Quantcast-coding_task-Exercise
Most Active Cookie coding challenge, in Python.

The script is run using the command specified in the prompt. `$./most_active_cookie cookie_log.csv -d 2018-12-09` given a file "cookie_log.csv" exists in the same directory.
Unit tests can be run by navigating to the top-level directory of the codebase and running `python -m unittest`

The program uses a dictionary to store the cookie names and their corresponding frequency, then iterates over this dictionary and compiles the most used cookies into a set, which is printed to the output. 

<h4><b>Time complexity:</b></h4> O(n) (one iteration per line in the file, then one iteration per cookie afterwards)
<h4><b>Space complexity:</b></h4> O(n) (one dictionary entry per cookie)
