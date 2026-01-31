import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
print(os.getcwd())


df=pd.read_csv(r"Project\nenetflix_titles.csv", encoding="utf8")
print(f"Shape:{df.shape}")
print(f"Column:{df.columns}")
df=df.dropna(subset=['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added','release_year', 'rating', 'duration', 'listed_in', 'description'])
type_counts=df['type'].value_counts()
plt.figure(figsize=(8,6))       
plt.bar(type_counts.index,type_counts.values,color=['skyblue','orange'],label='Netflix')
plt.title("Number of Movies Vs TV shows on Netflix")
plt.xlabel("type")
plt.ylabel('count')
plt.legend()
plt.tight_layout()
plt.savefig('Movies_VS_TVshows.png')
plt.show()


rating_counts = df['rating'].value_counts()

plt.figure(figsize=(8,6))
plt.pie(
    rating_counts.values,
    labels=rating_counts.index,
    colors=plt.cm.Pastel1.colors,
    autopct='%1.1f%%',
    startangle=90
)
plt.title('% of Content Ratings')
plt.tight_layout()
plt.savefig("percentage_of_content_rating.png")
plt.show()



movies_df=df[df['type']=='Movie'].copy()
movies_df['duration_int'] = (
    movies_df['duration']
    .str.replace('min','', regex=False)
    .str.strip()
    .astype(int)
)

plt.figure(figsize=(8,6))
plt.hist(movies_df['duration_int'],bins=30,color='skyblue',edgecolor='black')
plt.title("Distribution of movie duration")
plt.xlabel("Duration (minutes)")
plt.ylabel('Number of Movies')

plt.tight_layout()
plt.savefig('Movies_Distribution.png')
plt.show()

release_year=df['release_year'].value_counts().sort_index()
plt.figure(figsize=(8,6))
plt.scatter(release_year.index,release_year.values,marker='^',s=90,color='red')
plt.title("Year VS Number of Shows")
plt.xlabel("year")
plt.ylabel('number')

plt.tight_layout()
plt.savefig('myear_vs_number_of_shows.png')
plt.show()

top_country = (
    df['country']
    .str.split(', ')
    .explode()
    .value_counts()
    .head(10)
)
plt.figure(figsize=(8,6))
plt.barh(top_country.index, top_country.values,color='teal',label='country')
plt.title("Top Country in movies",fontsize=14,fontweight='bold')
plt.xlabel('shows',fontsize=12)
plt.ylabel('country',fontsize=12)
plt.grid(color='black' ,linestyle='-',alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("countries.pdf")
plt.show()
count_by_year= df.groupby(['release_year','type']).size().unstack().fillna(0)
fig, ax=plt.subplots(1,2,figsize=(12,5))
ax[0].plot(count_by_year.index, count_by_year['Movie'],color='blue')
ax[0].set_title("Movie_released per year")
ax[0].set_xlabel('year')
ax[0].set_ylabel("Numberof movies")

ax[1].plot(count_by_year.index, count_by_year['TV Show'],color='orange')
ax[1].set_title("TV shows released per year")
ax[1].set_xlabel('year')
ax[1].set_ylabel("Numberof shows")
fig.suptitle("Comparison of movies relased over years")
plt.tight_layout()
plt.savefig("subplotting.png")
plt.show()