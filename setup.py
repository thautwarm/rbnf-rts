from setuptools import setup, find_packages
from pathlib import Path

with Path('README.md').open() as readme:
    readme = readme.read()


setup(
    name='rbnf-rts',
    version="0.7",
    keywords="", # keywords of your project that separated by comma ","
    description="", # a conceise introduction of your project
    long_description=readme,
    long_description_content_type="text/markdown",
    license='mit',
    python_requires='>=3.6.0',
    url='https://github.com/thautwarm/rbnf-rts',
    author='thautwarm',
    author_email='twshere@outlook.com',
    packages=find_packages(),
    entry_points={
        "console_scripts":
            [
             "rbnf-dump-graph=rbnf_rts.rbnf_api:cli_dump_graph",
             "rbnf-view-graph=rbnf_rts.rbnf_api:cli_view_graph",
             "rbnf-pygen=rbnf_rts.rbnf_api:cli_generate"
            ]
    },
    # above option specifies commands to be installed,
    # e.g: entry_points={"console_scripts": ["yapypy=yapypy.cmd.compiler"]}
    install_requires=['prettyprinter', 'wisepy2'],
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)
