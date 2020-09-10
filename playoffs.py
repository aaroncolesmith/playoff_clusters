import pandas as pd
import streamlit as st
import plotly_express as px

st.title('NBA Playoffs Clusters')
df=pd.read_csv('./playoffs.csv')
p=pd.read_csv('./pca.csv')
st.write(df.head(3))
df['Cluster']=df['Cluster'].astype('str')

fig=px.scatter(df,
               x='Cluster_x',
               y='Cluster_y',
               color='Cluster',
               hover_data=['Player','PTS','TRB','AST','STL','BLK','match'],
#                text=df['Starters']
              )
fig.update_traces(textposition='top center',marker=dict(size=10,opacity=.8,line=dict(width=1,color='DarkSlateGrey')))
fig.update_layout(legend_title_text='Cluster')

advanced = st.checkbox('Advanced mode: show features on plot?')

if advanced:
    for i,r in p.iterrows():

        fig.add_annotation(
            x=r['x']*20,
            y=r['y']*20,
            text=r['field'],
        showarrow=False,
        bgcolor="white",
        opacity=.75)

st.plotly_chart(fig)
