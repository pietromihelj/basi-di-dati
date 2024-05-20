import pymongo
# Connessione a MongoDB
connessione = pymongo.MongoClient("mongodb://localhost:27017")
#creo il db
seventh_sea = connessione.seventh_sea
#creo le varie collezzioni
campagne = seventh_sea.campagne
personaggi = seventh_sea.personaggi
navi = seventh_sea.navi
storie = seventh_sea.storie
linee_guida = seventh_sea.linee_guida

#file di linee guida
lin = [
        {   'nome': 'nazioni',
            'nomi':[lista dei nomi -> stringhe],
            'bonus':[[tratti della prima nazione].....[tratti della n-esima nazione] -> liste di stringhe],
            'bonus_navi':[vantaggio dato dalla prima nazione,...,vantaggio dato dalla seconda -> lista di stringhe]
               },
        {   'nome': 'background',
            'nomi':[lista dei nomi -> stringhe],
            'descrizione':[lista di descrizioni -> stringhe],
            'peculiarità':[lista di peculiarità -> stringhe],
            'vantaggi':[[vantaggi primo background]...[vantaggi n-esimo background] -> liste di stringhe]
                },
        {   'nome': 'hubris',
            'nomi':[lista dei nomi -> stringhe],
            'descrizione':[lista di descrizioni -> stringhe]
              },
        {   'nome':'virtu',
            'nomi':[lista dei nomi -> stringhe],
            'descrizione':[lista di descrizioni -> stringhe],
              },
         {  'nome':'vantaggi',
            'nomi':[lista dei nomi -> stringhe],
            'costo':[array di costi -> interi tra 1 e 5],
            'descrizione':[lista di descrizioni -> stringhe],
            'tipo':[lista dei tipi, 1 per ogni vantaggio. 3 possibilità 'Normale', 'Innato','Talento' -> stringhe],
            'dadi':[descrive un eventuale aumento di dadi da lanciare -> 0 o 1]
             },
        {   'nome':'società segrete',
            'nomi':[lista dei nomi -> stringhe],
            'valori':[lista con le descrizioni dei valori morali perseguiti da ogni società -> stringhe],
            'favori':[{favore:costo,...,favore:costo}...{favore:costo,...,favore:costo} -> array di dizionari contenenti le coppie di favori e costo],
            'aiuti':[{aiuto:costo,..., aiuto:costo}...{aiuto:costo,..., aiuto:costo} -> array di dizionari con le coppie aiuto e costo]
                   }    
]

linee_guida.insert_many(lin)

#file tipo

# campi con + sono solo per gli eroi, i campi con - sono solo per i malvagi o i png, i campi con * sono opzionali
campagna = {'nome': nome della campagna -> stringa,
            'personaggi':[lista dei nomi dei personaggi nella campagna -> lista di stringhe],
            'navi':[lista dei nomi delle navi nella campagna -> lista di stringhe],
            'storie':[lista dei titoli delle storie della campagna -> lista di stringhe],
            'punti_pericolo': -> intero positivo
            }

personaggio = { 'nome': nome del personaggio -> stringa,
                'campagna': nome della campagna di cuì fa parte, una tra nomi campagne -> stringa,
                'tipo': uno tra 'Eroe' o 'Malvagio' o 'Png' -> stringa,
                'descrizione': descrizione fisica del personaggio -> stringa,
                'nazione': una tra quelle nelle linee guida -> stringa,
                'fede': una tra la lista delle fedi -> stringa,
                'fama':[lista dei titoli con cuì è conosciuto e per cui è famoso -> lista di stringhe],
                'giocatore+':nome del giocatore che ha inserito il persoanggio -> stringa,
                'spirale della morte+':[coppia di numeri -> primo un intero 0-16, secondo un intero 0-4],
                'tratti+':{tratto:n,...,tratto:n -> dizionario con i nomi dei tratti e un intero tra 2 e 5},
                'abilità+':{abilità:n,...,abilità:n -> dizionario con i nomi delle abilità e un intero tra 0 e 5},
                'vantaggi+':[lista dei nomi dei vantaggi, un tot tra le linee guida -> stringhe],
                'hubris+':una hubris tra le linee guida -> stringa,
                'virtu+':una virtu tra le linee guida -> stringa,
                'background+':[lista di 2 nomi dei background, tra le linee guida -> stringhe],
                'oggetti':[lista degli oggetti posseduti dal personaggi -> stringhe],
                'punti eroe+': n -> intero positivo,
                'corruzzione+':n -> intero tra 0-5,
                'ricchezza+':n -> intero positivo,
                'forza-':n -> intero positivo,
                'influenza-':n -> intero positivo,
                'ruolo*':uno tra la lista dei ruoli del personaggio sulla nave -> stringa,
                'nave*':la nave dove ha il suddetto ruolo -> stringa,
                'storie*':[titoli delle storie di cui fa parte -> lista di stringhe],
                'affiliazione*':[società/malvagio è il nome della società segreta, nelle linee guida, o di un malvagio, tra i personaggi -> lista di stringhe]
                }

nave = {'nome':nome della nave -> stringa,
        'campagna': nome della campagna di cuì fa parte, una tra nomi campagne -> stringa,
        'origini':una tra nazioni -> stringa,
        'leggende*':[una serie tra la lista delle leggende -> lista di stringhe],
        'avventure*':[una serie tra la lista delle avventure -> lista di stringhe],
        'composizione_equipaggio':{ruolo:n,..,ruolo:n dizionario con coppie ruolo, dalla lista dei ruoli del personaggio sulla nave e numerosità, intero positivo},
        'personaggi':[array dei personaggi legati a questa nave -> array di stringhe]
        }

storia = {'titolo': titolo della storia -> stringa,
          'campagna': nome della campagna di cuì fa parte, una tra nomi campagne -> stringa,
          'tipo': uno tra 'GM','Eroe','Macchinazione' -> stringa,
          'scopo': azione conclusiva della storia -> stringa,
          'atti':[lista degli atti, obbiettivi intermedi, di cuì è composta la storia -> lista di stringhe],
          'protagonista':[lista di nomi dei personaggi che riceveranno la ricompensa -> lista di stringhe],
          'ricompensa':[lista di ricompense una ogni protagonista -> lista di stringhe]
          }



##funzioni di ricerca##
#funzione per la ricerca delle info su un personaggio
def ricerca_personaggio(nomi): #camp è il nome della campagna in gioco al momento
    personaggi = seventh_sea.personaggi
    #trovo i nomi dei personaggi nella campagna
    personaggi_esistenti = storie.find({})
    nomi_esistenti = []
    for element in personaggi_esistenti:
        nomi_esistenti.append(element['titolo'])
    for ognuno in nomi:
        if ognuno not in personaggi_esistenti:
            print('\n',ognuno,' non è un personaggio di questa campagna')
            nomi.remove(ognuno)
    for name in nomi:                   #lista dei nomi di uno o più personaggi da cercare
        q = {{'nome': name}}
        pers = personaggi.find(q)
        for i in pers:
            print('\n',i)

