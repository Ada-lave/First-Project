import pandas as pd
df_anime = pd.DataFrame({
    'anime_name':['Naruto','Bleach','Akame','Demon Slayer'],
    'length_in_serial':[124,156,36,36],
    'type':['Rpg','Slaer','gg_mertv','gg-top']
})
print(df_anime)

select_serial = int(input('Введите сколько серий предпочитаете'))
print(df_anime[df_anime.length_in_serial<=select_serial][['anime_name','type']])