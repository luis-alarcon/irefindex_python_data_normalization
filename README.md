# Data Processing of iRefIndex Dataset

This python script generates a clean easily readable and accessible database from [iRefIndex][irefindex] dataset. 

# License

[GNU General Public License v3.0][license]

# Requirements

## Python

```sh
    Python 
```

## Packages

```sh
    import pandas as pd
    import re
```

# Information

## iRefIndex

> It is a dataset that provides an index of protein interactions available in a number of primary interaction databases; databases such as:
>
> * BIND
> * BioGRID
> * CORUM
> * DIP
> * HPRD
> * InnateDB
> * IntAct
> * MatrixDB
> * MINT
> * MPact
> * MPIDB
> * MPPI

## Issues with Current Format

As it can be seen in the [documentation][irefindex_documentation] each column entry divides the database and its relevant code for the interaction or proteins involved via <code> : </code> and each individual database via  <code> | </code>.

Example 1 : <code>uniprotkb:P06722</code>

Example 2: <code>uniprotkb:P23367|refseq:NP_418591|entrezgene/locuslink:948691|rogid:hhZYhMtr5JC1lGIKtR1wxHAd3JY83333|irogid:12345</code>

This structure makes it difficult to access the information required without having to process each column for each protein or interaction or other search factors.

## Script

This script in this first stage produces a clean and processes .csv file with each entry for each uidA (see iRefIndex documentation) in an individual row.

# Future Development

To be announced.

[irefindex]:<http://irefindex.org/wiki/index.php?title=iRefIndex>
[license]:<https://github.com/luis-alarcon/irefindex_python_data_normalization/blob/master/LICENSE>
[irefindex_documentation]:<http://irefindex.org/wiki/index.php?title=README_MITAB2.6_for_iRefIndex#Column_number:_3_.28altA.29>