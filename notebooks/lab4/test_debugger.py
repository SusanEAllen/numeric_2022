#%%
# step through the code using a debugger
import context
from numlabs.lab4.lab4_functions import initinter41,eulerinter41,midpointinter41
import numpy as np
from matplotlib import pyplot as plt

initialVals={'yinitial': 1,'t_beg':0.,'t_end':0.75,'dt':0.25,'c1':-1.,'c2':1.,'c3':1.}
coeff = initinter41(initialVals)
timeVec=np.arange(coeff.t_beg,coeff.t_end,coeff.dt)
nsteps=len(timeVec)
ye=[]
ym=[]
y=coeff.yinitial
ye.append(coeff.yinitial)
ym.append(coeff.yinitial)
for i in np.arange(1,nsteps):
    ynew=eulerinter41(coeff,y,timeVec[i-1])
    ye.append(ynew)
    ynew=midpointinter41(coeff,y,timeVec[i-1])
    ym.append(ynew)
    y=ynew
analytic=timeVec + np.exp(-timeVec)
theFig,theAxes=plt.subplots(1, 2, figsize=(10, 5))
l1=theAxes[0].plot(timeVec,analytic,'b-',label='analytic')
theAxes[0].set_xlabel('time (seconds)')
l2=theAxes[0].plot(timeVec,ye,'r-',label='euler')
l3=theAxes[0].plot(timeVec,ym,'g-',label='midpoint')
theAxes[0].legend(loc='best')
theAxes[0].set_title('interactive 4.1');
theAxes[1].plot(timeVec, ye-analytic, 'r-', label='euler')
theAxes[1].plot(timeVec, ym-analytic, 'g-', label='midpoint')
theAxes[1].legend(loc='best')
theAxes[1].set_title('Global Error');
# %%
