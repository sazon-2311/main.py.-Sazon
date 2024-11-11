# "Средний балл"
# "Воднные данные"
#Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] оценки учеников
#Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} - имена учеников
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
order=sorted(list(students)) #"перевел с множества в список и упорядочил"
q=sum(grades[0])/len(grades[0])  #"вычеследние среднего балла"
w=sum(grades[1])/len(grades[1])
e=sum(grades[2])/len(grades[2])
r=sum(grades[3])/len(grades[3])
t=sum(grades[4])/len(grades[4])
points=(q,w,e,r,t) #"Средний бал всех учеников"
finish=dict(zip(order,points)) #"нашел в интернете как перевести списки в словарь"
print(finish)