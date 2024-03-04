import numpy as np
import matplotlib.pyplot as plt

nsamples = 10000

outer_wall_thicknesses = np.random.uniform(2.5, 2.9, nsamples)

# Option 1
inside_wall_side_thicknesses_1 = np.zeros(nsamples)
inside_wall_middle_thicknesses_1 = np.zeros(nsamples)
for i in range(0, nsamples):
    inside_wall_side_thicknesses_1[i] = np.random.uniform(1.7, 2.3)
    inside_wall_middle_thicknesses_1[i] = np.random.uniform(1.2, 1.8)
    while inside_wall_middle_thicknesses_1[i] > inside_wall_side_thicknesses_1[i]:
        inside_wall_side_thicknesses_1[i] = np.random.uniform(1.7, 2.3)
        inside_wall_middle_thicknesses_1[i] = np.random.uniform(1.2, 1.8)




# Option 2
MAX_SIDE_WALL_SIDE_THICKNESS = 2.3
MIN_SIDE_WALL_SIDE_THICKNESS = 1.7
inside_wall_middle_thicknesses_2 = np.random.uniform(1.2, 1.8, nsamples)
max_ratios_between_side_and_middle = np.array([MAX_SIDE_WALL_SIDE_THICKNESS/inside_wall_middle_thicknesses_2[i] for i in range(0, nsamples)])
min_ratios_between_side_and_middle = np.array([max(1, MIN_SIDE_WALL_SIDE_THICKNESS/inside_wall_middle_thicknesses_2[i]) for i in range(0, nsamples)])
ratio_between_side_and_middle = np.array([np.random.uniform(min_ratios_between_side_and_middle[i], max_ratios_between_side_and_middle[i]) for i in range(0, nsamples)])
inside_wall_side_thicknesses_2 = ratio_between_side_and_middle*inside_wall_middle_thicknesses_2

# Plot thickness distribution - histogram
axis_label = ['Outer wall thickness (mm)', 'Inside wall "side" thickness (mm)', 'Inside wall "middle" thickness (mm)']
fig, axs = plt.subplots(1,3,figsize=(12,4))
axs[0].hist(outer_wall_thicknesses,20, density=False)
axs[1].hist(inside_wall_side_thicknesses_1,20, density=False)
axs[2].hist(inside_wall_middle_thicknesses_1,20, density=False)
for i in range(0,3):
    axs[i].grid()
    axs[i].set_title(axis_label[i])
plt.tight_layout()
plt.savefig('Option_1.pdf')
plt.show()

axis_label = ['Outer wall thickness (mm)', 'Inside wall "side" thickness (mm)', 'Inside wall "middle" thickness (mm)']
fig, axs = plt.subplots(1,3,figsize=(12,4))
axs[0].hist(outer_wall_thicknesses,20, density=False)
axs[1].hist(inside_wall_side_thicknesses_2,20, density=False)
axs[2].hist(inside_wall_middle_thicknesses_2,20, density=False)
for i in range(0,3):
    axs[i].grid()
    axs[i].set_title(axis_label[i])
plt.tight_layout()
plt.savefig('Option_2.pdf')
plt.show()