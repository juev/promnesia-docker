'''
A more sophisticated example of config for Promnesia
'''

from pathlib import Path

OUTPUT_DIR = Path('/data')

from promnesia import Source
from promnesia.sources import auto
from promnesia.sources import instapaper, pocket, twitter, roamresearch, hypothesis

SOURCES = [
    # handle my knowledge base: extract links from Org-mode and Markdown files
    Source(
        auto.index,
        '/data/blog',
        # you can specify optional name, so you can see where the URL is coming from in the extension
        name='blog',
    ),

    # will clone the repository and index its contents!
    Source(
        guess.index, # you could also use 'vcs.index', but auto can handle it anyway
        'https://github.com/karlicoss/exobrain',
        name='exobrain',
    ),
    lambda: Source(hypothesis.index),
]
