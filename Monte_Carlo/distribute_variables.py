import numpy as np
import matplotlib.pyplot as plt
#--------------------------------------------------------------------------------------------------------------------
# Define number of samples
#--------------------------------------------------------------------------------------------------------------------
nsamples = 100
#--------------------------------------------------------------------------------------------------------------------
# Define text file name
#--------------------------------------------------------------------------------------------------------------------
filename = 'parameters_v1.txt'
#--------------------------------------------------------------------------------------------------------------------
# Distribute thicknesses
#--------------------------------------------------------------------------------------------------------------------
outer_wall_thicknesses        = np.random.uniform( 2.5, 2.9, nsamples)
inside_wall_side_thicknesses   = np.random.uniform( 1.7, 2.3, nsamples)
inside_wall_middle_thicknesses = np.random.uniform( 1.2, 1.8, nsamples)
#--------------------------------------------------------------------------------------------------------------------
# Distribute geometries
#--------------------------------------------------------------------------------------------------------------------
heigths = np.random.uniform(  75.2,  76.6, nsamples)
widths  = np.random.uniform( 127.2, 128.6, nsamples)
#--------------------------------------------------------------------------------------------------------------------
# Distribute mechanical properties
#--------------------------------------------------------------------------------------------------------------------
sigmays = np.random.uniform(  240.39,  293.81, nsamples)
youngs  = np.random.uniform( 63000.0, 77000.0, nsamples)
#--------------------------------------------------------------------------------------------------------------------
# Plot thickness distribution
#--------------------------------------------------------------------------------------------------------------------
axis_label = ['Outer wall thickness (mm)', 'Inside wall "side" thickness (mm)', 'Inside wall "middle" thickness (mm)']
fig, axs = plt.subplots(1,3,figsize=(12,4))
axs[0].hist(outer_wall_thicknesses,20, density=False)
axs[1].hist(inside_wall_side_thicknesses,20, density=False)
axs[2].hist(inside_wall_middle_thicknesses,20, density=False)
for i in range(0,3):
    axs[i].grid()
    axs[i].set_title(axis_label[i])
plt.tight_layout()
plt.savefig('thickness_distribution.pdf')
plt.show()
#--------------------------------------------------------------------------------------------------------------------
# Plot thickness distribution
#--------------------------------------------------------------------------------------------------------------------
axis_label = ['Height profile (mm)', 'Width profile (mm)']
fig, axs = plt.subplots(1,2,figsize=(8,4))
axs[0].hist(heigths,20, density=False)
axs[1].hist(widths,20, density=False)
for i in range(0,2):
    axs[i].grid()
    axs[i].set_title(axis_label[i])
plt.tight_layout()
plt.savefig('geometry_distribution.pdf')
plt.show()
#--------------------------------------------------------------------------------------------------------------------
# Plot mechanical properties
#--------------------------------------------------------------------------------------------------------------------
axis_label = ['Yield stress (MPa)', 'Elastic modulus (MPa)']
fig, axs = plt.subplots(1,2,figsize=(8,4))
axs[0].hist(sigmays,20, density=False)
axs[1].hist(youngs,20, density=False)
for i in range(0,2):
    axs[i].grid()
    axs[i].set_title(axis_label[i])
plt.tight_layout()
plt.savefig('properties_distribution.pdf')
plt.show()
#--------------------------------------------------------------------------------------------------------------------
# Export parameters
#--------------------------------------------------------------------------------------------------------------------
fp = open(filename,'w')
fp.write('sample,outer_wall_tickness,inside_wall_side_tickness,inside_wall_middle_tickness,height,width,sigma0,youngs\n')
format_string = '{0:3d},{1:3.2f},{2:3.2f},{3:3.2f},{4:4.2f},{5:5.2f},{6:5.2f},{7:6.1f}\n'
for i in range(0,nsamples):
    data2write = [i+1,
                  outer_wall_thicknesses[i],inside_wall_side_thicknesses[i],inside_wall_middle_thicknesses[i],
                  heigths[i],widths[i],
                  sigmays[i],youngs[i]]
    fp.write(format_string.format(*data2write))
fp.close()