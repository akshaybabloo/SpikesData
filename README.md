# SpikesParser

| Branch | Codecov | CI | Requirements |
|--------|---------|---------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Master | [![codecov](https://codecov.io/gh/akshaybabloo/SpikesParser/branch/master/graph/badge.svg)](https://codecov.io/gh/akshaybabloo/SpikesParser) | [![Build Status](https://travis-ci.org/akshaybabloo/SpikesParser.svg?branch=master)](https://travis-ci.org/akshaybabloo/SpikesParser) | [![Requirements Status](https://requires.io/github/akshaybabloo/SpikesParser/requirements.svg?branch=master)](https://requires.io/github/akshaybabloo/SpikesParser/requirements/?branch=master) |

Data parser for Spikes SNN library but can also be used as an external library.

SpikesParser supports `csv`, `json` (coming soon) and `sml` (coming soon) reading and writing.

## Quick Start

Some basic examples on reading and writing of files.

### Reading a time series data with labels

```python
from spiksparser import reader

csv_reader = reader.ReadCSV('path/to/folder/')
```