#funzione per la ricerca di info sulle navi
def ricerca_navi(nomi):
    navi = seventh_sea.navi
    #cerco i nomi di tutte le navi che ho
    navi_esistenti = navi.find({})
    nomi_esistenti = []
    for element in navi_esistenti:
        nomi_esistenti.append(element['titolo'])
    for ognuna in nomi:             
        if ognuna not in nomi_esistenti:
            print('\n',ognuna,' non è una nave di questa campagna')
            nomi.remove(ognuna)
    for nave in nomi:                   
        q = {{'nome': nave}}
        #print(navi.find(q))
        nav = navi.find(q)
        for i in nav:
            print('\n',i)    

#funzione di ricerca info sulle storie
def ricerca_storie(titolo):
    storie = seventh_sea.storie
    #cerco i tiolidi tutte le storie che ho
    storie_esistenti = storie.find({})
    titoli_esistenti = []
    for element in storie_esistenti:
        titoli_esistenti.ppend(element['titolo'])
    for ognuno in titolo:
        if ognuno not in titoli_esistenti:
            print('\n',ognuno,' non è una storia di questa campagna')
            titolo.remove(ognuno)
    for storia in titolo:
        q = {{'titolo':storia}}
        #print(storie.find(q))
        sto = storie.find(q)
        for i in sto:
            print('\n',i) 

#funzione di ricerca info sulle campagne
def ricerca_campagna(camp):
    campagne = seventh_sea.campagne
    campagne = campagne.find({})
    nome_campagne = []
    for element in campagne:
        nome_campagne.append(element['nome'])
    for ognuna in camp:
        if ognuna not in nome_campagne:
            #se la campagna non esiste la rimuovo dalla ricerca
            print('\n',ognuna,' non è una campagna esistente')
            camp.remove(ognuna)
    for campagna in camp:
        q = {'nome':camp}
        #print(campagne.find(q))
        ca = campagne.find(q)
        for i in ca:
            print('\n',i)

#funzione di ricerca sulle linee guida
def ricerca_linee_guida(cosa): #cosa è una lista con dentro le cose da cercare tre le linee guida
    linee_guida = seventh_sea.linee_guida
    for element in cosa:
        if element not in ['nazioni','background','arcani','vantaggi','società segrete']:
            print('\n',element,' non è nelle linee guida')
            cosa.remove(element)
    for element in cosa:
        q = {'nome': cosa}
        #print(linee_guida.find(q))
        co = linee_guida.find(q)
        for i in co:
            print('\n',i)


