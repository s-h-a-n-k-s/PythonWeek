import matplotlib.pyplot as plt

year = [2010, 2011, 2012, 2013, 2014, 2015]
rice = [10, 30, 50, 30, 40, 42]

plt.xlabel("Years")
plt.ylabel("Rice Production")
plt.title("Rice Production 2010 - 2015")
plt.plot(year, rice)

plt.show()