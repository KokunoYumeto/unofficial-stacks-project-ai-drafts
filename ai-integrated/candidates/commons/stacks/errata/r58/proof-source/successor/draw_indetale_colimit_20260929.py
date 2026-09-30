"""Draw the exact colimit quotient and nil-ideal sequence."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
H=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(14,6));ax.set(xlim=(0,14),ylim=(0,6));ax.axis('off')
def txt(x,y,s,size=19):ax.text(x,y,s,ha='center',va='center',fontsize=size)
def arr(a,b,label):
    ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',lw=2,color='#205777'))
    txt((a[0]+b[0])/2,(a[1]+b[1])/2+.32,label,17)
txt(7,5.7,'The original colimit and its finite idempotent quotients',23)
txt(2,4.5,r'$Q=\bigotimes_{k,R} B_k$',24)
txt(7,4.5,r'$Q_{d_F}\cong Q/(1-d_F)Q$',23)
txt(12,4.5,r'$Q/J$',24)
arr((3.4,4.5),(4.8,4.5),r'$q\mapsto q/1$')
arr((9.25,4.5),(11.3,4.5),r'$q/d_F^m\mapsto [q]$')
txt(7,3.5,r'$d_F=\prod_{h\in F}d_h,\quad J=\sum_h(1-d_h)Q,\quad Q/J\cong\mathrm{colim}_{F\ \mathrm{finite}}Q_{d_F}$',22)
txt(7,2.75,'Each stage in the middle is ind-étale; the arrows retain the actual quotient classes.',16)
txt(7,2,'Reduction modulo a nil ideal keeps its exact kernel',22)
txt(.6,1.05,r'$0$',23);txt(3.1,1.05,r'$N\otimes_R A$',24)
txt(7,1.05,r'$A$',24);txt(10.8,1.05,r'$A/NA$',24);txt(13.5,1.05,r'$0$',23)
arr((.9,1.05),(1.9,1.05),'')
arr((4.45,1.05),(6.55,1.05),r'$n\otimes a\mapsto na$')
arr((7.4,1.05),(9.85,1.05),r'$a\mapsto[a]$')
arr((11.75,1.05),(13.15,1.05),'')
txt(7,.32,r'$A$ is ind-étale over $R$; $N\subset R$ is a nil ideal.',15)
fig.text(.5,.035,'Proofs and source comparisons: ALGEBRA_INDETALE_NOTES_20260929.md; Stacks Project authors, algebra.tex 42761–42958 and earlier diagonal/lifting results.',ha='center',fontsize=10)
fig.subplots_adjust(left=.02,right=.98,top=.99,bottom=.07)
for suffix in ['svg','png']:fig.savefig(H/('INDETALE_COLIMIT_MAPS_20260929.'+suffix),dpi=160)
print('Saved the exact colimit and reduction diagrams.')
