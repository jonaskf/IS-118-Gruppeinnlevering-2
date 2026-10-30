poeng = 0
#introduksjon
print ("Det har gått seks uker siden Erling, prosjektleder for utviklingen av kommunens nye digitale medborgerportal, samlet sitt prosjektteam for første gang. Etter en inspirerende oppstart med høy energi, begynner samarbeidet nå å møte sine første reelle prøver.")
print ()
input("Trykk enter for å fortsette" )
print ()
print ("I starten var stemningen god. Gruppen opplevde høy motivasjon og fellesskap i målet om å lage en portal som kunne øke innbyggerengasjement og transparens i kommunen. Men nå, etter seks uker, har prosjektet gått inn i den klassiske storming-fasen, der ulike faglige perspektiver og personlige preferanser begynner å kollidere")
print ()
input("Trykk enter for å fortsette" )
print ()
print ("Du er Erling, du skal lede teamet gjennom denne storming-fasen. Måten du håndterer disse konfliktene på vil påvirke hele prosjektets fremdrift og suksess. Du må finne en balanse mellom å opprettholde teamets motivasjon og å sikre at prosjektet holder seg på sporet.")
print ()
print ("Er du klar for oppdraget?")
svar = input ("ja/nei: ")
if svar == "ja" or svar == "JA" or svar == "Ja": print ("Fantastisk! la oss sette i gang! ")
elif svar == "nei" or svar == "NEI" or svar == "Nei":
    print ("Det var synd, men du kan ikke trekke deg nå. ta deg sammen og løs dette for gruppa!")
else: print (" jeg skjønner ikke hva du prøver å si, men jeg tolker det som et JA!, så la oss komme i gang!")

#konflikt 1
print ()
print ("Den første konflikten som oppstår er en uenighet mellom Silje og Elias. Silje, som er en ekstern UX/UI-designer, mener løsningen Elias foreslår vil låse brukeropplevelsen og hindre innovasjon. Mens Elias, som er en  IT-rådgiver fra kommunens IT-avdeling, mener Siljes forslag er urealistisk, usikkert og for kostbart. Diskusjonene blir stadig mer emosjonelle, og begge trekker støtte fra sine nærmeste i teamet.")
print ()
input("Trykk enter for å fortsette ")
print ()
#løsning 1
while True:
    print ("Hva vil du gjøre for å løse denne konflikten? Du kan velge mellom følgende alternativer:")
    print ("Løsning a: Ta opp konflikten i plenum for å skape åpenhet for resten av gruppen. Begge partene legger fram sine synspunkter og deretter blir det tatt en håndsopprekning av hvilken løsning de skal gå for.")
    print ()
    print ("Løsning b: Ta opp konflikten i plenum for å skape åpenhet for resten av gruppen. Denne gangen avgjør du løsningen ut ifra hvilken løsning hvert gruppemedlem setter mest pris på.")
    print ()
    print ("Løsning c: Du kan ta en-til-en samtaler med Silje og Elias for å forstå begges bekymringer og deretter gå for en løsning ut ifra hvilken løsning du synes passer best")
    print ()
    konflikt1 = input ("vil du velge løsning a, b eller løsning c? (a/b/c): ")
    if konflikt1 == "a" or konflikt1 == "A":
            print ()
            print ("Du velger å ta opp konflikten i plenum. Dette skaper åpenhet, men diskusjonen blir raskt preget av sterke meninger og det blir vanskelig å komme til enighet. Til slutt ender det med at flertallet stemmer for Elias sin løsning, noe som fører til at Silje føler seg overkjørt og demotivert.")
            poeng += 5
            break
    elif konflikt1 == "b" or konflikt1 == "B":
           print ()
           print("Du velger å ta opp konflikten i plenum. Dette skaper åpenhet og alle gruppemedlemmene legger fram hvilken løsning de setter mest pris på. Her får både Silje og Elias deler av sin vilje, begge føler seg hørt og konflikten minker. Alle blir ferdig innenfor tidsfristen og produktet er optimalt")
           poeng += 10
           break
    elif konflikt1 == "c" or konflikt1 == "C":
           print ()
           print ("Du velger å ta en-til-en samtaler med Silje og Elias. Dette gir deg en bedre forståelse av begges perspektiver og lar deg ta en avgjørelse som du synes passer best. Du er ingen ekspert i dette fagfeltet så du velger en løsning som ikke funker...")
           poeng += 0
           break
    else:
            print ()
            print ("ugyldig svar, prøv igjen, svaralternativene er a, b eller c")

#konflikt 2
print ("Samtidig med konflikten mellom Silje og Elias oppstår det spenning mellom Hamdi (kulturavdelingen) og Hallgeir (brukerrepresentant)")
print ()
input ("Trykk enter for å fortsette ")
print ()
print ("De er uenige i hvordan innbyggerne skal kunne delta i digitale folkemøter. Hamdi ønsker en kontrollert løsning fjennom å bruke kommunens eksisterende platforme, mens Halgeir ønsker et mer åpent, dialogbasert system med rom for spontane innspill.")
print ()
print ("Foreløpig er uenigheten lavmælt, men Erling merker at frustrasjonen vokser. Prosjektet nærmer seg en viktig milepæl: første prototype skal være klar om tre uker. Stemningen er spent, kommunikasjonen hakkete, og Erling vet at hans neste valg kan avgjøre om teamet beveger seg videre mot “norming” eller blir stående fast i stormen.")
print ()
print ("Hvordan vil du håndtere denne konflikten? Du kan velge mellom følgende alternativer:")
print ()
print ("Løsning a: Kall hele teamet inn for et felles teammøte der Hamdi og Halgeir for presentere sine løsninger og avklare uenigheter. Deretter blir det en håndsopprekning for å avgjøre hvilken løsning teamet mener er best.")
print ()
print ("Løsning b: Du kan velge å holde deg passiv. La Hamdi og Halgeir få finne ut av konflikten selv, og håpe at de kommer til enighet på egenhånd.")
print ()
print ("Løsning c: Få HR inn i casen. Siden du og Halgeir er ganske gode venner innser du at du ikke klarer å være objektiv i bestemmelsen din. La HR ta over konflikten og veilede begge parter til å finne en løsning som funker for begge.")
print ()

