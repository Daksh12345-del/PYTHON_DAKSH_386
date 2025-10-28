import os
#mkdir help to make a nested folder

for i in range(0,100):
    os.rename(f"data/day{i+1}",f"data/tutorial{i+1}")
