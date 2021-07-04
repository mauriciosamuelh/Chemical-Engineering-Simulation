import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Problem:
# Use a mass, species and energy balance to describe the dynamic response in volume, concentration and temperature of a well-mixed vessel

# Define CSTR reactor model
def reactor(x,t,q,qf,Caf,Tf):
    # inputs (4):
    # qf: Inlet volumetric flowrate (L/min)
    # q: Outlet volumetric flowrate (L/min)
    # Caf: Feed concentration (mol/L)
    # Tf: Feed temperature (K)

    # State variables (3):
    # Volume (l)
    V = x[0]
    # Concentration of A (mol/L)
    Ca = x[1]
    # Temperature (K)
    T = x[2]

    # Parameters:
    # Reaction rate
    rA = 0.0

    # Mass Balance
    dVdt = qf - q

    # Species Balance
    dCadt = (qf*Caf - q*Ca)/V - rA - (Ca*dVdt/V)

    # Energy Balance
    dTdt = (qf*Tf - q*T)/V - (T*dVdt/V)

    return [dVdt,dCadt,dTdt]

# Initial condiditons to states
V0 = 1.0
Ca0 = 0.0
T0 = 350.0
y0 = [V0,Ca0,T0]

# Time interval (min)
t = np.linspace(0,10,100)

# Inlet volumetric flowrate (L/min)
qf = np.ones(len(t)) * 5.2
qf[50:] = 5.1

# Outlet volumetric flowrate (L/min)
q = np.ones(len(t)) * 5.0

# Feed concentration (mol/L)
Caf = np.ones(len(t)) * 1.0
Caf[30:] = 0.5

# Feef temperature (K)
Tf = np.ones(len(t)) * 300.0
Tf[70:] = 325.0

# Results storage
V = np.ones(len(t)) * V0
Ca = np.ones(len(t)) * Ca0
T = np.ones(len(t)) * T0

# Loop to each time step
for i in range(len(t) - 1):
    # Simulate
    inputs = (q[i],qf[i],Caf[i],Tf[i])
    ts = [t[i],t[i+1]]
    y = odeint(reactor,y0,ts,args=inputs)
    # Store results
    V[i+1] = y[-1][0]
    Ca[i+1] = y[-1][1]
    T[i+1] = y[-1][2]
    # Adjust initial condition to next step
    y0 = y[-1]

# Construct results and store data
data = np.vstack((t,qf,q,Tf,Caf,V,Ca,T))
data =data.T
np.savetxt('data.txt',data,delimiter=',')

# Plot the inputs and results
plt.figure()

plt.subplot(3,2,1)
plt.plot(t,qf,'b--',linewidth=3)
plt.plot(t,q,'b:',linewidth=3)
plt.ylabel('Flow Rates (L/min)')
plt.legend(['Inlet','Outlet'],loc='best')

plt.subplot(3,2,3)
plt.plot(t,Caf,'r--',linewidth=3)
plt.ylabel('Caf (mol/L)')
plt.legend(['Feed Concentration'],loc='best')

plt.subplot(3,2,5)
plt.plot(t,Tf,'k--',linewidth=3)
plt.ylabel('Tf (K)')
plt.legend(['Feed Temperature'],loc='best')
plt.xlabel('Time (min)')

plt.subplot(3,2,2)
plt.plot(t,V,'b--',linewidth=3)
plt.ylabel('Volume (L)')
plt.legend(['Volume'],loc='best')

plt.subplot(3,2,4)
plt.plot(t,Ca,'r--',linewidth=3)
plt.ylabel('Ca (mol/L)')
plt.legend(['Concentration'],loc='best')

plt.subplot(3,2,6)
plt.plot(t,T,'k--',linewidth=3)
plt.ylabel('T (K)')
plt.legend(['Temperature'],loc='best')
plt.xlabel('Time (min)')

plt.show()