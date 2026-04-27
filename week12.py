import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

scores = [80, 90, 70, 60, 85]

arr = np.array(scores)
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))

df = pd.DataFrame(scores, columns=["Score"])
print(df.describe())

plt.plot(scores)
plt.show()
