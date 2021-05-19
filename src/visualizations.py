import pandas as pd
import plotly.express as px
from umap import UMAP
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

# Total covid cases
def total_cases(data):
    return px.line(data, x='date', y='total_cases', color='location')


# Total covid cases per million inhabitants
def total_cases_mil(data):
    return px.line(data, x='date', y='total_cases_per_million', color='location')


# 7 days moving average of new covid cases
def new_cases_smooth_mil(data):
    return px.line(data, x='date', y='new_cases_smoothed_per_million', color='location')


# Total deaths
def total_deaths(data):
    return px.line(data, x='date', y='total_deaths', color='location')


# Total deaths per million inhabitants
def total_deaths_mil(data):
    return px.line(data, x='date', y='total_deaths_per_million', color='location')


# 7 days moving avg. of new deaths
def new_deaths_smooth_mil(data):
    return px.line(data, x='date', y='new_deaths_smoothed_per_million', color='location')


# COVID-19 virus' reproduction rate (R)
def r_rate(data):
    return px.line(data, x='date', y='reproduction_rate', color='location')


# Stringency index as calculated in Oxford COVID-19 Government Response Tracker, Blavatnik School of Government.
# Interval is from 0 to 100, where 100 is the strictest response
def stringency_index(data):
    return px.line(data, x='date', y='stringency_index', color='location')


def gdp(data):
    df_hdi = data.drop_duplicates(subset='location')
    df_hdi = df_hdi.dropna(subset=['gdp_per_capita'])

    return px.bar(df_hdi, x='location', y='gdp_per_capita', color='location')


# Human development index from UNDP
def hdi(data):
    df_hdi = data.drop_duplicates(subset='location')
    df_hdi = df_hdi.dropna(subset=['human_development_index'])

    return px.bar(df_hdi, x='location', y='human_development_index', color='location')


# Gini index from World Bank Open Data
def gini(data):
    df_gini = data.drop_duplicates(subset='location')
    df_gini = df_gini.dropna(subset=['gini'])

    return px.bar(df_gini, x='location', y='gini', color='location')


# Dimensionality reduction
def dim_red_kmeans(data, cluster, technique):
    if cluster == 'renda':
        features = data.loc[:, 'gdp_per_capita':]
    else:
        features = data.loc[:, 'cardiovasc_death_rate':]

    if technique == 'umap':
        umap_2d = UMAP(n_components=2, init='random', random_state=0)
        proj_2d = umap_2d.fit_transform(features)
    elif technique == 'pca':
        pca = PCA(n_components=2, random_state=0)
        proj_2d = pca.fit(features).transform(features)
    else:
        tsne = TSNE(n_components=2, random_state=0)
        proj_2d = tsne.fit_transform(features)
    
    kmeans = KMeans(n_clusters=7, init="k-means++", max_iter=500, n_init=10, random_state=123)
    identified_clusters = kmeans.fit_predict(proj_2d)

    data['Cluster'] = identified_clusters

    return px.scatter(
        proj_2d, x=0, y=1,
        color=data.Cluster, labels={'color': 'Cluster'},
        hover_name=data.location
    )

