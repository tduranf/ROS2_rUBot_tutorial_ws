from setuptools import setup
import os
from glob import glob

package_name = 'project_tecla'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),  # Aquesta línia és clau

    ],
    install_requires=['setuptools', 'turtlesim'],
    zip_safe=True,
    maintainer='tecla',
    maintainer_email='tduranfo17@alumnes.ub.edu',
    description='My ROS2 turtlesim controller',
    license='MIT',
    entry_points={
        'console_scripts': [
            'commander = project_tecla.commander_node:main',
        ],
    },
)
