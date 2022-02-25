import numpy as np
import matplotlib.pyplot as plt

scores = [100, 68, 40, 78, 81, 65, 39, 118, 46, 78, 9, 37, 43, 87, 54, 29, 95, 87, 111, 65, 43, 53, 47, 16, 98, 82, 58, 5, 49, 67, 60,
          76, 16, 111, 65, 61, 73, 63, 115, 72, 76, 48, 75, 101, 45, 46, 82, 57, 17, 88, 90, 53, 32, 28, 50, 91, 93, 7, 63, 88, 55, 37, 67, 0, 79]

average_score = sum(scores) / len(scores)

avg_score_percent = (average_score/120) * 100


avg_percent_stg = str(avg_score_percent)[0:5]

scores_arr = np.array(scores)

top_frac = sum((scores_arr - average_score) ** 2)


std_scores = np.sqrt(top_frac / (len(scores_arr) - 1))

# I don't know yet how it works yet

plt.hist(scores, 10, alpha=0.5)
plt.axvline(61, color='k', label="Mean")
plt.axvline(89, ls='--', color='k', label="+1 STD")
plt.axvline(33, ls='--', color='k', label="-1 STD")
plt.xlabel('score (out of 120)')
plt.ylabel('Number of Students')
plt.legend()
plt.savefig('./plot')
