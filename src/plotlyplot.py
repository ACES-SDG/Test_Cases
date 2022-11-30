# import plotly.express as px
# fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
# print(type(fig))
# fig.show()

# import plotly.express as px
# fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])

# import plotly.graph_objects as go
# fig_widget = go.FigureWidget(fig)
# fig_widget


import plotly.express as px

fig =px.scatter(x=range(10), y=range(10))
fig.write_html("file.html")