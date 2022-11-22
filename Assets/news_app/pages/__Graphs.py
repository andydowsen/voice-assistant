import plotly.express as px

# Data to be plotted
df = px.data.iris()

# Plotting the figure
fig = px.scatter_3d(df, x='sepal_width',
                    y='sepal_length',
                    z='petal_width',
                    color='species')

fig.show()