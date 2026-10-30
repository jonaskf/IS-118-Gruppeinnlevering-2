#Beskrivelse av oppgaven
print ("Erling har to konflikter og må hjelpe teamet bevare motivasjonen. Dette skal du hjelpe ham med ved å ta flere valg som har ulike konsekvenser, og som vil føre til ulike endingspunkter.")


#Dette er hvor og hvordan konflikten mellom Elias og Silje skal løses. Jeg har valgt å gjøre det simpelt, med å bare ta i bruk print, input, elif, if, else slike oppgaven sier.
print ("Konflikt 1: Silje vs Elias: Det er uenighet om teknologivalg og design, Silje vil ha en løsning som gir bedre brukeropplevelse og gir henne mer frihet til innovasjon, men Elias mener dette er urealistisk og fokuserer på ressursbruk")
print ("løsning 1) Ta opp konflikten i plenum gjennom håndsopprekning")
print ("løsning 2) Ta opp konflikten i plenum, avgjørelsen tas ettersom hva gruppen setter mest pris på")
print ("løsning 3) Utfør individuelle samtaler med både Silje og Elias")

#gir input mulighet for å velge 1,2 eller 3, man kan velge mellom 3 valg og jeg bruker if, elif, og else for å gjøre at jeg kan få 3 mulige svar + sette inn else setning hvis man ikke svarer riktig i terminalen
valg1 = input ("velg løsning 1, 2 eller 3: ")

if valg1 == "1":
    print("Etter håndsopprekning vinner Elias, men silje føler seg ikke hørt og produkter blir dårligere")
    resultat1 ="dårlig"

elif valg1 == "2":
    print ("Både Elias og Silje får sin vilje og produktet blir produsert optimalt innen tidsfrist.")
    resultat1 = "bra"

elif valg1 == "3":
    print ("De individuelle samtalene senker konfliktens intensitet litt, men det blir dårligere kommunikasjon i etterkant.")
    resultat1 = "ok"
# Valgte å legge in en liten "warning" for hvis man ikke skriver tallene som korisponderer med koden. 
else:
    print ("ERROR IKKE PRØV DEG, DETTE ER SERIØST ERROR")
    exit()

#Her er delen med Hamdi og Hallgeir, det er det samme oppsettet som Elias og Silje

print ("Konflikt 2: Hamdi VS Hallgeir: De er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter, Hamdi ønsker en kontrolert løsning gjennom kommunsens eksisterende plattform, mens hallgeir ønsker et mer åpent, dialogbasert system med rom for spontane innspill")
print("Løsning 1) Felles møte der ideen med flest stemmer vinner")
print ("Løsning 2) Avvente og håpe på at konflikten mellom dem løses av seg selv")
print ("Løsning 3) Hente inn HR for å løse konflikten")

valg2 = input("Velg løsning 1, 2 eller 3: ")

if valg2 == "1":
    print ("Det blir avstemning og de kommer til en løsning, men taperen føler seg ikke satt pris på.")
    resultat2 = "ok"

elif valg2 == "2":
    print ("Konflikten eskalerer til en personkonflikt. Begge parter drar med seg andre inn i gruppa, og de klarer ikke å få produsert prototype i tide")
    resultat2 = "dårlig"

elif valg2 == "3":
    print ("HR hjelper gruppen frem til en felles enighet, og erling mister ingen tillit fra de andre gruppemedlemmene")
    resultat2 = "bra"
else:
    print ("ERROR IKKE PRØV DEG, DETTE ER SERIØST ERROR")
    exit()

#Teambuilding delen, samme oppsett som de to over fungerer likt
print ("Erling må holde oppe motivasjonen i gruppa etter at valgene for å løse konfliktene er tatt")
print ("Løsning 1) Implementere relasjonsbygging og sosiale aktiviteter")
print ("Løsning 2) Prioritere fremdrift og leveranse for å holde fokus på resultatet av prosjektet")

valg3 = input("Velg enten løsning 1, eller løsning 2: ")

if valg3 == "1":
    print ("Erling vektlegger relasjonsbygging og sosiale aktiviteter, det blir arrangert klarting og grilling for å øke moralen, men på bekostning av tid. Dette skaper sterkere relasjoner men de merker på at det blir spenning i teamer fordi de føler de mangler tid. ")
    resultat3 = "ok"
elif valg3 == "2":
    print ("Erling prioriteter fremdring og leveranse for å fokusere på resultat. Det blir gjennomført møter for å følge med på fremdrift, arbeidsoppgavene blir fordelt utfra kompetanse og prosjektet får økt produktivitet, ungår unødvendig diskusjoner, analyser og planlegging.")
    resultat3 = "bra"
else:
    print ("ERROR IKKE PRØV DEG, DETTE ER SERIØST ERROR")
    exit()

#konklusjonen av hele opplegget. gjorde slik at hvis du velger de to korrekte gode svarene så får du en god slutt, hvis du felger to dårlige får du en dårlig, og hvis du valgte noe i mellom fikk du en helt ok slutt, dvs hvis du velger en god men en dårlig, eller en ok og en god, en god og en og, osv.
print ("Nå som du har valgt noen svar så får dette noen konsekvenser")
if resultat1 == "bra" and resultat2 == "bra" and resultat3 == "bra":
    print ("DU HAR FÅTT DEN GODE SLUTTEN. Teamet klarer å løse konfliktene og de beveger seg til norming fasen")
elif resultat1 == "dårlig" and resultat2 == "dårlig":
    print ("DU HAR FÅTT DEN DÅRLIGE SLUTTEN. Teamet er utsatt for mange uenigheter og konflikter, teamer faller fra hverandre og de har ikke produsert prototypen til tide")
else:
    print("DU HAR FÅTT EN OK SLUTT. Konfliktene blir løst delvis, men det er fremdeles litt dårlig stemning mellom teammedlemmene.")



