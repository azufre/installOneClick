import os
import glob
import subprocess

def root_to_install(package):
    return f'C:/Users/Vaio/Desktop/coffee/env/Scripts/pip install {package}' 

def install_package(packages):

    for package in packages:
        print(f'{package} installing...')
        subprocess.call(root_to_install(package))

def get_local_package(local_packages_dir):
    data = []
    os.chdir(local_packages_dir)

    for package in glob.glob('*.whl'):
        data.append(os.path.realpath(package))

    return data    

packages_from_website = ['test-test', ]
package_from_local  = 'C:/Users/Vaio/Desktop/packages'

#install_package(packages_from_website)
install_package(get_local_package(package_from_local))