##funzioni di inserimento dati##
def inserimento_personaggio(): #argomenti sono i campi da inserie 
    #mi collego alle collection per ricavare le info di cui ho bisogno
    personaggi = seventh_sea.personaggi
    campagne = seventh_sea.campagne
    navi = seventh_sea.navi
    linee_guida = seventh_sea.linee_guida
    storie = seventh_sea.storie
    info_personaggio = {}
    #una serie di campi sono validi solo se cio che inserisce l'utente sta in una lista predefinita
    #creo le liste di controllo
        #campagne
    campagna = campagne.find({})
    nomi_campagne = []
    for element in campagna:
        nomi_campagne.append(campagna[element]['nome'])
        #tipo
    tipi = ['Eroe','Png','Malvagio']
        #nazioni
    nomi_nazioni = linee_guida.find({'nome':'nazioni'})
    nomi_nazioni = nomi_nazioni['nomi']
        #fede
    fedi = ['Druidismo','Vaticino', 'Chiesa di Avalon', 'Obiezionismo', 'pagana Inish', 'pagana Highland', 'Ateo', 'pagana Rzeczpospolitana', 'pagana Curoniana', 'Chiesa Ortodossa Ussurana', 'pagana Ussurana', 'pagana Vesten']
        #tratti
    tratti = ['vigore','grazia','risolutezza','acume','panache']
        #abilità
    abilità = ['allettare','a.d.guerra','atletica','cavalcare','convincere','empatia','esibirsi','furto','intimidire','istruzione','mira','mischia','nascondersi','navigazione','notare','rissa']
        #vantaggi
    nomi_vantaggi = linee_guida.find({'nome':'vantaggi'})
    nomi_vantaggi = nomi_vantaggi['nomi']
        #hubris
    nomi_hubris = linee_guida.find({'nome':'hubris'})
    nomi_hubris = nomi_hubris['nomi']
        #virtù
    nomi_virtu = linee_guida.find({'nome':'virtù'})
    nomi_virtu = nomi_virtu['nomi']
        #background
    nomi_background = linee_guida.find({'nome':'background'})
    nomi_background = nomi_background['nomi']
        #ruolo
    ruoli = ['comandante','nostromo','cannoniere','medico di bordo','cadetto','marinaio di lungo corso','marinaio scelto','marinaio semplice']
        #nome delle organizzazioni a cui posso essere affiliato
    nomi_socseg = linee_guida.find({'nome':'società segrete'})
    nomi_socseg = nomi_socseg['nomi']
    

    ##inserimento vero e proprio dei dati
    #inserisco quelli obbligatori per entrembi
    #prima di tutto la campagna
    print('\ninserisci una campagna tra: ',nomi_campagne)
    campagna = input()
    while campagna not in nomi_campagne:
        print('\ninput errato, inserisci di nuovo ')
        campagna = input()
    info_personaggio.update({'campagna':campagna})
    
    #una volta trovata la campagna posso cercare navi,storie e personaggi di quella campagna per in caso collegarle
    #nome personaggi 
    personaggi_camp = campagne.find({'nome':campagna})
    personaggi_camp = personaggi_camp['personaggi']
    #storie del gm. ogni eroe deve far perte delle storie del gm
    storia = storie.find({'tipo':'gm'},{'campagna':campagna})
    nomi_storie = []
    for element in storia:
        nomi_storie.append(storia[element]['titolo'])
     #navi
    nave = navi.find({})                
    nome_navi = []              
    for element in nave:
        nome_navi.append(nave[element]['nome'])
    #posso ora definire le affiliazioni
    affiliazioni = personaggi_camp.extend(nomi_socseg)

    #inserisco il nome che non può essere duplicato
    pers1 = personaggi.find({})                
    nomi_pers = []              
    for element in pers1:
        nomi_pers.append(pers1[element]['nome'])
    print('\ninserisci il nome del personaggio: ')
    name = input()
    while name in nomi_pers:
        print('personaggio gia esistente cambia nome')
        name = input()
    info_personaggio.update({'nome':name})
    
    

    #poi inserisco il tipo che mi serve per definire che argomenti avrà
    print('\ninserisci un tipo tra: ',tipi)
    tipo = input()
    while tipo not in tipi:
        print('input errato, inserisci di nuovo ')
        tipo = input()
    info_personaggio.update({'tipo':tipo})
    
    #descrizione
    print('\ninserisci una desrizione: ')
    descrizione = input()
    info_personaggio.update({'descrizione':descrizione})

    #nazione
    print('\ninserisci una nazione tra: ',nomi_nazioni)
    nazione = input()
    while nazione not in nomi_nazioni:
        print('input errato, inserisci di nuovo ')
        nazione = input()
    info_personaggio.update({'nazione':nazione})

    #fede
    print('\ninserisci una fede tra: ',fedi)
    fede = input()
    while fede not in fedi:
        print('input errato, inserisci di nuovo ')
        fede = input()
    info_personaggio.update({'fede':fede})

    #fama
    print('\ninserisci i titoli con cui è conosciuto. quando vuoi fermarti inserisci stop: ')
    ins = input()
    fama = []
    while ins != 'stop':
        fama.append(ins)
        print('\n')
        ins = input()
    info_personaggio.update({'fama':fama})

    #oggetti: inserisco una serie di oggetti
    print('\ninserisci gli oggetti posseduti dalpersonaggio. quando vuoi fermarti inserisci stop: ')
    ins = input()
    oggetti = []
    while ins != 'stop':
        oggetti.append(ins)
        print('\n')
        ins = input()
    info_personaggio.update({'oggetti':oggetti})
    
    if tipo == 'Eroe':
        #come prima cosa inserisco il giocatore che giocherà il personaggio
        print('\ninserisci il nome del giocatore')
        giocatore = input()
        info_personaggio.update({'giocatore':giocatore})
        #la spirale della morte è 0 di defaula
        info_personaggio.update({'spirale della morte':[0,0]})
        #tratti: devo inserire un valore tra 2 e 5 per ogni tratto
        val_tratti = {}
        for tratto in tratti:
            print('\ninserisci un numero intero tra 2 e 5 per il tratto: ',tratto)
            val = input()
            while int(val) not in range(2,6):
                print('\ninput errato, inserisci di nuovo ')
                val = input()
            val_tratti.update({tratto:val})
        info_personaggio.update({'tratti':val_tratti})
        #abilità: come sopra
        val_abilita = {}
        for abi in abilità:
            print('\ninserisci un numero intero tra 0 e 5 per abilità: ',abi)
            val = input()
            while int(val) not in range(0,6):
                print('\ninput errato, inserisci di nuovo ')
                val = input()
            val_abilita.update({abi:val})
        info_personaggio.update({'abilità':val_abilita})
        
        #hubris
        print('\ninserisci una hubris tra: ',nomi_hubris)
        hubris = input()
        while hubris not in nomi_hubris:
            print('\ninput errato, inserisci di nuovo ')
            hubris = input()
        info_personaggio.update({'hubris':hubris})
        #virtu
        print('\ninserisci una virtu tra: ',nomi_virtu)
        virtu = input()
        while virtu not in nomi_virtu:
            print('\ninput errato, inserisci di nuovo ')
            virtu = input()
        info_personaggio.update({'virtu':virtu})
        #background
        print('\ninserisci 2 background tra: ',nomi_background)
        background = []
        for i in range(0,1):
            print('\ninserisci il primo background')
            back = input()
            while back not in nomi_background:
                print('\ninput errato, inserisci di nuovo ')
                back = input()
            background.append(back)
        info_personaggio.update({'background':background})
        #vantaggi
        vantaggi = []
        #forniti dal background
        vantaggi_back = linee_guida.find({'nome':'background'})
        vantaggi_back = vantaggi_back['vantaggi']
        for element in background:
            vantaggi = vantaggi+vantaggi_back[nomi_background.index(element)]
        #comprati    
        print('seleziona uno o piu vantaggi. per fermarti digita stop. scegli tra: ',nomi_vantaggi )
        va = input()
        while va != 'stpo':
            while va not in nomi_vantaggi:
                print('errato, inserisci di nuovo')
                va = input
            vantaggi.append(va)
            print('inserisci il prossimo vantaggio')
            va = input
        info_personaggio.update({'vantaggi':vantaggi})
            
        
        #punrti eore 1 di default
        info_personaggio.update({'punti eroe':1})
        #corruzzione 0 di default
        info_personaggio.update({'corruzzione':0})
        #ricchezza un numero intero positivo
        print('\ninserisci la ricchezza del personaggio')
        ricchezza = input()
        while int(ricchezza) < 0:
            print('\nla ricchezza deve essere almeno 0 ')
            ricchezza = input()
        info_personaggio.update({'ricchezza':int(ricchezza)})
        #storia un eroe deve obbligatoriamente avere una storia personale e inoltre devo inserirlo nelle storie del gm
        titolo = inserimento_storie(info_personaggio['nome'],info_personaggio['campagna'])
        info_personaggio.update({'storie'})
        for element in nomi_storie:
            protagonisti = storia[element]['protagonista']  #quando ho definito l'array storie ho anche tirato fuori tutte le storie del gm che ho chiamato storia
            protagonisti.append(info_personaggio['nome'])
            storie.update_one({{'titolo':element},{'$set':{'protagonista':protagonisti}}})

    else:#obbligatori per malvagi o png
        #forza un intero positivo
        print('\ninserisci la forza del personaggio')
        forza = input()
        while int(forza) < 1:
            print('\nla forza deve essere almeno 1 ')
            forza = input()
        info_personaggio.update({'forza':int(forza)})
        #influenza: identico a forza
        print('\ninserisci la influenza del personaggio')
        influenza = input()
        while int(influenza) < 1:
            print('\nla influenza deve essere almeno 1 ')
            influenza = input()
        info_personaggio.update({'influenza':int(influenza)})
    
    #adesso inserisco i campi facoòtativi
    #ruolo, se si vuole inserire il ruolo allora si dovra anche specificare una nave
    print('\n se non vuoi inserire un ruolo scrivi no. altrimenti metti uno tra: ',ruoli)
    ruolo = input()
    if ruolo != 'no':
        while ruolo not in ruoli:
            print('\nil ruolo inserito non esiste ')
            ruolo = input()
        info_personaggio.update({'ruolo':ruolo})
        nomi_navi = campagne.find({'nome':info_personaggio['campagna']})
        nomi_navi = nomi_navi['navi']
        print('\n digita #nuovo# se devi inserire una nave dove lavora il personaggio, se no inserisci il nome di una nave esistente tra: ',nomi_navi)
        na = input()
        if na == 'nuovo':
            na = inserimento_navi([info_personaggio['ruolo'],info_personaggio['nome'],info_personaggio['campagna']])
        else:
            while na not in nomi_navi:
                print('\nnave non esistente ')
                na = input()
        info_personaggio.update({'nave':na})
    #affiliazione
    print('\ninserisci le affiliazioni. di chi è al servizio il personaggio, se non vuoi inserire nessunodigita no, quando vuoi semettere di inserire digita stop.')
    aff = input()
    affiliazioni = []
    if aff != 'no':
        while aff != 'stop':
            while aff not in affiliazioni :
                print('\naffiliazione inserita sbagliata')
                aff = input()
            affiliazioni.append(aff)
            print('\ninserisci affiliazione: ')
            aff = input()
        info_personaggio.update({'affiliazioni':affiliazioni})
    personaggi.inserti_one(info_personaggio)
    #infine inserisco il personaggio nella campagna
    personaggi_camp.append(info_personaggio['nome'])
    campagne.update_one({{'nome':campagna},{'$set':{'personaggi':personaggi_camp}}})

