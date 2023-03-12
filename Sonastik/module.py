from gtts import gTTS
rus=[]
est=[]
def slovar(rus_file,est_file):
    language = input("valige keel (rus/est): ")
    if language == "rus":
        loe_failistr(rus_file)
        translater
        editr
    elif language == "est":
        loe_failiste(est_file)
        translateest
        edite
    else:
        print("Vale input. Palun valige 'rus' või 'est'.")


def loe_failistr(rus):
    fail=open(rus,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def loe_failiste(est):
    fail=open(est,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas


def translater(sona,wsona,sonar,sonae,sazik,slovar):
    if sazik == 'rus':
        sonar=input("Kirjuta sõna mida sa tahad tõlkida")
        if sonar not in rus:
            rus.append(sonar)
    nsona = input('Otsitavat sõna pole sõnastikus "{}". Kas sa tahad lisada sõna? (y/n) '.format(sona))
    if nsona.lower() == 'y':
        rus[sona] = input('Sisestage sõna tõlge "{}": '.format(sona))
        wsona('rus.txt', [k + ':' + v for k, v in rus.items()])
        if sazik == 'rus':
            return rus[sona]
        elif sazik == 'est':
            return sona
    else:
        return None

def translateest(sona,wsona,sonae,sazik,slovar):
    if sazik == 'est':
        sonae=input("Kirjuta sõna mida sa tahad tõlkida")
        if sonae not in est:
            est.append(sonae)
    nsona = input('Otsitavat sõna pole sõnastikus "{}". Kas sa tahad lisada sõna? (y/n) '.format(sona))
    if nsona.lower() == 'y':
        est[sona] = input('Sisestage sõna tõlge "{}": '.format(sona))
        wsona('est.txt', [k + ':' + v for k, v in est.items()])
        if sazik == 'rus':
            return est[sona]
        elif sazik == 'est':
            return sona
    else:
        return None

def editr(wsona,sona, translate, rus):
    if sona in rus:
        rus[sona] = translate
        wsona('dictionary.txt', [k + ':' + v for k, v in rus.items()])
        print('Sõnastikku värskendati edukalt!')
    else:
        print('Sõna "{}" ei leidu sõnastikus.'.format(sona))

def edite(wsona,sona, translate, est):
    if sona in est:
        est[sona] = translate
        wsona('dictionary.txt', [k + ':' + v for k, v in est.items()])
        print('Sõnastikku värskendati edukalt!')
    else:
        print('Sõna "{}" ei leidu sõnastikus.'.format(sona))

