# Assignment

## Brief

Write the Python codes for the following questions.

## Instructions

Paste the answer as Python in the answer code section below each question.

### Question 1

Question: Calculate the correlation between 'MSFT' and 'IBM' returns from a DataFrame of stock returns.

```python
corr_msft_ibm = returns["MSFT"].corr(returns["IBM"])
print(corr_msft_ibm)

```

Answer:

```python

```

### Question 2

Question: Convert the columns `B` and `C` from wide to long format.

```python
import pandas as pd

df = pd.DataFrame({
'A': {0: 'a', 1: 'b', 2: 'c'},
'B': {0: 1, 1: 3, 2: 5},
'C': {0: 2, 1: 4, 2: 6}
})
```

Answer:

```python
df_long = df.melt(id_vars="A", value_vars=["B", "C"], var_name="variable", value_name="value")
print(df_long)

```

### Question 3

Question: Slice the Series to return data from 5th to 15th January.

```python
import pandas as pd
import numpy as np

dates = pd.date_range("2023-01-01", "2023-01-31")
data = pd.Series(np.random.rand(len(dates)), index=dates)
```

Answer:

```python
slice_data = data.loc["2023-01-05":"2023-01-15"]
print(slice_data)

```

## Submission

- Submit the URL of the GitHub Repository that contains your work to NTU black board.
- Should you reference the work of your classmate(s) or online resources, give them credit by adding either the name of your classmate or URL.
