poeng = 0

print ("Erling Jobber som prosjektleder for digital utvikling i en liten kommune i Norge, og skal utvikle og lansere en digital medborgerportal for kommunen.")
print ()
print ("Nå har teamet til Erling jobbet med prosjektet i 6 uker, hvor det har oppstått flere konflikter internt i teamet.")
print ()
print ("Den første konflikten har utviklet seg til en personkonflikt som hanlder om Silje og Elias. Her kan Erling velge mellom å ta konfliken i plenum, la gruppen løse konflikten internt eller ha individuelle samtaler med partene")
print ()
print ("Hva velger Erling?")
print ("1. Ta konflikten i plenum.")
print ("2. La gruppen diskutere saken internt.") 
print ("3. Benytte seg av individuelle samtaler.")
print ()
svar = input("1, 2 eller 3 valg = ")

if svar == "1":
    poeng += 2
    print ("Erling tar opp konflikten i plenum for å skape åpenhet og involvere resten av gruppen. Erling benytter seg av en håndopprekning om hvilken ide som er viktigst.")
    print ("Elias sitt forsvalg ender opp med å vinne, hvor flertallet mener at selve programmet er viktigere enn UX-designet. Dette fører til at Silje føler seg oversett og ikke hørt i gruppen, som medvirker at UX-designet blir dårligere enn det kunne ha vært og Silje mister motivasjon.")

elif svar =="2":
    poeng += 5
    print ("Erling lar gruppen diskutere saken for å finne en løsning som ivaretar ønskene og behovene til både Silje og Elias.")
    print ("Både Silje og Elias får gjennomslag for deler av forlagene sine. Begge føler seg hørt, og konflikten minsker.")

elif svar=="3":
    poeng += 3
    print ("Erling tar med både Silje og Elias for å ta individuelle samtaler om konflikten for å høre deres meninger og forslag.")
    print ("Ering sier seg mer enig med Slije sin ide, men løser mesteparten av konflikten, men på grunn av dårlig kommunikasjon oppstår konflikten på nytt hvor Elias er misunelig på Erling sitt valg. Elias slutter dermed å prate med Silje.")

print ()
print ()
print ("Den andre konflikten hander om Hamdi og Halgeir som foreløpig er en sakskonflikt. De er uenige om hvordan oppgaven best kan løses.")
print ("Hva velger Erling?")
print ("1. Arrangere et felles møte med teamet.")
print ("2. Forholde seg passiv")
print ("3. Involvere HR-avdelig")
print ()
svar = input ("1, 2 eller 3? valg = ")

if svar =="1":
    poeng += 2
    print ("Erling samler teamet til et møte der ale får mulighet itl å uttrykke menigene sine og diskutere de ulike forslagene. Målet er å komme fram til en løsning som fungerer for flertallet, og som kan gjennomføres innen tidsfristen.")
    print ("Flertallet støtter Halgeirs forlag, gjennom en demokratisk avstemmning. Hamdi føler imindlertidig at både meningene og bidragene hans ikke blir satt pris på. Selv om gruppen har kommet fram til en løsning er det sikker ikke at konflikten er fullstendig løst.")

elif svar == "2":
    poeng +=3
    print ("Erling velger å ikke gripe inn i konflikten, og håper at Hamdi og Halgeir klarer å løse uenigheten på egenhånd.")
    print ("Hamdi og Halgeir klarer ikke å bli enige, og konflikten eskalerer til en personkonflikt. De slutter å kommunisere direkte med hverandre og begynner i stedet å snakke negativt om hverandre intert i gruppen.")

elif svar == "3":
    poeng += 5
    print ("Erling velger å involvere HR-avdeligen fordi han og Halgeir er gode venner. Han innser at det kan være vanskelig å ta en helt nøytral avgjørelse når han har personlige forhold til en av partene.")
    print ("Hamdi og Halgeir forklarer sine perspertiver og får en bedre forståelse av hverandre. De blir enige om at det, med tanke på den korte tiden de har igjen, er det mest hensiktsmessig å bruke kommunens eksisterende systemer som utganspunkt for å utvikle et best mulig produkt.")

print ()
print ()
print ("Etter som det har oppstått konflikter gjennom prosjektet til Erling bestemmer han seg for å ta to valg.")
print ()
print ("Valg 1. Sette av tid til relasjonsbygging og sosiale aktiviteter for å gjennoprette arbeidsmoral og redusere konflikter mellom prosjektmedarbeidere.")
print ()
print ("Valg 2. Prioritere fremdrift og leveranse for å holde fokus på resultatet")
print ()
print ("Hva velger Erling?")

svar = input ("1 eller 2? valg = ")

print ()
if svar =="1":
        poeng += 3
        print ("Erling setter av tid til sosiale aktiviteter fremfor fremdrift for å øke samholde i laget og minke faren for senere konflikter.")
        print ("Erling arrangerer klarting og grilling for prosjektmedlemmene. Dette fører til et styrket samhold hvor prosjektmedlemmene har en større respekt/forsåelse for hverandre. Konfliktfaren minker også, men tidrn til prototypen skal være ferdig skaper spenning i teamet,")


elif svar =="2":
     poeng += 5
     print ("jevnlige møter for å følge opp fremdriften for å sikre at prosjektet holder tidsplanen. Han fordeler også arbeidsoppgavene utafra kompetanse prosjektmedlemmene har. Prosjektet for en økt produktivitet, hvor unødvendige diskusjoner, analyser og planlegging forsvinner.")
     print ("Faren for konflikter melllom prosjektmedlemmer har også minket grunnet skjerpet oppførsel og økt fokus.")


if poeng >= 13:
     print ("DEN GODE SLUTTEN")
     print ("Konfliktene løser seg og prosjektet beveger seg mot norming-fasen. Prosjektmedlemmene samarbeider godt og ingenting kan hindre dem i å fullføre prosjektet.")


elif poeng >= 9:
     print ("DEN HELT OK SLUTTEN")
     print ("Enkelte konflikter er delvist løst, men det er fremdeles lada stemmning i teamet. Prosjektet bli fullført i tide, men Erling må jobbe mer får å få prosjektmedlemmer på riktig frekvens.")

else:
     print ("DEN DÅRLIG SLUTTEN")
     print ("Konfliktene blir ikke løst, hvor det krangles mye internt i teamet og det er like før det kollapser. Tidsfristen blir ikke nåd, hvor Erling sitter igjen med ingen prototype å vise.")



