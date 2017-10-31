# SpikesData

Data parser for Spikes SNN library but can also be used as an external library.

SpikesData parser supports `csv`, `json` (coming soon) and `sml` (coming soon) reading and writing.

## Quick Start

### Reading a time series data with labels

```python
from spiksdata import reader

csv_reader = reader.ReadCSV('path/to/folder/')
```
