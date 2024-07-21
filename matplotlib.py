import matplotlib.pyplot as plt

# بيانات الباحثين عن عمل لعام 2018
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
job_seekers_2018 = [5000, 5200, 5100, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 6100]

# بيانات الباحثين عن عمل لعام 2019
job_seekers_2019 = [5100, 5300, 5200, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 6100, 6200]

# حساب الفرق بين العامين
difference = []
for i in range(len(job_seekers_2018)):
    difference.append(job_seekers_2019[i] - job_seekers_2018[i])

# رسم البيانات
plt.figure(figsize=(10, 5))

plt.plot(months, job_seekers_2018, marker='o', color='blue', label='2018')
plt.plot(months, job_seekers_2019, marker='s', color='red', linestyle='--', label='2019')
plt.plot(months, difference, marker='x', color='green', linestyle='-.', label='Difference')

plt.title('Comparison of Job Seekers in Oman (2018 vs 2019)', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Job Seekers', fontsize=12)
plt.legend()
plt.grid(True)

plt.show()
