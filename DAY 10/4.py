#(9)
import matplotlib.pyplot as plt


subjects = ['A', 'B', 'C', 'D', 'E']
sem1 = [85, 90, 78, 88, 92]
sem2 = [80, 85, 75, 83, 89]



plt.plot(subjects, sem1, label='Semester 1', marker='o', linestyle='--', color='blue')
plt.plot(subjects, sem2, label='Semester 2', marker='s', linestyle='-', color='green')


plt.title('Semester Results Comparison')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.legend()
plt.grid(True)
plt.show()