#Variabler
poeng = 0

#Definisjoner
def fortsette():
    x = 1

    while x != "":
        x = input("\nTrykk på Enter for å fortsette: \n")
        if x == "":

            break
# Laget en funksjon som legger til en fortsette knapp for å dele opp historien mellom valg

def gyldig_svar(spørsmål, svar_alternativer):
    svar = int(input(spørsmål))

    while svar not in svar_alternativer:
     print ("\nJeg forsto ikke.")
     svar = int(input(spørsmål))

    return svar 
#Laget en funksjon for å velge svar, og for å se om svaret er gyldig. Den returnerer også svaret slik at verdien blir lagret og poengsummen kan regnes ut.

#Starten på spillet
print ("IS-118 Tekstspill\n")
print ("\nDu skal hjelpe Erling med tre situasjoner han står overnfor med teamet sitt."
       "\nDu kommer til å få noen valg som Erling må ta."
       "\nTil slutt får du en poengsum som forteller deg hvor bra du gjorde det!")

klar = input("Er du klar?: ").lower()
while klar != "ja" and klar != "nei":
    print ("Jeg forsto ikke")
    klar = input("Er du klar?: ").lower()

if klar == "nei":
    print ("Da får du komme tilbake senere.")
    exit()
    
elif klar == "ja":
    print ("\nSå bra, la oss starte.")

fortsette()

#Første spørsmål om Silje og Elias
svar1 = gyldig_svar("\nDette er den første utfordringen til Erling..."
                    "\nSilje og Elias er i en personkonflikt angående program og UX-design."
                    "\nErling kan:"
                    "\n1.Ta det opp i plenum."
                    "\n2.Erling kan håndtere det selv med individuelle samtaler med Silje og Elias.\n"
                    "\nHva velger du?"
                    "\nTrykk på 1 eller 2 for å velge tilsvarende løsning: ",
                    [1,2])

#Andre spørsmål dersom plenum ble valgt
if svar1 == 1:
    svar2 = gyldig_svar("\nErling tar saken opp i plenum."
                        "\nDu får nå to nye valg:"
                        "\n1.Velge ut fra håndsopprekning."
                        "\n2.Velge ut fra hva folk setter størst pris på."
                        "\nTrykk på 1 eller 2 for å velge tilsvarende løsning: ", 
                        [1,2])

    
#Dersom håndsopprekning ble valgt
    if svar2  == 1:
        print("\nEtter håndsopprekningen vinner Elias sin idé,"
              "\nsiden de fleste i gruppen var enige i at selve programmet var viktigere enn UX-designet."
              "\nDette fører til at Silje ikke føler seg sett eller hørt i gruppen."
              "\nDet fører til at arbeidsmoralen til Silje synker, og at UX-designet ikke blir bra i det ferdige produktet.")
        poeng += 6

#Dersom hva folk setter størst pris på ble valgt
    elif svar2 == 2:
        print("\nHer får både Silje og Elias deler av viljen sin."
              "\nBegge føler seg hørt, og konflikten minker."
              "\nAlle blir ferdige innenfor tidsfristen, og produktet blir optimalt.")
        poeng += 10

#Dersom individuelle samtaler ble valgt
elif svar1 == 2:
    print("\nEtter at Erling har hørt hva begge har å si,"
          "\nkommer han med en løsning som heller mer mot Siljes side, men som fortsatt løser mesteparten av konflikten."
          "\nProduktet nærmer seg sluttfasen, men konflikten oppstår igjen på grunn av dårlig kommunikasjon mellom Elias og Silje."
          "\nDette skyldes at Elias blir sjalu fordi Erling tok mer hensyn til Silje."
          "\nDerfor vil han ikke snakke med henne.")
    poeng += 0

fortsette()

