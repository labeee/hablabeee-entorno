
# Paths
path_setup = r'system/has_setup.txt'

def install_packages():
    has_setup = open(path_setup, 'r').read()
    if has_setup == '0':
        import os
        os.system('python -m pip install --upgrade pip')
        os.system('pip install --upgrade python')
        os.system('pip install pandas')
        os.system('pip install googlemaps')
        has_setup = open(path_setup, 'w').write('1')

