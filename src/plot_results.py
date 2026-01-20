import matplotlib.pyplot as plt
import numpy as np

# Données du rapport (pour être cohérent avec le README)
sizes = ['1000', '2000', '5000']
t_seq = [2.34, 9.78, 42.56]
t_par = [1.17, 4.89, 21.78]

x = np.arange(len(sizes))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 6))
rects1 = ax.bar(x - width/2, t_seq, width, label='Séquentiel', color='#ff9999')
rects2 = ax.bar(x + width/2, t_par, width, label='Parallèle', color='#66b3ff')

ax.set_ylabel('Temps (secondes)')
ax.set_title('Comparaison des performances : Séquentiel vs Parallèle')
ax.set_xticks(x)
ax.set_xticklabels(sizes)
ax.legend()

ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('results/performance_graph.png')
print("Graphique généré dans results/performance_graph.png")
