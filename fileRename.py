def file_rename(file_list):
    newfilenames = []

    for filename in file_list:
        # Add extension here
        extension = ' '
        if extension in filename:
            newfilenames.append(filename[:-2])
        else:
            newfilenames.append(filename)

    return newfilenames