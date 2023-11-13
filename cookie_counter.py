#!/usr/bin/env python

def is_valid_date_format(date_string):
    """
    Check if the format of an inputted date string is correct (yyyy-mm-dd)
    param: a string
    returns: true or false
    """
    if len(date_string) != 10:
        return False
    
    if date_string[4] != '-' or date_string[7] != '-':
        return False

    try:
        int(date_string[:4])
        month = int(date_string[5:7])
        day = int(date_string[8:])
    except ValueError:
        return False

    if month > 12 or day > 31:
        return False
    
    return True

def most_used_cookies(file_path, date):
    """
    Returns the most frequently used cookies in a CSV log of cookies and the timestamp they were used
    param: string, the filepath of the CSV log
    param: string or None, a date to look for cookies in yyyy-mm-dd format (if None, will search the entire log)
    returns: string, the most used cookie(s) (if multiple cookies tie for most used, they are included and get their
        own line in the string)
    """
    cookie_counts = {}
    
    if (date != None and not is_valid_date_format(date)):
        raise ValueError("Invalid date format, (must be yyyy-mm-dd).")
    
    with open(file_path, 'r') as file:
        file.readline() # advance past the header
        
        for line in file:
            row = line.strip().split(',')

            datetime = row[1].strip().split('T')
            row_date = datetime[0]
            
            if date != None and row_date != date:
                continue
            
            cookie = row[0]
            if cookie in cookie_counts:
                cookie_counts[cookie] += 1
            else:
                cookie_counts[cookie] = 1
    
    # compile the most used cookies into a set
    cur_max = 0
    most_used_cookies = set()
    for cookie in cookie_counts:
        if cookie_counts[cookie] > cur_max:
            cur_max = cookie_counts[cookie]
            most_used_cookies = set()
            most_used_cookies.add(cookie)
        elif cookie_counts[cookie] == cur_max:
            most_used_cookies.add(cookie)
    
    return "\n".join(most_used_cookies) + "\n"
