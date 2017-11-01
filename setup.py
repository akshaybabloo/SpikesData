import os

from setuptools import setup, find_packages

from spikesparser import __version__

base_dir = os.path.dirname(__file__)

try:
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace("\r", "")  # Do not forget this line
except OSError:
    print("Pandoc not found. Long_description conversion failure.")
    import io

    # pandoc is not installed, fallback to using raw contents
    with io.open('README.md', encoding="utf-8") as f:
        long_description = f.read()

setup(
    name='SpikesData',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/akshaybabloo/SpikesParser',
    license='MIT',
    author='Akshay Raj Gollahalli',
    author_email='akshay@gollahalli.com',
    description='Temporal data parser.',
    long_description=long_description,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Microsoft',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Software Distribution',
        'Topic :: Utilities'
    ]
)
