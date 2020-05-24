import pandas as pd
import plotly.express as px

df = pd.read_csv("./covid_19_data.csv")

df = df.rename(columns={'Country/Region': 'Country'})
df = df.rename(columns={'ObservationDate': 'Date'})

df_countries = df.groupby(['Country', 'Date']).sum().reset_index().sort_values('Date', ascending=False)
df_countries = df_countries.drop_duplicates(subset=['Country'])
df_countries = df_countries[df_countries['Confirmed'] > 0]

# fig = go.Figure(data=go.Choropleth(
#     locations=df_countries['Country'],
#     locationmode='country names',
#     z=df_countries['Confirmed'],
#     colorscale='Reds',
#
# ))

df_countrydate = df[df['Confirmed'] > 0]
df_countrydate = df_countrydate.groupby(['Date', 'Country']).sum().reset_index()

fig = px.choropleth(df_countrydate, locations='Country', locationmode='country names', color='Confirmed',
                    hover_name='Country', animation_frame='Date')

fig.update_layout(
    title_text='Confirmed cases',
    title_x=0.5,
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    )
)

fig.show()