def inserimento_navi(info_danave):
    navi = seventh_sea.navi
    campagne = seventh_sea.campagne
    linee_guida = seventh_sea.linee_guida
    personaggi = seventh_sea.personaggi
    #campagna
    campagna = campagne.find({})
    nomi_campagne = []
    for element in campagna:
        nomi_campagne.append(campagna[element]['nome'])
    #origini
    nomi_nazioni = linee_guida.find({'nome':'nazioni'})
    nomi_nazioni = nomi_nazioni['nomi']
    #leggende
    leggende = ['oltre orizzente','attraverso lo specchio','catturata dai pirati','amica di iskandar','capitano eroico','cacciatrice di pirati','battaglia famosa','doppiato il corno','ingoiata dal triangolo']
    #avventure
    avventure = ['una jenny in ogni porto','una vita breve e felice','avventuriera','trascinateli verso il loro destino','riempire la nave di spettri','lo oro fa sognare un uomo','alla inseguimento','quanto a lungo puoi trattenere il fiato?','oltre la mappa','salvato dagli abissi','licenza','sfidare il fato','grazie per lo aiuto','lo unico pirata buono','mi scusi principessa','la x indica il punto','o lo oro o la vita']
    ruoli = ['comandante','nostromo','cannoniere','medico di bordo','cadetto','marinaio di lungo corso','marinaio scelto','marinaio semplice','nulla']
    info_nave = {}

    #se info nave passato è none allora sto inserendo una nave da sola. se non è cosi allora significa che l'inserimento di una nave è legato ad un personaggio quindi alcuni elementi sono 'fissati'
    if info_danave is None:
        print('\ninserisci una campagna tra: ',nomi_campagne)
        campagna = input()
        while campagna not in nomi_campagne:
            print('\ninput errato, inserisci di nuovo ')
            campagna = input()
    else:
        campagna = info_danave[2]
    #inserisco il nome che non può essere duplicato
    nave = navi.find({})                
    nome_navi = []              
    for element in nave:
        nome_navi.append(nave[element]['nome'])
    print('\ninserisci il nome: ')
    nome = input()
    while nome in nome_navi:
        print('\nnave gia esistente, riinserire: ')
        nome = input()
    #voglio inserire prima il nome poi la campagna. quindi lo faccio qua
    info_nave.update({'nome':nome})
    info_nave.update({'campagna':campagna})
    #origini
    print('\ninserisci una origine tra: ',nomi_nazioni)
    origini = input()
    while origini not in nomi_nazioni:
        print('\ninput errato, inserisci di nuovo ')
        origini = input()
    info_nave.update({'origini':origini})
    #leggende
    leggen = []
    print('\ndigita no se non vuoi inserire leggende o quando hai finito di inserirne. metti una o più tra: ',leggende)
    legg = input()
    while legg != 'no':
        while legg not in leggende:
            print('\nla leggenda inserita non esiste ')
            legg = input()
        leggen.append(legg)
        print('\ninserisci la prossima leggenda: ')
        legg = input()
    info_nave.update({'leggende':leggen})
    #avventure
    avven = []
    print('\ndigita no se non vuoi inserire leggende o quando hai finito di inserirne. metti una o più tra: ',avventure)
    avv = input()
    while avv != 'no':
        while avv not in avventure:
            print('\nla avventura inserita non esiste ')
            avv = input()
        avven.append(avv)
        print('\ninserisci la prossima avventura: ')
        avv = input()
    info_nave.update({'avventure':avven})    
    #equipaggio
    equipaggio = {}
    for element in ruoli:
        print('\ninserisci la numerosità di ',element,' : ')
        num = input()
        while num < 0:
            print('\nnon si può avere una numerosità negativa: ')
            num = input
        equipaggio.update({element:num})
    #se la nave viene inserita perche collegata ad un personaggio controllo che ilsuo ruolo non sia 0. se lo è lo metto a 1
    if info_danave is not None:
        if equipaggio[info_danave[0]] == 0:
            equipaggio[info_danave[0]] == 1
    #personaggi collegati alla nave
    if info_danave is None:
        #trovo i personaggi
        pers = personaggi.find({'campagna':campagna})                
        nome_personaggi = []              
        for element in pers:
            nome_personaggi.append(pers[element]['nome'])
        personaggi = []
        print('\ndigita no se non vuoi inserire personaggi collegati o quando hai finito di inserirne. metti uno o più tra: ',nome_personaggi)
        per = input()
        while per != 'no':
            while per not in avventure:
                print('\nil personaggio inserito non esiste ')
                per = input()
            personaggi.append(per)
            print('\ninserisci il prossimo personaggio: ')
            per = input()
        info_nave.update({'personaggi':personaggi}) 
    else:
        info_nave.update({'personaggi':[info_danave[1]]})
   
    #inserisco
    navi.insert_one(info_nave)
    #infine inserisco la nave nella campagna
    navi_camp = campagne.find({'nome':info_nave['campagna']})
    navi_camp = navi_camp['navi']
    navi_camp.append(info_nave['nome'])
    campagne.update_one({{'nome':campagna},{'$set':{'navi':navi_camp}}})

    return(info_nave['nome'])

