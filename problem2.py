import pandas as pd
numbers=[int(input())for _ in range(5)]
sq=pd.Series(numbers)
print(sq)
for i in numbers:
    print(i*i)