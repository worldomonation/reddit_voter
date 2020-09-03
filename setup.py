import os

from setuptools import setup

MAJOR_VERSION = 0
MINOR_VERSION = 0
REVISION = 2

PACKAGE_VERSION = '.'.join([
    str(item) for item in [MAJOR_VERSION, MINOR_VERSION, REVISION]
])
DESCRIPTION = '''A mass-upvote/downvote client for Reddit.'''
with open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'README.md')) as f:
    README = f.read()

DEPENDENCIES = [
    'flake8',
    'praw',
    'progressbar2'
]

setup(
    name='reddit_voter',
    version=PACKAGE_VERSION,
    description=DESCRIPTION,
    long_description=README,
    keywords='reddit',
    author='Edwin Gao',
    author_email='egao@outlook.com',
    url='https://github.com/worldomonation/reddit_voter',
    license='',
    packages=['reddit_voter'],
    include_package_data=True,
    install_requires=DEPENDENCIES,
    entry_points="""
    # -*- Entry points: -*-
    [console_scripts]
    voter = reddit_voter.main:main
    """,
)