def inserimento_storie(info_dastoria):
    storie = seventh_sea.storie
    campagne = seventh_sea.campagne
    personaggi = seventh_sea.personaggi
    info_storia ={}
    if info_dastoria is None:
        #nomi delle campagna
        campagna = campagne.find({})
        nomi_campagne = []
        for element in campagna:
            nomi_campagne.append(campagna[element]['nome'])
        #inserisco la campagna
        print('\ninserisci una campagna tra: ',nomi_campagne)
        campagna = input()
        while campagna not in nomi_campagne:
            print('\ninput errato, inserisci di nuovo ')
            campagna = input()
    else:
        campagna = info_dastoria[1]
    #inserisco il titolo che non può essere duplicato
    sto = sto.find({})                
    storie_correnti = []              
    for element in sto:
        storie_correnti.append(sto[element]['titolo'])
    print('\ninserisci il titolo: ')
    titolo = input()
    while titolo in storie_correnti:
        print('\nstoria gia esistente, cambia: ')
        titolo = input()
    #ora inserisco in ordine titolo e campagna
    info_storia.update({'titolo':titolo})
    info_storia.update({'campagna':campagna})
    #tipo
    if info_dastoria is None:
        print('\ninserisci il tipo. uno tra GM, Eroe, Macchinazione')
        tipo = input()
        while tipo not in ['Eroe','GM','Macchinazione']:
            print('\ntipo errato: ')
            tipo = input()
         
    else:
        tipo = 'Eroe'
    info_storia.update({'tipo':tipo})
    #scopo
    print('\ninserisci lo scopo: ')
    scopo = input()
    info_storia.update({'scopo':scopo})
    #atti
    atti = []
    print('\ninserisci uno o più atti, digita stop qunado vuoi fermarti')
    while len(atti) == 0:
        print('\ndevi inserire almeno un atto')
        atto = input()
        while atto != 'stop':
            print('\ninserisci atto  ')
            atto = input()
        atti.append(atto)
    info_storia.update({'atti':atti})
    #protagonisti
    if info_dastoria is None:
        #se la storia è di un eroe posso inserire come protagonista solo quell'eroe
        if info_storia['tipo'] == 'Eroe':
            #ricavo i nomi degli eroi
            eroi = personaggi.find({'campagna':info_storia['campagna']},{'tipo':'Eroe'})
            nomi_eroi = []
            for element in eroi:
                nomi_eroi.append(element['nome'])
            #inserisco un nome di un eroe
            print('\ninserisci un eroe tra: ',nomi_eroi)
            eroe = input()
            while eroe not in nomi_eroi:
                print(eroe, 'non è un eroe: ')
                eroe = input()
            info_storia.update({'protagonista':[eroe]})
        #se la storia è una macchinazione posso inserire solo malvagi
        if info_storia['tipo'] == 'Macchinazione':
            #ricavo i nomi dei malvagi
            malvagi = personaggi.find({'campagna':info_storia['campagna']},{'tipo':'Malvagio'})
            nomi_malvagi = []
            for element in malvagi:
                nomi_malvagi.append(element['nome'])
            #inserisco un nome di un eroe
            print('\ninserisci un malvagio tra: ',nomi_malvagi)
            malvagio = input()
            while malvagio not in nomi_malvagi:
                print('\n',malvagio, 'non è un malvagio: ')
                malvagio = input()
            info_storia.update({'protagonista':[malvagio]})
        #se la storia è del gm inserisco tutti gli eroi tra i protagonisti
        if info_storia['tipo'] == 'GM':
            eroi = personaggi.find({'campagna':info_storia['campagna']},{'tipo':'Eroe'})
            nomi_eroi = []
            for element in eroi:
                nomi_eroi.append(element['nome'])
            info_storia.update({'protagonista':nomi_eroi})
    else:#l'inserimento della storia è stato chiamato alla fine dell'inserimento di un personaggio
        info_storia.update({'protagonista':info_dastoria[0]})
    #una volta inseriti i protagonisti inserisco il titolo della storia tra i titoli dele storie di cui fa parte il personaggio
    for element in info_storia['protagonista']:
        sto_pers = personaggi.find({'nome':element})
        sto_pers = sto_pers['storie']
        sto_pers.append(info_storia['titolo'])
        personaggi.update_one({'nome':element},{'$set':{'storie':sto_pers}})
    #infine la ricompensa. parte più lunga perchè sottosta ad una marea di regole
    #innanzitutto si dividono le ricompense tra eroi e malvagi/png
    ricompense = []
    for element in info_storia['protagonista']:
        if info_storia['tipo'] in ['Eroe','GM']:
            #se uno sbaglia gli do la possibilità di reinserire la ricompensa  
            for element in info_storia['protagonista']:
                err = True
                while err:
                    tipi_ricompense = ['abilità', 'vantaggio','background','hubris','virtu','tratto','corruzzione']
                    print('\ninserisci il tipo di ricompensa. uno tra: ', tipi_ricompense)
                    tipo_ri = input
                    while tipo_ri not in tipi_ricompense:
                        print('\ninserisci una ricompensa valida')
                        tipo_ri = input
                    #abilità
                    if tipo_ri == 'abilità':
                        abilità = ['allettare','a.d.guerra','atletica','cavalcare','convincere','empatia','esibirsi','furto','intimidire','istruzione','mira','mischia','nascondersi','navigazione','notare','rissa']
                        print('\n\inserisci una abilità')
                        abi = input()
                        while abi not in abilità:
                            print('\nricompensa sbagliata ')
                            abi = input()
                        if len(info_storia[atti]) > (5): #se il grdo della ricompensa non supera il 5 allora metto quello se no metto il grado massimo. cioè 5
                            ricompense.append([abi,len(info_storia[atti])])
                        else: 
                            ricompense.append([abi,5])
                        err = False
                    #tratti
                    if tipo_ri == 'tratto':
                        tratti = ['vigore','grazia','risolutezza','acume','panache']
                        print('\ninserisci un tratto')
                        tratt = input()
                        #se il tratto è gia massimo faccio scegliere un'altro tratto
                        flag = True
                        while flag:
                            while tratt not in tratti:
                                print('\nricompensa sbagliata ')
                                abi = input()
                            grado = personaggio.find({'nome':element})
                            grado = grado['tratti'][tratt]
                            if len(info_storia['atti']) < 5:
                                print('ricompensa errata ')
                            elif grado+1 <= 5 : #un tratto non può essere aumentato oltre i 5
                                ricompense.append([tratt,grado+1])
                                flag = False
                            else: 
                                print('\ntratto maxato. scegline un altro')
                        err = False
                    #hubris
                    if tipo_ri == 'hubris':
                        nomi_hubris = linee_guida.find({'nome':'hubris'})
                        nomi_hubris = nomi_hubris['nomi']
                        print('\ninserisci la hubris sostitutiva')
                        hu = input() 
                        if len(info_storia['atti']) >= 4:
                            while hu not in nomi_hubris:
                                print('\ninserisci una hubris esistente')
                                hu = input()
                            ricompense.append([hu])
                            err = False
                        else:
                            print('\nricompensa non valida')
                    #virtu
                    if tipo_ri == 'virtu':
                        nomi_virtu = linee_guida.find({'nome':'virtu'})
                        nomi_virtu = nomi_virtu['nomi']
                        print('\ninserisci la virtu sostitutiva')
                        vi = input() 
                        if len(info_storia['atti']) >= 4:
                            while vi not in nomi_virtu:
                                print('\ninserisci una virtu esistente')
                                vi = input()
                            ricompense.append([vi])
                            err = False
                        else:
                            print('\nricompensa non valida')
                    #background
                    if tipo_ri == 'background':
                        nomi_background = linee_guida.find({'nome':'bsckground'})
                        nomi_background = nomi_background['nomi']
                        print('\ninserisci il background sostitutivo')
                        ba = input() 
                        if len(info_storia['atti']) >= 3:
                            while ba not in nomi_background:
                                print('\ninserisci un background esistente')
                                ba = input()
                            ricompense.append([ba])
                            err = False
                        else:
                            print('\nricompensa non valida')

                    #vantaggio
                    if tipo_ri == 'vantaggio':
                        nomi_vantaggi = linee_guida.find({'nome':'vantaggi'})
                        costi = nomi_vantaggi['costo']
                        nomi_vantaggi = nomi_vantaggi['nomi']
                        print('\ninserisci il vantaggio aggiuntivo')
                        va = input() 
                        while va not in nomi_virtu:
                            print('\ninserisci un vantaggio esistente')
                            va = input()
                        #ricavo il costo del vantagggio
                        p = nomi_vantaggi.index(va)
                        if len(info_storia['atti']) == costi[p]:
                            ricompense.append([va])
                            err = False
                        else:
                            print('\nricompensa non valida')
            
                    #corruzione: rimuovere 1 punto corruzionerichiede 5 atti
                    if tipo_ri == 'corruzione' and len(info_storia['atti']) >= 5:
                        ricompense.append(['corruzione',-int(len(info_storia['atti'])/5)])
                        err = False
            else:
                tipi_ri = ['forza','influenza']
                for element in tipi_ri:
                    print('\ninserisci un numero di aumento per ',element)
                    num = input()
                    while not num.isnumeric():
                        print('\nerrato. inserisci un numero')
                        num = input()
                    ricompense.append([element,int(num)])
    #una volta inserita una ricompensa conforme alle regole
    info_storia.update({'ricompensa':ricompense})
    storie.insert_one(info_storia)
    #infine inserisco la stori nella campagna
    storie_camp = campagne.find({'nome':info_storia['campagna']})
    storie_camp = storie_camp['storie']
    storie_camp.append(info_storia['titolo'])
    campagne.update_one({{'nome':campagna},{'$set':{'storie':storie_camp}}})

    return(info_storia['titolo'])
                            
