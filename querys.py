import pandas as pd

amazon=pd.read_csv("amazonfinal.csv")
disney=pd.read_csv("disneyfinal.csv")
hulu=pd.read_csv("hulufinal.csv")
netflix=pd.read_csv("netflixfinal.csv")

# Qn1

def get_max_duration1(anio,plataforma,min):
    a=int(anio)
    p=str(plataforma)
    q=str(min)
    y=[]
    df=amazon[(amazon["release_year"]==int(a))].durationmovie.max()
    df1=amazon[(amazon["release_year"]==int(a))].durationseason.max()
    df2=disney[(disney["release_year"]==int(a))].durationmovie.max()
    df3=disney[(disney["release_year"]==int(a))].durationseason.max()
    df4=hulu[(hulu["release_year"]==int(a))].durationmovie.max()
    df5=hulu[(hulu["release_year"]==int(a))].durationseason.max()
    df6=netflix[(netflix["release_year"]==int(a))].durationmovie.max()
    df7=netflix[(netflix["release_year"]==int(a))].durationseason.max()
    
    if q=="min" and p=="Amazon":
        for indice, elemento in enumerate(amazon["durationmovie"]): 
            if amazon["durationmovie"][indice].max()==df and amazon["release_year"][indice]==a:
                y.append(amazon["title"][indice])
        return y #("La peli de Amazon con mayor duracion tiene:",x,"minutos, año:",y)
    
    if q=="season" and p=="Amazon":
        for indice, elemento in enumerate(amazon["durationseason"]): 
            if amazon["durationseason"][indice].max()==df1 and amazon["release_year"][indice]==a:
                y.append(amazon["title"][indice])
        return y #("La peli de Amazon con mayor duracion tiene:",x,"minutos, año:",y)

    if q=="min" and p=="Disney":
        for indice, elemento in enumerate(disney["durationmovie"]): 
            if disney["durationmovie"][indice].max()==df2 and disney["release_year"][indice]==a:
                y.append(disney["title"][indice])
        return y #("La peli de Amazon con mayor duracion tiene:",x,"minutos, año:",y)
    
    if q=="season" and p=="Disney":
        for indice, elemento in enumerate(disney["durationseason"]): 
            if disney["durationseason"][indice].max()==df3 and disney["release_year"][indice]==a:
                y.append(disney["title"][indice])
        return y #("La peli de Amazon con mayor duracion tiene:",x,"minutos, año:",y)

    if q=="min" and p=="Hulu":
        for indice, elemento in enumerate(hulu["durationmovie"]): 
            if hulu["durationmovie"][indice].max()==df4 and hulu["release_year"][indice]==a:
                y.append(hulu["title"][indice])
        return y #("La peli de Amazon con mayor duracion tiene:",x,"minutos, año:",y)
    
    if q=="season" and p=="Hulu":
        for indice, elemento in enumerate(hulu["durationseason"]): 
            if hulu["durationseason"][indice].max()==df5 and hulu["release_year"][indice]==a:
                y.append(hulu["title"][indice])
        return y #("La peli de Amazon con mayor duracion tiene:",x,"minutos, año:",y)

    if q=="min" and p=="Netflix":
        for indice, elemento in enumerate(netflix["durationmovie"]): 
            if netflix["durationmovie"][indice].max()==df6 and netflix["release_year"][indice]==a:
                y.append(netflix["title"][indice])
        return y #("La peli de Amazon con mayor duracion tiene:",x,"minutos, año:",y)
    
    if q=="season" and p=="Netflix":
        for indice, elemento in enumerate(netflix["durationseason"]): 
            if netflix["durationseason"][indice].max()==df7 and netflix["release_year"][indice]==a:
                y.append(netflix["title"][indice])
        return y #("La peli de Amazon con mayor duracion tiene:",x,"minutos, año:",y)

#Q n2

def get_count_plataform(plataforma):
    if plataforma=="amazon":
        cantseries=len(amazon[(amazon["type"]=="TV Show")].count(axis=1))
        cantmovie=len(amazon[(amazon["type"]=="Movie")].count(axis=1))
        return "La plataforma Amazon tiene un total de:",cantseries,"series y un total de:",cantmovie,"movies"

    if plataforma=="disney":
        cantseries=len(disney[(disney["type"]=="TV Show")].count(axis=1))
        cantmovie=len(disney[(disney["type"]=="Movie")].count(axis=1))
        return "La plataforma Disney tiene un total de:",cantseries,"series y un total de:",cantmovie,"movies"
    
    if plataforma=="hulu":
        cantseries=len(hulu[(hulu["type"]=="TV Show")].count(axis=1))
        cantmovie=len(hulu[(hulu["type"]=="Movie")].count(axis=1))
        return "La plataforma Hulu tiene un total de:",cantseries,"series y un total de:",cantmovie,"movies"
        
    if plataforma=="netflix":
        cantseries=len(netflix[(netflix["type"]=="TV Show")].count(axis=1))
        cantmovie=len(netflix[(netflix["type"]=="Movie")].count(axis=1))
        return "La plataforma Netflix tiene un total de:",cantseries,"series y un total de:",cantmovie,"movies"

#Q n3

def get_listedin(genero):
    dic={'Fitness':83, 'andCulture':483, 'Animation':547, 'Sports':160, 'Documentary':993, 'Kids':1085, 'Action':1657, 'Arts':483, 'SpecialInterest':980, 'Historical':31, 'MilitaryandWar':44, 'Horror':875, 'TVShows':263, 'YoungAdultAudience':87, 'Suspense':1501, 'Adventure':259, 'TalkShowandVariety':14, 'Entertainment':483, 'LGBTQ':113, 'Romance':674, 'Drama':3687, 'Anime':80, 'MusicVideosandConcerts':155, 'Fantasy':68, 'Unscripted':152, 'International':355, 'ScienceFiction':457, 'Arthouse':141, 'FaithandSpirituality':66, 'Comedy':2099, 'Western':234}
    if genero=="comedy":
        return dic['Comedy']
    if genero=="action":
        return dic['Action']
    if genero=="suspense":
        return dic['Suspense']
    if genero=="drama":
        return dic['Drama']