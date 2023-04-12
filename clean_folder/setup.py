from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.1',
    description='Sorting files be category',
    url='https://github.com/maxafanasiev/homework_2',
    author='Afanasiev Maksym',
    author_email='afanasievmaksym2@gmail.com',
    license='UA',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.sort:main']}
)