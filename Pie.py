import matplotlib.pyplot as plt
labels = ('Python', 'Java', 'Scala', 'C#')
sizes = [45,30,15,10]

#Only explode the first slice

explode = (0.1,0,0,0)
plt.pie(sizes,
explode = explode,labels=labels,autopct='%1.f%%',
shadow=True,
counterclock = False,
startangle = 45)
plt.savefig('Pie')
plt.show()

