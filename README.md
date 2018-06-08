# Dummy Package with f90 library to test conda recipes.

## Finnal test:

conda install -c YOUR_ANACONDA_CHANNEL vector_normalization

```python
import numpy as np
from vector_normalization import normalize_vector()

vect=np.array([1,1,1])
normalize_vector(vect)
print(vect)
```
