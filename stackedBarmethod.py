import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_excel("C:/Users/acesi/OneDrive/Desktop/Excel_files/Sample - Superstore2.xlsx")
g_data = df.groupby(['Region','Sub-Category']).aggregate({'Sales':sum}).unstack(-2)

# global fig

def stackedBar():
    # global fig
    fig, ax = plt.subplots(1, figsize=(7, 5))
    print(type(fig))
    for j in list(g_data.columns):
        # if i % 2==0:
        plt.bar(g_data.index, g_data[j].values, )  #color = '#337AE3',
        # print(j)
        # else:
        #     plt.bar(g_data.index, g_data[j].values,  width =0.5,bottom=g_data[g_data.columns[i-1]].values)
        #     print('this is bottom ',g_data[g_data.columns[i-1]])
        #     print(f'\n its j is this {j}')
    # plt.bar(g_data.index, g_data['interest_revenue'], bottom = g_data['sales_revenue'], color = '#5E96E9', width =0.5)
    # plt.bar(g_data.index, g_data['fixed_costs'], color = '#DB4444', width =0.5)
    # plt.bar(g_data.index, g_data['variable_costs'], bottom = g_data['fixed_costs'], color = '#E17979', width =0.5)
    # # x and y limits
    # plt.xlim(-0.6, 10.5)
    # plt.ylim(-1600, 2000)
    # remove spines
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    #grid
    ax.set_axisbelow(True)
    ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.7)
    # x ticks
    # xticks_labels = ['Jan', 'Fev', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
    plt.xticks(rotation=90)
    # title and legend
    # legend_label = ['Sales Revenue', 'Interest Revenue', 'Variable Costs', 'Fixed Costs']
    # plt.legend(legend_label, ncol = 4, bbox_to_anchor=([1, 1.05, 0, 0]), frameon = False)
    
    # plt.title('My Company - 2020\n', loc='left')
    # plt.show()
    return fig
stackedBar()