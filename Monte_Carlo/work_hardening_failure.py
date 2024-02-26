import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
#
def voce(p,props):
    [sigma0,T1,Q1,T2,Q2,T3,Q3] = props
    sigmay = sigma0+Q1*(1.0-np.exp(-T1/Q1*p))
    if np.abs(Q2) > 0.0:    
       sigmay += Q2*(1.0-np.exp(-T2/Q2*p))
    if np.abs(Q3) > 0.0:
       sigmay += Q3*(1.0-np.exp(-T3/Q3*p))
    return sigmay
#
def find_failure(props,WC):
    p = np.linspace(0.0,2.0,100000)
    sigmaeq = voce(p,props)
    damage = integrate.cumtrapz(sigmaeq, x=p, initial=0.0)/WC
    indx = np.where(damage >= 1.0)[0][0]
    return p[indx]
#------------------------------------------------------------------------
# Define reference yield stress
#------------------------------------------------------------------------
sigma0 = [267.1]
#------------------------------------------------------------------------
# Define reference work-hardening parameters
#------------------------------------------------------------------------
hard = [32.602, 1.8230, 1425.7, 48.633, 129300.0, 10.675]
#------------------------------------------------------------------------
# Define reference failure parameters
#------------------------------------------------------------------------
failure = [390.47, 33.0, 83.46, 0.950]
#------------------------------------------------------------------------
# Define equivalent plastic strain
#------------------------------------------------------------------------
p = np.linspace(0.0,0.5,10000)
#------------------------------------------------------------------------
# Define distribution of yield stresses
#------------------------------------------------------------------------
sigma0s = np.linspace(240.39,  293.81, 10)
#------------------------------------------------------------------------
# Define distribution of yield stresses
#------------------------------------------------------------------------
fig, axs = plt.subplots(1,3,figsize=(12,4))
#------------------------------------------------------------------------
# Define distribution of yield stresses
#------------------------------------------------------------------------
axs[0].plot(p,voce(p,sigma0+hard),c='k',lw=2)
for i in range(0,10):
    axs[0].plot(p,voce(p,[sigma0s[i]]+hard))
axs[0].grid()
axs[0].set_xlim([0.0,0.5])
axs[0].set_ylim([240.0,360.0])
axs[0].set_ylabel('Equivalent stress (MPa)')
axs[0].set_xlabel('Equivalent plastic strain (-)')
axs[0].set_title('Stres-strain curve')
#------------------------------------------------------------------------
# Plot bending ductility
#------------------------------------------------------------------------
epsf = np.zeros([10])
for i in range(0,10):
    epsf[i] = find_failure([sigma0s[i]]+hard,failure[0])
axs[1].plot(sigma0s,epsf)
axs[1].grid()
axs[1].set_xlim([240.0,300.0])
axs[1].set_ylim([1.1,1.3])
axs[1].set_ylabel('Failure strain (-)')
axs[1].set_xlabel('Initial yield stress (MPa)')
axs[1].set_title('Bending ductility')
#------------------------------------------------------------------------
# Plot membrane ductility
#------------------------------------------------------------------------
# For large shell elements
epsf = np.zeros([10])
for i in range(0,10):
    epsf[i] = find_failure([sigma0s[i]]+hard,failure[1])
axs[2].plot(sigma0s,epsf)
# For small shell elements
epsf = np.zeros([10])
for i in range(0,10):
    epsf[i] = find_failure([sigma0s[i]]+hard,failure[2])
axs[2].plot(sigma0s,epsf)
axs[2].grid()
axs[2].set_xlim([240.0,300.0])
axs[2].set_ylim([0.0,0.3])
axs[2].set_ylabel('Failure strain (-)')
axs[2].set_xlabel('Initial yield stress (MPa)')
axs[2].set_title('Membrane ductility')
# Clean plot and save figure
plt.tight_layout()
plt.savefig('material_properties.pdf')
plt.show()