def inserimento_campagne():
    campagne = seventh_sea.campagne  
    #inserisco solo il nome e i punti pericolo. storie, navi e personaggi si inseriscono automaticamente
    info_campagna = {}
    print('\ninserisci il nome della campagna: ') 
    nome = input()    
    info_campagna.update({'nome':nome})
    #li inizzializzo comunque come stringhe vuote
    personaggi = []
    navi = []
    storie = []
    info_campagna.update({'personaggi':personaggi})
    info_campagna.update({'navi':navi})
    info_campagna.update({'storie':storie})
    #i punti pericolo sono 0 di default
    info_campagna.update({'punti pericolo':0})
    campagne.insert_one(info_campagna)

##funzioni modifica dati##
def modifica_campagna():
    campagne = seventh_sea.campagne
    campagna = campagne.find({})
    nomi_campagne = []
    for element in campagna:
        nomi_campagne.append(campagna[element]['nome'])
    print('\ninserisci una campagna tra: ',nomi_campagne)
    camp = input()
    while camp not in nomi_campagne:
        print('\ninserisci una campagna esistente')
        camp = input
    print('\ninserisci il nuovo numero di punti pericolo: ')
    num = input
    while not num.isnumeric() and int(num) < 0:
        print('\nerrato. inserisci un numero')
        num = input()

def modifica_storie():
    storie = seventh_sea.storie
    s = storie.find({})
    titoli = []
    for element in s:
        titoli.append(element['titolo'])
    print('inserisci il titolo della storia da cambiare')
    titolo = input()
    while titolo not in titoli:
        print('inserisci il titolo di una storia esistente ')
        titolo = input()
    print('\ncosa vuoi modificare. atto, scopo')
    modifica = input()
    while modifica not in ['atto,scopo']:
        print('errore inserisci la modifica giusta: ')
        modifica = input()
    if modifica == 'scopo':
        print('\ninserisci lo scopo: ')
        new_scopo = input()
        storie.update_one({{'titolo':titolo},{'$set':{'scopo':new_scopo}}})
    #faccio reinserire tutti gli atti come punizione
    if modifica == 'atto':
        # il numero di atti pero non può essere minore a quello precedente
        new_atti = []
        atti = storie.find({'titolo':titolo})
        atti = atti['atti']
        print('\ninserisci uno o più atti, digita stop qunado vuoi fermarti')
        while len(new_atti) < len(atti):
            print('\ndevi inserire un numero di atti almeno pari al precedente')
            atto = input()
            while atto != 'stop':
                print('\ninserisci atto  ')
                atto = input()
            new_atti.append(atto)
        storie.update_one({{'titolo':titolo},{'$set':{'atti':new_atti}}})

def modifica_nave(info_modifica):
    navi = seventh_sea.navi
    if modifica is None:# modifico la nave senza che questa modifica sia dovuta alla modifica di un personaggio
        n = navi.find({})
        nomi = []
        for element in n:
            nomi.append(element['nome'])
        print('inserisci il nome della nave da modificare')
        nome = input()
        while nome not in nomi:
            print('inserisci il nome di una nave esistente: ')
            nome = input()
        print('\ncosa vuoi modificare. avventure, leggende, equipaggio')
        modifica = input()
        while modifica not in ['avventure, leggende, equipaggio']:
            print('errore inserisci la modifica giusta: ')
            modifica = input()
        # le avventure possono solo essere aggiunte
        if modifica == 'avventure':    
            avventure = ['una jenny in ogni porto','una vita breve e felice','avventuriera','trascinateli verso il loro destino','riempire la nave di spettri','lo oro fa sognare un uomo','alla inseguimento','quanto a lungo puoi trattenere il fiato?','oltre la mappa','salvato dagli abissi','licenza','sfidare il fato','grazie per lo aiuto','lo unico pirata buono','mi scusi principessa','la x indica il punto','o lo oro o la vita']
            new_avv = []
            print('\ninserisci uno o più avventure, digita stop qunado vuoi fermarti')
            avv = input()
            while avv != 'stop':
                while avv not in avventure:
                    print('inserisci una avventura esistente: ')
                    avv = input()
                new_avv.append(avv)
            avv_nave = navi.find({'nome':nome})
            avv_nave = avv_nave['avventure']
            avv_nave.extend(new_avv)
            navi.update_one({{'nome':nome},{'$set':{'avventure':avv_nave}}})
        #le leggende possono solo essere aggiunte
        if modifica == 'leggende':
            leggende = ['oltre orizzente','attraverso lo specchio','catturata dai pirati','amica di iskandar','capitano eroico','cacciatrice di pirati','battaglia famosa','doppiato il corno','ingoiata dal triangolo']
            new_legg = []
            print('\ninserisci uno o più leggende, digita stop qunado vuoi fermarti')
            legg = input()
            while legg != 'stop':
                while legg not in leggende:
                    print('inserisci una leggenda esistente: ')
                    legg = input()
                new_legg.append(legg)
            legg_nave = navi.find({'nome':nome})
            legg_nave = legg_nave['leggende']
            legg_nave.extend(new_legg)
            navi.update_one({{'nome':nome},{'$set':{'leggende':legg_nave}}})
        #i ruoli possono essere modificati a piacimento fin che non vanno sotto 0
            if modifica == 'ruolo':
                ruoli = ['comandante','nostromo','cannoniere','medico di bordo','cadetto','marinaio di lungo corso','marinaio scelto','marinaio semplice','nulla']
                new_role = navi.find({'nome':nome})
                new_role = new_role['composizione_equipaggio']
                print('\ninserisci uno o più ruoli, digita stop qunado vuoi fermarti')
                role = input()
                while role != 'stop':
                    while role not in ruoli:
                        print('inserisci un ruolo esistente: ')
                        legg = input()
                    val = -1
                    while int(val) < 0 and val.isnumeric():
                        print('inserisci il nuovo numero di membri del ruolo')
                        val = input()
                    new_role[role] = val
                navi.update_one({{'nome':nome},{'$set':{'composizione_equipaggio': new_role}}})
    #se cambio di ruolo un personaggio o questo se na va dalla nave devo rimuovere i suo ruolo e il personaggio dalla lista di collegamenti
    #se il personaggio cambia ruolo devo poi aggiungere il nuovo ruolo alla nave e aggiungere il personaggio alla lista di collegamenti
    elif info_modifica[2] == 1: #il personaggio arriva in una nave
        new_role = navi.find({'nome':info_modifica[0]})
        new_role = new_role['composizione_equipaggio']
        new_role[info_modifica[1]] = new_role[info_modifica[1]]+1
        pers = navi.find({'nome':info_modifica[0]})
        pers = pers['personaggi']
        navi.update_one({'nome':info_modifica[0]},{'$set':{'composizione_equipaggio': new_role}})
        navi.update_one({'nome':info_modifica[0]},{'$set':{'personaggi':pers.append(info_modifica[3])}})
    elif info_modifica[2] == -1: #un personaggio va via da una nave
        new_role = navi.find({'nome':info_modifica[0]})
        new_role = new_role['composizione_equipaggio']
        new_role[info_modifica[1]] = new_role[info_modifica[1]]-1
        pers = navi.find({'nome':info_modifica[0]})
        pers = pers['personaggi']
        navi.update_one({{'nome':info_modifica[0]},{'$set':{'composizione_equipaggio': new_role}}})
        navi.update_one({'nome':info_modifica[0]},{'$set':{'personaggi':pers.remove(info_modifica[3])}})

