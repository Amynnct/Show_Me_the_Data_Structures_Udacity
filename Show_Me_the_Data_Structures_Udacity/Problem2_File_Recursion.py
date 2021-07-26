import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not os.path.isdir(path):
        return ("Please use a valid directory path")

    if suffix == '':
        return []
    
    result_files = []
    for dir in os.listdir(path):
        if os.path.isfile(os.path.join(path, dir)):      #if this dir is a file, then check if it ends with suffix
            if dir.endswith('.' + suffix):
                result_files.append(dir)
        else:
            result_files.extend(find_files(suffix, os.path.join(path, dir)))
            
    return result_files

#%% Testing official
# Testing preparation
path_base = os.getcwd() + '/problem2_testdir/testdir'

# Normal Cases:
print(find_files(suffix='c', path=path_base))
# ['a.c', 'b.c', 'a.c', 't1.c']

print(find_files(suffix='h', path=path_base))
# ['a.h', 'b.h', 'a.h', 't1.h']

print(find_files(suffix='z', path=path_base))
# []

# Edge Cases:
print(find_files(suffix='', path=path_base))
# []
print(find_files(suffix='c', path='/problem2testdir/testdir'))
#Please use a valid directory path
