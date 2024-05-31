{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import matplotlib.pyplot as plt\
import numpy as np\
import pandas as pd\
from math import pi\
def load_and_prepare_data(file_path):\
\'a0 \'a0 data = pd.read_excel(file_path)\
\'a0 \'a0 relevant_data = data[['BOROUGH', 'CONTRIBUTING FACTOR VEHICLE 1']]\
\'a0 \'a0 clean_data = relevant_data.dropna()\
\'a0 \'a0 factor_counts = clean_data.groupby(['BOROUGH', 'CONTRIBUTING FACTOR VEHICLE 1']).size().unstack(fill_value=0)\
\'a0 \'a0 top_factors = factor_counts.sum().nlargest(5).index\
\'a0 \'a0 factor_counts = factor_counts[top_factors]\
\'a0 \'a0 return factor_counts\
if __name__ == "__main__":\
\'a0 \'a0 file_path = 'Motor_Vehicle_Collisions_-_Crashes2.xlsx'\
\'a0 \'a0 factor_counts = load_and_prepare_data(file_path)\
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]\
plt.rcParams['font.family'] = 'Arial'\
plt.rcParams['font.size'] = 12\
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))\
angles = [n / float(len(factor_counts.columns)) * 2 * pi for n in range(len(factor_counts.columns))]\
angles += angles[:1]\'a0 \
for i, (idx, row) in enumerate(factor_counts.iterrows()):\
\'a0 \'a0 data = row.tolist()\
\'a0 \'a0 data += data[:1]\
\'a0 \'a0 ax.plot(angles, data, color=colors[i], linewidth=2, linestyle='solid', label=idx)\
\'a0 \'a0 ax.fill(angles, data, color=colors[i], alpha=0.4)\
ax.set_xticks(angles[:-1])\
ax.set_xticklabels(factor_counts.columns, size=14, color='grey')\
ax.set_ylim(0, factor_counts.values.max() + 10)\
ax.grid(True)\
legend = ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=12)\
legend.get_frame().set_facecolor('white')\
legend.get_frame().set_edgecolor('lightgray')\
plt.show()\
}