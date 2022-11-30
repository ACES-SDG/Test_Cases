from typing import List
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure
import matplotlib.gridspec as gridspec
from mplcursors import cursor  # separate package must be installed

def onclick(event):
    ax = event.inaxes
    x = event.xdata
    lbls = ax.get_xticklabels()
    idx = int(x.round())
    lbl = lbls[idx]
    print(lbl.get_text())
    
    
def on_plot_hover(event):
    ax = event.inaxes
    
    # Iterating over each data member plotted
    for curve in ax.get_lines():
        # Searching which data member corresponds to current mouse position
        if curve.contains(event)[0]:
            print("over %s" % curve.get_gid())
            
            
            
def func_LOD_two_x(df:pd.DataFrame = ..., x_axis:List[str] = ..., y_axis:List[str]=...)->Figure:
    
    first_category = x_axis[0]
    # fetching the uniques of first category from selected x_axis   
    uniques = list(df[first_category].unique())
    uniques.sort()
    no_cols = len(uniques)
    no_rows= len(y_axis)
    
    # initializing the matplotlib figure 
    # figure, (ax1, ax2, ax3 , ax4) = plt.subplots(1, 4, sharey=True)
    f, axarr = plt.subplots(no_rows, no_cols,sharey=True, gridspec_kw = {'wspace':0, 'hspace':0})   # 
    x =x_axis[1]
    y =y_axis[0]
    # gs1 = gridspec.GridSpec(1,4)
    
    # for unique , ax  in zip(uniques,(ax1,ax2,ax3,ax4)):
    # for y in y_axis:
        # print(y)
    for unique , ax in zip(uniques,f.axes):
        run_df = df[df[first_category]==unique]
        # plt.subplot(no_cols , no_rows , index+1)
        # print(ax )
        # count+= count
        grp_df = run_df.groupby(x).aggregate({y:sum})
        
        y_final = tuple(grp_df[y])
        x_final = tuple(grp_df[y].keys())
        # for y in y_axis:
        ax.bar(x_final,y_final)
         
        """ set title for each sub plot """
        ax.set_title(f'{unique}')
        cursor(hover=True)
        # if unique == uniques[0]:
        #     ax.set_ylabel(f'{y}')
        # plt.xticks(rotation=90)
        # if unique == uniques[-1]:
        #     # print(unique, 'at ', uniques.index(unique))
        # ax.set_xticks(ticks =df[x].unique() ,rotation = 90)
        # ax.set_xticklabels(labels =df[x].unique() , rotation=90)
        # else:
        #     ax.set_xticklabels([])
        
        """ adjust the figure by shrinking the plot from bottom """
        plt.subplots_adjust(bottom=0.25 )
        
        # ax.xticks()
        # gs1.update(wspace=0, hspace=0.1)
        # ax.set_aspect('auto')
        ax.set_xticklabels(labels =x_final , rotation=90,fontname = "Times New Roman")
        # plt.margins(0)
        # x__axis = ax.get_xaxis()
        """set y-axis lable for figure """
        f.supylabel(f'{y}')
        """hide tick and tick label of the big axis"""
        ax.tick_params(left=False) #top=False, bottom=False, right=False
        """set x-axis label for the figure """
        f.supxlabel(f'{x}')
        
        f.canvas.mpl_connect('button_press_event', onclick)
        # f.canvas.mpl_connect('motion_notify_event', on_plot_hover)   
        # plt.xticks(rotation=90)
    plt.show()
    return f

df = pd.read_excel("C:/Users/Mazhar/OneDrive/Desktop/LIve_Working/Ocean Pro V_3.0.0/Excel_files/sales.xlsx")

x = ['Ship Mode','Sub-Category']
y = ['Quantity']
fig = func_LOD_two_x(df,x_axis=x,y_axis=y)