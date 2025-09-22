import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("D:/studies/program.py/Matplotlib/netflix_titles.csv")
df = df.dropna(subset=["type","release_year","rating","country","duration"])    # Drop all rows in the DataFrame df that have missing (NaN) values in any of the specified columns
type_counts = df["type"].value_counts() #Count how many times each unique value appears in the 'type' column of the DataFrame df, and store the result in type_counts
plt.figure(figsize=(6,4))
#type_counts.index: provides the labels (e.g., "Movie", "TV Show").
#type_counts.values: provides the heights of the bars (e.g., 3, 2).
#color=["skyblue", "orange"]: sets custom colors for the bars.
plt.bar(type_counts.index,type_counts.values,color=["skyblue","orange"])
plt.title("Number of Movies Vs TV shows on netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("movies_vs_tvshows.png")
plt.show()

rating_counts = df["rating"].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts,labels=rating_counts.index, autopct="%1.1f%%",startangle=90)
plt.title("Percentage of content ratings")
plt.tight_layout()
plt.savefig("content_Rating_pie.png")
plt.show()

movie_df = df[df["type"]=="Movie"].copy()
movie_df["duration_int"] =movie_df["duration"].str.replace("min","").astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df["duration_int"], bins=30,color="purple",edgecolor="black")
plt.title("Distributation of Movie duration")
plt.xlabel("Duration of (minutes)")
plt.ylabel("Number of movies")
plt.tight_layout()
plt.savefig("movie_duration_histogram.png")
plt.show()

release_counts = df["release_year"].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index,release_counts.values,color="red")
plt.title("Release year vs number of shows")
plt.xlabel("Release year")
plt.ylabel("Number of shows")
plt.tight_layout()
plt.savefig("release_year_Scatter.png")
plt.show()

country_counts = df["country"].value_counts().head(10)
plt.figure(figsize=(6,4))
plt.barh(country_counts.index,country_counts.values,color=["skyblue","orange"])
plt.title("Top 10 countries by number of shows")
plt.xlabel("Number of shows")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("top_10_countries.png")
plt.show()

content_by_year = df.groupby(["release_year", "type"]).size().unstack().fillna(0)
fig, ax = plt.subplots(1, 2, figsize=(12,5))
if "Movie" in content_by_year.columns:
    ax[0].plot(content_by_year.index, content_by_year["Movie"], color="blue")
    ax[0].set_title("Movies released per year")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Number of Movies")
if "TV Show" in content_by_year.columns:
    ax[1].plot(content_by_year.index, content_by_year["TV Show"], color="orange")
    ax[1].set_title("TV Shows released per year")
    ax[1].set_xlabel("Year")
    ax[1].set_ylabel("Number of TV Shows")

fig.suptitle("Comparison of Movies and TV Shows released over years")
plt.tight_layout()
plt.savefig("movies_tv_shows_comparison.png")
plt.show()