def modifica_personaggio():
    personaggi = seventh_sea.personaggi
    navi = seventh_sea.navi
    p = personaggi.find({})
    nomi = []
    for element in p:
        nomi.append(element['nome'])
    print('inserisci il nome del personaggio da modificare')
    nome = input()
    while nome not in p:
        print('inserisci il nome di un personaggio esistente: ')
        nome = input()
    print('\ncosa vuoi modificare. fama,fede,ricchezza,ruolo,nave,descrizione,affiliazione','corruzione')
    modifica = input()
    while modifica not in ['fama,fede,ricchezza,ruolo,descrizione,affiliazione','corruzione']:
        print('errore inserisci la modifica giusta: ')
        modifica = input()
    #la corruzione è+ sempre un aumento di 1
    if modifica == 'corruzione':
        cor = personaggi.find({'nome'})
        cor = cor['corruzione']
        cor = cor+1
        personaggi.update_one({'nome':nome},{'$set':{'corruzione':cor}})
    #la fama comporta l'aggiunta di titoli
    if modifica == 'fama':
        print('\ninserisci i titoli con cui è conosciuto. quando vuoi fermarti inserisci stop: ')
        ins = input()
        new_fama = []
        while ins != 'stop':
            new_fama.append(ins)
            print('\n')
            ins = input()
        fama = personaggi.find({'nome':nome})
        fama = fama['fama']
        fama.extend(new_fama)
        personaggi.update_one({{'nome':nome},{'$set':{'fama':fama}}})
    #la fede puo solo essere rimpiazzata
    if modifica == 'fede':
        fedi = ['Druidismo','Vaticino', 'Chiesa di Avalon', 'Obiezionismo', 'pagana Inish', 'pagana Highland', 'Ateo', 'pagana Rzeczpospolitana', 'pagana Curoniana', 'Chiesa Ortodossa Ussurana', 'pagana Ussurana', 'pagana Vesten']
        print('\ninserisci una fede tra: ',fedi)
        fede = input()
        while fede not in fedi:
            print('input errato, inserisci di nuovo ')
            fede = input()
        personaggi.update_one({{'nome':nome},{'$set':{'fede':fede}}})
    #ricchezza può essere guadagnata o persa
    if modifica == 'ricchezza':
        print('\ninserisci nuova la ricchezza del personaggio')
        ricchezza = input()
        while int(ricchezza) < 0:
            print('\nla ricchezza deve essere almeno 0 ')
            ricchezza = input()
        personaggi.update_one({'nome':nome},{'$set':{'ricchezza':ricchezza}})
    #ruolo
    if modifica == 'ruolo':
        ruoli = ['comandante','nostromo','cannoniere','medico di bordo','cadetto','marinaio di lungo corso','marinaio scelto','marinaio semplice','nulla']
        print('inserisci il nuovo ruolo: ')
        new_ruolo = input()
        while new_ruolo not in ruoli:
            print('inserisci un ruolo esistente')
            new_ruolo = input()
        vecchio_ruolo = personaggi.find({'nome':nome})
        vecchio_ruolo = vecchio_ruolo['ruolo']
        #modifico la nave
        nave = personaggi.find({'nome':nome})
        nave = nave['navi']
        modifica_nave([nave,vecchio_ruolo,-1,nome])# rimuovo il ruolo vecchio dalla nave
        modifica_nave([nave,new_ruolo,1,nome])#aggiungo il ruolo nuovo sulla nave
        personaggi.update_one({'nome':nome},{'$set':{'ruolo':new_ruolo}})
    #nave
    if modifica == 'nave':
        try:
            t = personaggi.find({'nome':nome})
            t = t['nave']
            print('vuoi abbandonare la nave o cambiare: ')
            decisione = input()
            while decisione not in ['abbandonare','cambiare']:
                print('inserisci abbandonare o cambiare. ')
                decisione = input()
            if decisione == 'abbandonare':
                nave = personaggi.find({'nome':nome})
                nave = nave['navi']
                ru = personaggi.find({'nome':nome})
                ru = ru['ruolo']
                modifica_nave([nave,ru,-1,nome])
                personaggi.update_one({'nome':nome},{'$unset':{'nave':1}})
                personaggi.update_one({'nome':nome},{'$unset':{'ruolo':1}})
            if decisione == 'cambiare':
                nave = personaggi.find({'nome':nome})
                nave = nave['navi']
                ru = personaggi.find({'nome':nome})
                ru = ru['ruolo']
                modifica_nave([nave,ru,-1,nome])#nave da cui va via
                print('inserisci il nome di una nave esistente')
                nave = input()
                while len(navi.find({'nome':nave})) == 0:
                    print('inserisci il nome di una nave esistente: ')
                    nave = input()
                modifica_nave([nave,ru,1,nome])#nave a cui arriva
                personaggi.update_one({'nome':nome},{'$set':{'nave':nave}})
        except:# il personaggio non ha nessuna nave
            n = navi.find({})
            nomi = []
            for element in n:
                nomi.append(element['nome'])
            print('inserisci il nome di una nave esistente')
            nave = input()
            while nave not in nomi:
                print('inserisci il nome di una nave esistente: ')
                nave = input()
            ruoli = ['comandante','nostromo','cannoniere','medico di bordo','cadetto','marinaio di lungo corso','marinaio scelto','marinaio semplice','nulla']
            print('inserisci il ruolo: ')
            ruolo = input()
            while ruolo not in ruoli:
                print('inserisci un ruolo esistente')
                ruolo = input()
            modifica_nave([nave,ruolo,1,nome])
            #ricavo il personaggio e ci aggiungo nave e ruolo
            pers = personaggi.find({'nome':nome})
            pers.update({'$set':{'nave':nave,'ruolo':ruolo}})
            #lo elimino ed inserisco la versione modificats
            personaggi.remove({'nome':nome})
            personaggi.insert_one(pers)
    #descrizione la sovrascrivo
    if modifica == 'descrizione':
        print('\ninserisci una desrizione: ')
        descrizione = input()
        personaggi.update_one({'nome':nome},{'$set':{'descrizione':descrizione}})
    #affiliazione
    if modifica == 'affiliazione':
        ca = personaggi.find({'nome':nome})
        ca = ca['campagna']
        personaggi_camp = campagne.find({'nome':ca})
        personaggi_camp = personaggi_camp['personaggi']
        nomi_socseg = linee_guida.find({'nome':'società segrete'})
        nomi_socseg = nomi_socseg['nomi']
        aff = personaggi_camp.extend(nomi_socseg)
        print('inserisci una affiliazione tra: ',aff)
        a = input()
        while a not in aff:
            print('affiliazione sbagliata')
            a = input()
        print('vuoi aggiungere o rimuovere la affiliazione')
        mod = input()
        while mod not in ['rimuovere','aggiungere']:
            print('sbagliato')
            mod = input()
        #rimozione
        if mod == 'rmuovere':
            pe = personaggi.find({'nome':nome})
            pe = pe['affiliazioni']
            pe.remove(a)
            personaggi.update_one({'nome':nome},{'$set':{'affiliazioni':pe}})
        #aggiunta
        if mod == 'aggiungere':
            pe = personaggi.find({'nome':nome})
            pe = pe['affiliazioni']
            pe.append(a)
            personaggi.update_one({'nome':nome},{'$set':{'affiliazioni':pe}})

