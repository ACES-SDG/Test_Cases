import plotly.express as px
import pandas as pd
df = pd. read_excel("C:/Users/acesi/OneDrive/Desktop/Excel_files/Sample - Superstore2.xlsx")
# df = px.data.gapminder()

# fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp",
# 	         size="pop", color="continent",
#                  hover_name="country", log_x=True, size_max=100)
sum = df['Sales'].sum()
print(sum)
def scatter(clr,sz):
    if clr or sz:
        if clr and sz:
            fig = px.scatter(df, x="Sales", y="Quantity", color=clr,size=sz,
                 hover_name="Country/Region", log_x=True, size_max=100)
            fig.show()

        elif clr:
            fig = px.scatter(df, x="Sales", y="Quantity", color=clr,
                 hover_name="Country/Region", log_x=True, size_max=100)
            fig.show()
        elif sz:
            fig = px.scatter(df, x="Sales", y="Quantity", size=sz,
                 hover_name="Country/Region", log_x=True, size_max=100)
            fig.show()
    else:
        fig = px.scatter(df, x="Sales", y="Quantity",hover_name="Country/Region", log_x=True, size_max=100)
        fig.show()
col = list(df.columns)
clr=col[12]
sz=col[13]


# print(clr,sz,'columns==========================================================================================================')

# scatter(clr,sz)  # case 1 for both colors and size marks

# scatter(clr,'')   # case 2 for only color marks
# scatter('',sz)  # case 3 for only size marks

# scatter('','') # case 4 for non marks

fig = px.scatter(df, x="Sales", y='Quantity', color="Region",
                 hover_name="Country/Region", log_x=True, size_max=100)
# fig.show()