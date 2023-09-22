def navigate_data(data, keys):
    '''
    navigate_data(data, keys)\n
    data: This is the nested data structure (dictionary or list) from which we want to extract values.\n
    keys: This is a list of key chains, where each key chain is itself a list of keys or indices to navigate through the nested data structure.\n
    keys example: [['id'],['generation','url']]
    '''
    result = []
    for key_chain in keys:
        current_value = data    # This variable will be used to keep track of the current position within the nested data structure.
        for key in key_chain:
            if current_value is None:   # Handle the case where no data is found.
                break
            if isinstance(key, str):    # By the key being a string, it is implied we are dealing with a dictionary.
                if key in current_value:    # Handle the case where a key is missing in the path.
                    current_value = current_value[key]
                    if key == 'url':
                        current_value = int(current_value.rsplit("/", 2)[-2]) # Used to extract the specific ids for future foreign key creation.
                else:
                    current_value = None
                    break
            elif isinstance(key, int):  # By the key being an integer, it is implied we are dealing with a list.
                if key < len(current_value) and len(current_value) != 0:    # Handle the case where the list index is out of bounds (negatives are allowed for backwards list slicing).
                    try:
                        current_value = current_value[key]
                    except:
                        current_value = current_value[0]    # Handle the case where an invalid index is used (defaults to 0 to grab the first available value)
                else:
                    current_value = None
                    break
        result.append(current_value)    # Append individual value to final results list.
    return result