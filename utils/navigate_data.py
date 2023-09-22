def navigate_data(data, keys):
    '''
    navigate_data(data, keys)
    data: This is the nested data structure (dictionary or list) from which we want to extract values.
    keys: This is a list of key chains, where each key chain is itself a list of keys or indices to navigate through the nested data structure.
    '''
    result = []
    for key_chain in keys:
        # This variable will be used to keep track of the current position within the nested data structure.
        current_value = data
        for key in key_chain:
            # By the key being a string, it is implied we are dealing with a dictionary.
            if isinstance(key, str):
                # Handle the case where a key is missing in the path.
                if key in current_value:
                    current_value = current_value[key]
                    # Added check to see if we require the id of another resource and to extract that from the specified url.
                    if key == 'url':
                        current_value = int(current_value.rsplit("/", 2)[-2])
                else:
                    current_value = None
                    break
            # By the key being an integer, it is implied we are dealing with a list.
            elif isinstance(key, int):
                # Handle the case where the list index is out of bounds.
                if key < len(current_value) and len(current_value) != 0:
                    try:
                        current_value = current_value[key]
                    except:
                        current_value = current_value[0]
                else:
                    current_value = None
                    break
        result.append(current_value)
    return result