#løsning 2
while True:
    konflikt2 = input ("vil du velge løsning a, b eller c? (a/b/c): ")
    print ()
    if konflikt2 == "a" or konflikt2 == "A":
            print ("Du velger å kalle inn hele teamet for et felles teammøte. Etter at begge parter har presentert sine synspunkter, blir det tatt en håndsopprekning, og teamet bestemmer seg for å gå videre med Halgeirs forslag om et mer åpent system. Prosjektet går videre, men Hamdi føler seg overkjørt og demotivert, noe som kan påvirke hans engasjement i prosjektet fremover.")
            poeng += 5
            break
    elif konflikt2 == "b" or konflikt2 == "B":
           print ("Du velger å holde deg passiv. Hamdi og Halgeir prøver å finne ut av konflikten selv, men uenigheten eskalerer, og prosjektet blir forsinket. De snakker ikke sammen lenger og snakker hverandre ned til de andre teammedlemmene.")
           poeng += 0
           break
    elif konflikt2 == "c" or konflikt2 == "C":
           print ("Du velger å involvere HR i konflikten. HR tar over og veileder Hamdi og Halgeir til å finne en løsning som fungerer for begge parter. Dette bidrar til å løse konflikten på en profesjonell måte. Prosjektet går videre og begge parter føler seg sett og hørt, noe som styrker teamets samarbeid og engasjement. Erling beholder også tilliten til teamet.")
           poeng += 10
           break
    else:
            print ("ugyldig svar, prøv igjen, svaralternativene er a, b eller c")

#konflikt 3
print ()
print ("Til slutt må Erling bestemme om han vil forebygge slike konflikter i fremtiden, eller om han er nødt til å prioritere å jobbe hardt en stund frem mot tidsfristen og heller ta teambyggingen i ettertid")
print ()
print ("Hva velger du?")
print ("Vil du gå for løsning a: Implementere relasjonsbygging og sosiale aktiviteter fremfor fremdrift og leveranse.")
print ()
print ("Eller vil du gå for løsning b: prioritere fremdrift og leveranse for å holde fokus på resultatet")
print ()
#løsning 3
while True:
       konflikt_3 = input ("velg a eller b: ")
       print ()
       if konflikt_3 == "a" or konflikt_3 == "A":
              print ("Erling arrangerer klatring og grilling for prosjektmedlemmene. Prosjektmedlemmene styrker samholdet og får en større forståelse/respekt for hverandre, hvor konfliktfaren minker, men tiden til prototypen skal være ferdig skaper spenning i teamet.")
              poeng += 5
              break
       elif konflikt_3 == "b" or konflikt_3 == "B":
              print ("Erling gjennomfører jevnlige møter for å følge opp fremdriften for å sikre at prosjektet holder tidsplanen. Han fordeler også arbeidsoppgavene utafra kompetanse prosjektmedlemmene har. Prosjektet for en økt produktivitet, hvor unødvendige diskusjoner, analyser og planlegging forsvinner. Faren for konflikter mellom prosjektmedlemmer har også minker grunnet skjerpet oppførsel og økt fokus.")
              poeng += 10
              break
       elif konflikt_3 == "AI" or konflikt_3 == "ai" or konflikt_3 == "Ai":
              import time
              time.sleep(3)
              print ("...")
              time.sleep(3)
              print ("Dette var egentlig ikke et alternativ...")
              time.sleep(3)
              print ("Hvordan fant du dette?...")
              time.sleep(3)
              print ("Du har valgt å sparke hele teamet...")
              time.sleep(3)
              print ("Du erstatter alle med AI...")
              time.sleep(3)
              print ("Du har nå et team som aldri krangler, aldri blir slitne og alltid leverer på tid. Du har laget det perfekte teamet. Nå kan du bare slappe av og la teamet fikse resten for deg")
              poeng = 100000
              break
       else:
              print ("ugyldig svar, prøv igjen, svaralternativene er a eller b")

#løsningen
print ()
print ("Nå har du prøvd deg på å løse alle konfliktene. La oss se hvordan det gikk")
print ()
input ("Trykk enter for å fortsette ")
print ()
if poeng == 30:
       print ("Bra jobba! Du fant de beste løsningene for teamet. Nå kan teamet endeleig gå komfortabelt over i norming fasen og dere vil ha en prototype som er klar når fristen kommer")
       print ("Takk for den gode jobben!")
elif poeng == 5:
       print ("Du er i hvertfall i mål!")
       print ("Du løste ingen av konfliktene ordentlig, prosjektet faller sammen og teamet er i ferd med å gå i oppløsning")
       print ("Minn oss på å aldri be deg om hjelp igjen")
elif poeng == 100000:
       print ("Det skulle egentlig ikke ha funka...")
       time.sleep(2)
       print ("...")
       time.sleep(1)
       print("Javel, du erstattet hle teamet med AI og som sagt vil dette løse alle problemene dine, bare ikke glem å betale for alle abbonomentene dine ;)")
else:
       print ("Du løste enkelte konflikter som hjalp litt med å holde temperaturen i teamet nede. Konfliktene vil trolig oppstå igjen, så du har bare forskjøvet problemet til senere. Ikke helt ideelt.")
       print ("Jeg tror du burde prøve dette en gang til")
       
