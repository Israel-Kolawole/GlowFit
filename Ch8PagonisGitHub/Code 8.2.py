#plot MOK-CW and GOK-CW equation for delocalized processes
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
def MOKCW( Nd,n):
    alpha, g =n10/(n10+Nd), 1/(N1+Nd)
    Ft=np.exp(g*Nd*lamda*t)
    CW=g*(Nd**2.0)*alpha*lamda*Ft/((Ft-alpha)**2.0)
    plt.plot(t,np.log(CW),symbs[n],\
    label=r'$\alpha$='+f'{alpha:.2f}',linewidth=2)
    return CW
def GOKCW(b,n):
    c=(n10/N1)**(b-1)
    CW=n10*c*lamda*(1+c*lamda*(b-1)*t)**(-b/(b-1))   
    plt.plot(t,np.log(CW),symbs[n],\
    label=labls[n],linewidth=2)
n10, N1=1e10, 1e10       
t = np.linspace(0, 130,20)
N1ds=[1e12,1e10,1e8]
symbs=['+-','^-','o-']
plt.subplot(1,2,1)
lamda=0.05
for j in range(1,4): 
    MOKCW(N1ds[j-1],j-1)
plt.text(30,15,"MOK-CW")
plt.xlabel('Time [s]')
plt.ylabel('ln(CW-OSL)')
plt.title('(a)')
leg = plt.legend()
leg.get_frame().set_linewidth(0.0)
plt.subplot(1,2,2)
lamda=0.1
Rs=[1.01,1.5,1.9]
labls=['b='+str(x) for x in Rs]
for j in range(1,4): 
    GOKCW(Rs[j-1],j-1)
leg = plt.legend()
leg.get_frame().set_linewidth(0.0)
plt.xlabel('Time [s]')
plt.text(30,11,'GOK-CW')
plt.ylabel('ln(CW-OSL)')
plt.title('(b)')
plt.tight_layout()
plt.show()