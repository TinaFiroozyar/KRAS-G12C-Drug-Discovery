import matplotlib.pyplot as plt
import numpy as np

# HADDOCK results:
ligands = ['ARS-853', 'JDQ443', 'ARS-1620']
haddock_scores = [-43.8, -41.7, -40.9]
cluster_sizes = [163, 167, 165]
buried_surface = [816.6, 810.1, 802.7]

# color for each ligand:
colors = ['#2ecc71', '#3498db', '#e74c3c']

#  creating the chart
fig, axes = plt.subplots(1, 3, figsize=(15, 6))
fig.suptitle('KRAS G12C — Docking Results Comparison', 
             fontsize=16, fontweight='bold', y=1.02)

# first chart — HADDOCK Score
bars1 = axes[0].bar(ligands, haddock_scores, color=colors, 
                     edgecolor='black', linewidth=0.8)
axes[0].set_title('HADDOCK Score\n(more negative = better)', 
                   fontsize=12, fontweight='bold')
axes[0].set_ylabel('HADDOCK Score')
axes[0].axhline(y=0, color='black', linewidth=0.5)
for bar, score in zip(bars1, haddock_scores):
    axes[0].text(bar.get_x() + bar.get_width()/2., -1,
                f'{score}', ha='center', va='top', 
                fontweight='bold', color='white', fontsize=11)

# second chart — Cluster Size
bars2 = axes[1].bar(ligands, cluster_sizes, color=colors,
                     edgecolor='black', linewidth=0.8)
axes[1].set_title('Cluster Size\n(larger = more consistent)', 
                   fontsize=12, fontweight='bold')
axes[1].set_ylabel('Number of Structures')
axes[1].set_ylim([160, 170])
for bar, size in zip(bars2, cluster_sizes):
    axes[1].text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.1,
                f'{size}', ha='center', va='bottom',
                fontweight='bold', fontsize=11)

# third chart — Buried Surface Area
bars3 = axes[2].bar(ligands, buried_surface, color=colors,
                     edgecolor='black', linewidth=0.8)
axes[2].set_title('Buried Surface Area (Å²)\n(larger = better pocket fit)', 
                   fontsize=12, fontweight='bold')
axes[2].set_ylabel('BSA (Å²)')
axes[2].set_ylim([790, 825])
for bar, bsa in zip(bars3, buried_surface):
    axes[2].text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.2,
                f'{bsa}', ha='center', va='bottom',
                fontweight='bold', fontsize=11)

# overall settings
for ax in axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(axis='x', labelsize=10)

plt.tight_layout()

# saving the output
output = r'C:\Users\MICRO SYSTEM\OneDrive\Desktop\kras.project\figures\fig_docking_comparison.png'
plt.savefig(output, dpi=300, bbox_inches='tight')
print("chart is saved")
plt.show()