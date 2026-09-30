"""Exact source-map diagram and rational counterexample, without a TeX engine."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
H=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(15,6.8))
ax.set(xlim=(0,15),ylim=(0,6.8));ax.axis('off')
color='#205777'
def text(x,y,s,size=19,**kw):
    return ax.text(x,y,s,fontsize=size,ha='center',va='center',**kw)
def arrow(a,b,label,offset=.28):
    ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',color=color,lw=2))
    text((a[0]+b[0])/2,(a[1]+b[1])/2+offset,label,18)
text(3.6,6.45,'Preserve the original maps',24)
text(11.1,6.45,'A concrete missing-square test',24)
for x,s in [(1,'$M$'),(3.5,'$P$'),(6,'$M$')]:text(x,5.3,s,27)
arrow((1.4,5.3),(3.1,5.3),r'$\pi$')
arrow((3.9,5.3),(5.6,5.3),r'$i$')
text(3.5,4.25,r'$\alpha=i\pi,\qquad a=\pi\alpha i=(\pi i)^2$',23)
text(3.5,3.4,r'$i a^j\pi=\alpha^{2j+1}\quad(j\geq0)$',23)
text(3.5,2.5,r'$P(a)=0\quad\Longrightarrow\quad\alpha P(\alpha^2)=0$',22)
text(3.5,1.4,r'$E=U(\alpha)\,\alpha^2 Q_1(\alpha),\qquad E^2=E$',21)
text(3.5,.7,r'$M=\operatorname{Im}(E)\oplus\operatorname{Im}(1-E)$',21)
text(11.2,5.3,r'$R=\mathbf{Q},\ M=P=\mathbf{Q}^2,\ \pi=I,\ i=\mathrm{diag}(1,-1)$',18)
text(11.2,4.55,r'$a=I,\qquad P(T)=(T-1)^2,\qquad x=(1,0)$',20)
text(11.2,3.55,r'$\alpha^2 P(\alpha)=\mathrm{diag}(0,4)\ne0$',23,color='#912b32')
text(11.2,2.6,r'$\alpha^2 P(\alpha^2)=0$',24,color=color)
text(11.2,1.75,r'$Q_1=(T+1)^2,\quad Q_2=(T-1)^2,\quad U=(4-3T)/4$',18)
text(11.2,.85,r'$E=\mathrm{diag}(1,0),\quad x\in\operatorname{Im}(E)$',22)
fig.text(.5,.014,'Stacks Project, algebra.tex 42718–42760; complete correction and all comparison maps: ALGEBRA_HENSELIAN_NOTES_20260929.md.',ha='center',fontsize=11)
fig.subplots_adjust(left=.025,right=.985,top=.99,bottom=.07)
for suffix in ['svg','png']:
    fig.savefig(H/('HENSELIAN_PROJECTION_20260929.'+suffix),dpi=160)
print('Saved the exact projection diagram as SVG and PNG.')
