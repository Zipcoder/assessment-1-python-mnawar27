
def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    for i in keylist:
        datadict.pop(i)
    return datadict

def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    return key in datadict.values()

def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    for i in ddd:
        if ddd[i] == min(ddd.values()):
            return i

def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    for i in ddd:
        if ddd[i] == max(ddd.values()):
            return i

def letterfreq(word):
    '''
    # Write a function that returns a dictionary of letter frequencies from a word
    '''
    a = {}
    for i in word:
        if i in a:
            a[i] +=1
        else:
            a[i] = 1
    return a
