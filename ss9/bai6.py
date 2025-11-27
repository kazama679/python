import numpy as np
import matplotlib.pyplot as plt
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
pop = [92, 93, 94, 95, 96, 97, 98, 99, 100, 101]
plt.figure()
plt.plot(years, pop, color='blue', marker='o', linestyle='-')
plt.title("Tăng trưởng dân số Việt Nam 2015–2024")
plt.xlabel("Năm")
plt.ylabel("Dân số (triệu người)")
plt.grid(linestyle='--', alpha=0.6)
plt.legend(["Dân số"])