def completamento_storia():
    storie = seventh_sea.storie
    linee_guida = seventh_sea.linee_guida
    personaggi = seventh_sea.personaggi
    #le possibili liste di controllo delle ricompense
    tratti = ['vigore','grazia','risolutezza','acume','panache']
        #abilità
    abilità = ['allettare','a.d.guerra','atletica','cavalcare','convincere','empatia','esibirsi','furto','intimidire','istruzione','mira','mischia','nascondersi','navigazione','notare','rissa']
        #vantaggi
    nomi_vantaggi = linee_guida.find({'nome':'vantaggi'})
    nomi_vantaggi = nomi_vantaggi['nomi']
        #hubris
    nomi_hubris = linee_guida.find({'nome':'hubris'})
    nomi_hubris = nomi_hubris['nomi']
        #virtù
    nomi_virtu = linee_guida.find({'nome':'virtù'})
    nomi_virtu = nomi_virtu['nomi']
        #background
    nomi_background = linee_guida.find({'nome':'background'})
    nomi_background = nomi_background['nomi']
    #tiro fuori i nomi delle storie
    sto = sto.find({})                
    storie_correnti = []              
    for element in sto:
        storie_correnti.append(sto[element]['titolo'])
    print('\ninserisci il titolo: ')
    titolo = input()
    while titolo in storie_correnti:
        print('\ninserisci una storia esistente: ')
        titolo = input()
    storia_finita = storie.find({'titolo':titolo})
    protagonisti = storia_finita['protagonista']
    ricompense = storia_finita['ricompense']

    #assegno la ricompensa ad ogni protagonista
    i = 0
    for element in protagonisti:
        #tiro fuori il dizionario dei tratti modifico solo quello che mi interessa
        if ricompense[i][0] in tratti:
            tratti_pers = personaggi.find({'nome':element})
            tratti_pers = tratti_pers['tratti']
            tratti_pers[ricompense[i][0]] = ricompense[i][1]
            personaggi.update_one({'nome':element},{'$set':{'tratti':tratti_pers}})
        #tiro fuori il dizionario delle abilità e modifico solo quella che mi interessa
        if ricompense[i][0] in abilità:
            abilità_pers = personaggi.find({'nome':element})
            abilità_pers = abilità_pers['abilita']
            abilità_pers[ricompense[i][0]] = ricompense[i][1]
            personaggi.update_one({'nome':element},{'$set':{'abilita':abilità_pers}})
        #aggiungo il vantaggio alla lista dei vantaggi
        if ricompense[i][0] in nomi_vantaggi:
            vantaggi_pers = personaggi.find({'nome':element})
            vantaggi_pers = vantaggi_pers['vantaggi']
            vantaggi_pers.append(ricompense[i][0])
            personaggi.update_one({'nome':element},{'$set':{'vantaggi':vantaggi_pers}})
        #cambio l'arcano corrispondente
        if ricompense[i][0] in nomi_hubris:
            personaggi.update_one({'nome':element},{'$set':{'hubris':ricompense[i][0]}})
        if ricompense[i][0] in nomi_virtu:
            personaggi.update_one({'nome':element},{'$set':{'virtu':ricompense[i][0]}})
        #il background che verra rimosso sarà il primo che è stato inserito
        if ricompense[i][0] in nomi_background:
            back_pers = personaggi.find({'nome':element})
            back_pers = back_pers['vantaggi']
            back_pers.append(ricompense[i][0])
            back_pers = back_pers[1:]
            personaggi.update_one({'nome':element},{'$set':{'background':back_pers}})
        #forza, nfluenza, corruzione basta sommare il valore della ricompensa a quello gia esistente
        if ricompense[i][0] in ['forza','influenza','corruzione']:
            pers = personaggi.find({'nome':element})
            c = pers[ricompense[i][0]]
            c = c+ricompense[i][1]
            personaggi.update_one({'nome':element},{'$set':{ricompense[i][0]:c}})
        i = i+1

##funzioni generali##
def inserimento(): #cosa mi dice se voglio inserire una campagna, personaggio,storia,nave
    continua = 'si'
    while(continua == 'si'):
        print('puoi inserire solo uno tra campagna','personaggio','nave','storia: ')
        cosa = input()

        while(cosa not in ['campagna','personaggio','nave','storia']):
            print('puoi inserire solo uno tra campagna','personaggio','nave','storia: ')
            cosa = input()
    
        if cosa == 'campagna':
            inserimento_campagne()
        
        if cosa == 'personaggio':
            inserimento_personaggio()
        
        if cosa == 'nave':
            c = inserimento_navi(None) #serve a dire che l'inserimento della nave non deriva dall'inserimento di un personaggio
        
        if cosa == 'storia':
            c = inserimento_storie(None) #serve a dire che l'inserimento della storia non deriva dall'inserimento di un personaggio
        
def modifica():
    continua = 'si'
    while(continua == 'si'):
        print('puoi modificare solo uno tra campagna, personaggio, nave, storia: ')
        cosa = input()

        while(cosa not in ['campagna','personaggio','nave','storia']):
            print('puoi inserire solo uno tra campagna','personaggio','nave','storia: ')
            cosa = input()
    
        if cosa == 'campagna':
            modifica_campagna()
        
        if cosa == 'personaggio':
            modifica_personaggio()
        
        if cosa == 'nave':
            modifica_nave(None) #serve a dire che la modifica della nave non avviene perche sto modificando un personaggio
        
        if cosa == 'storia':
            modifica_storie() 

def ricerca():
    print()
    continua = 'si'
    while(continua == 'si'):
        print('puoi cercare tra campagna, personaggio, nave, storia, linee_guida: ')
        cosa = input()

        while(cosa not in ['campagna','personaggio','nave','storia','linee_guida']):
            print('puoi inserire solo uno tra campagna,personaggio,nave,storia, linee_guida: ')
            cosa = input()
    
        if cosa == 'campagna':
            print('inserisci un nome, per smettere di inserire inserisci stop')
            nome = input()
            nomi = []
            while nome != 'stop':
                nomi.append(nome)
                print('inserisci un nome, per smettere di inserire inserisci stop')
                nome = input()
            ricerca_campagna(nome)
        
        if cosa == 'personaggio':
            print('inserisci un nome, per smettere di inserire inserisci stop')
            nome = input()
            nomi = []
            while nome != 'stop':
                nomi.append(nome)
                print('inserisci un nome, per smettere di inserire inserisci stop')
                nome = input()
            ricerca_personaggio(nomi)
        
        if cosa == 'nave':
            print('inserisci un nome, per smettere di inserire inserisci stop')
            nome = input()
            nomi = []
            while nome != 'stop':
                nomi.append(nome)
                print('inserisci un nome, per smettere di inserire inserisci stop')
                nome = input()
            ricerca_navi(nomi) #serve a dire che la modifica della nave non avviene perche sto modificando un personaggio
        
        if cosa == 'storia':
            print('inserisci un nome, per smettere di inserire inserisci stop')
            nome = input()
            nomi = []
            while nome != 'stop':
                nomi.append(nome)
                print('inserisci un nome, per smettere di inserire inserisci stop')
                nome = input()
            ricerca_storie(nomi)    