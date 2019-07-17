import numpy as np
import pandas as pd

df = pd.DataFrame(
    np.random.randn(5, 3), 
    columns = ['one', 'two', 'three']
)

df

df['one'].sum()
