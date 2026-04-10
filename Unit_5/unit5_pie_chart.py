import matplotlib.pyplot as plt
labels = ['A','B','C']
sizes = [30,40,30]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