#Første spørsmål om Hamdi og Hallgeir
svar3 = gyldig_svar("\nDette er den andre utfordringen til Erling"
                    "\nHamdi og Hallgeir er ikke enige om det eksisterende systemet og et nyere, åpent system."
                    "\nErling har tre valg:"
                    "\n1.Felles møte for å avklare uenighet, ideen med flest stemmer vinner."
                    "\n2.Avvente og håpe at det løser seg selv."
                    "\n3.Erling er redd for å være partisk så han tar inn HR for å løse konflikten saklig."
                    "\nTrykk på 1, 2 eller 3 for å velge tilsvarende løsnign: ",
                    [1,2,3])

#Dersom møte med flest stemmer ble valgt
if svar3 == 1:
    print("\nDet blir tatt en avstemning, og man kommer frem til en løsning."
          "\nTaperen av avstemningen føler seg ikke satt pris på.")
    poeng += 6

#Dersom avventing ble valgt
elif svar3 == 2:
    print("\nKonflikten eskalerer til en personkonflikt."
          "\nBegge parter drar med seg andre i gruppen med i konflikten."
          "\nTeamet har ingen prototype å vise frem når fristen går ut.")
    poeng += 0

#Dersom Erling ber om hjelp fra HR ble valgt
elif svar3 == 3:
    print("\nDe kommer frem til en felles enighet."
          "\nOg Erling mister ikke tilliten til de andre gruppemedlemmene.\n")
    poeng += 10

fortsette()

#Første spørsmål angående team motivasjon
svar4 = gyldig_svar("\nNå har du kommet til den siste utfordringen til Erling."
                    "\nHvordan bevare motivasjonen i teamet."
                    "\nErling har to ideer."
                    "\n1.Sette av tid fra prosjektet for relasjonsbygging og sosiale aktiviteter."
                    "\n2.Prioritere fremdrift og leveranse for å holde fokus på resultat."
                    "\nTrykk på 1 eller 2 for å velge tilsvarende løsning: ",
                     [1,2])

#Dersom implementering av relasjonsbygging ble valgt
if svar4 == 1:
    print("\nErling implementerer relasjonsbygging og sosiale aktiviteter fremfor fremdrift og leveranse."
          "\nErling arrangerer klatring og grilling for prosjektmedlemmene."
          "\nProsjektmedlemmene styrker samholdet og får en større forståelse/respekt for hverandre, hvor konfliktfaren minker,"
          "\nmen tiden til prototypen skal være ferdig skaper spenning i teamet.")
    poeng += 6

#Dersom prioritering av fremdrift ble valgt
elif svar4 == 2:
    print("\nErling prioritere fremdrift og leveranse for å holde fokus på resultatet."
          "\nErling gjennomfører jevnlige møter for å følge opp fremdriften for å sikre at prosjektet holder tidsplanen."
          "\nHan fordeler også arbeidsoppgavene ut fra kompetansen prosjektmedlemmene har."
          "\nProsjektet får en økt produktivitet, hvor unødvendige diskusjoner, analyser og planlegging forsvinner."
          "\nFaren for konflikter mellom prosjektmedlemmer har også minker grunnet skjerpet oppførsel og økt fokus.")
    poeng += 10

fortsette()

#Poengsummen og endings
if poeng == 30:
    print("\nBra jobba!"
          "\nDu valgte alle de beste valgene og prosjektet ender bra uten konflikter!"
          "\nDu fikk 30 poeng som er maks poengsum!")
#Bra ending

elif poeng <= 6:
    print("\nDårlig jobba >:("
          "\nDu valgte mesteparten av de verste alternativene og prosjektet gikk i dass."
          f"\n du fikk {poeng} poeng av 30 mulige.")
#Dårlig ending

else:
    print("\nDu gjorde en helt OK jobb."
          "\nProsjektet ble ferdig, men det var små konflikter her og der."
          "\nOg forbedringspotensial i prosjektet."
          f"\nDu fikk {poeng} poeng av 30 mulige.")
#Mid ending

