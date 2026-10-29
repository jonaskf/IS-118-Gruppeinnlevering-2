# Forklaring og start av programmet
print("ERLINGS TRE UTFORDRINGER")
print("Du er Erling, prosjektlederen for kommunens nye medborgerportal!")
print("Teamet har jobbet i seks uker. Prototypen skal være klar om tre uker.")
print("Uenigheter har utviklet seg til konflikter, og samarbeid er vanskelig.")
print("Du får tre situasjoner du må komme deg igjennom. Noen valg åpner nye spørsmål underveis.")
print("Valgene dine påvirker både samarbeidet videre og hvordan prosjektet ender. Lykke til! :)")

# Første beslutning: Silje og Elias
print("\n1. KONFLIKTEN MELLOM SILJE OG ELIAS")
print("Silje ønsker god brukeropplevelse og rom for innovasjon.")
print("Elias prioriterer sikkerhet og budsjett. Uenigheten har blitt personlig.")
print("\n1: Ta saken opp i plenum.")
print("2: Ta individuelle samtaler med Silje og Elias.")

# Lager en loop så man bare kan skrive "1" eller "2" og sånn at bokstaver ikke krsjer programmet
valg1 = input("Hva velger du? Skriv 1 eller 2: ")
while valg1 not in ("1", "2"):
    print("Ugyldig svar. Du må skrive 1 eller 2.")
    valg1 = input("Prøv igjen: ")

silje_elias_enige = False

if valg1 == "1":
    print("\nDu samler teamet. Silje og Elias forklarer forslagene sine.")
    print("Gruppen er fortsatt uenig. Hvordan vil du komme frem til en avgjørelse?")
    print("\n1: La flertallet bestemme gjennom håndsopprekning.")
    print("2: Diskuter hva partene setter mest pris på, og finn en felles løsning.")

    plenum_valg = input("Hvordan avgjør du saken? Skriv 1 eller 2: ")
    while plenum_valg not in ("1", "2"):
        print("Ugyldig svar. Du må skrive 1 eller 2.")
        plenum_valg = input("Prøv igjen: ")

    if plenum_valg == "1":
        valg_silje_elias = "Avstemning i plenum"
        print("\nElias sitt forslag vinner avstemningen.")
        print("Silje føler seg ikke hørt og mister motivasjon.")
        print("Gruppen har valgt en løsning, men brukeropplevelsen blir dårligere.")
    else:
        valg_silje_elias = "Felles løsning i plenum"
        silje_elias_enige = True
        print("\nSilje og Elias får begge gjennomslag for deler av forslagene sine.")
        print("De føler seg hørt, og konflikten dempes.")
        print("Samarbeidet gir bedre forutsetninger for å bli ferdige innen fristen.")
else:
    valg_silje_elias = "Individuelle samtaler"
    print("\nDu hører begge sider, men velger en løsning som heller mot Siljes forslag.")
    print("Konflikten roer seg først. Senere føler Elias seg tilsidesatt.")
    print("Han slutter å snakke med Silje, og konflikten oppstår igjen.")

# Andre beslutning: Hamdi og Hallgeir
print("\n2. UENIGHETEN MELLOM HAMDI OG HALLGEIR")
print("Hamdi vil bruke kommunens eksisterende plattform for digitale folkemøter.")
print("Hallgeir ønsker et åpent system med rom for spontane innspill.")
if silje_elias_enige:
    print("Etter den felles løsningen snakker Silje og Elias bedre sammen.")
    print("Hamdi og Hallgeir får se at det går an å finne løsninger sammen.")
elif valg1 == "1":
    print("Silje har trukket seg tilbake etter avstemningen.")
    print("Hamdi og Hallgeir er bekymret for at deres innspill også kan bli oversett.")
else:
    print("Elias unngår Silje etter de individuelle samtalene.")
    print("Den dårlige kommunikasjonen gjør det vanskeligere å diskutere nye forslag.")
print("\n1: Grip inn for å få avklart uenigheten.")
print("2: Ikke bland deg, og håp at Hamdi og Hallgeir løser uenigheten selv.")

valg2 = input("Hva velger du? Skriv 1 eller 2: ")
while valg2 not in ("1", "2"):
    print("Ugyldig svar. Du må skrive 1 eller 2.")
    valg2 = input("Prøv igjen: ")

hamdi_hallgeir_enige = False

if valg2 == "1":
    print("\nDu bestemmer deg for å gripe inn før konflikten vokser.")
    print("Du er venn med Hallgeir og må tenke gjennom hvordan saken håndteres.")
    print("\n1: Samle teamet til et møte og la flertallet bestemme.")
    print("2: Hent inn HR for å sikre en nøytral samtale.")

    konflikt_valg = input("Hvordan griper du inn? Skriv 1 eller 2: ")
    while konflikt_valg not in ("1", "2"):
        print("Ugyldig svar. Du må skrive 1 eller 2.")
        konflikt_valg = input("Prøv igjen: ")

    if konflikt_valg == "1":
        valg_hamdi_hallgeir = "Felles møte med avstemning"
        print("\nFlertallet velger Hallgeirs forslag, og teamet kan arbeide videre.")
        print("Hamdi føler likevel at bidragene hans ikke blir satt pris på.")
        print("Avgjørelsen er tatt, men uenigheten er ikke helt løst.")
    else:
        valg_hamdi_hallgeir = "Nøytral samtale med HR"
        hamdi_hallgeir_enige = True
        print("\nHR hjelper partene med å forstå hverandre og komme frem til enighet.")
        print("De blir enige om å ta utgangspunkt i kommunens eksisterende systemer.")
        print("Den nøytrale håndteringen gjør at teamet beholder tilliten til deg.")
else:
    valg_hamdi_hallgeir = "Du håper det blåser over og vil ikke blande deg."
    print("\nHamdi og Hallgeir klarer ikke å bli enige.")
    print("Sakskonflikten blir en personkonflikt, og de trekker andre inn i den.")
    print("Arbeidet stopper opp. Teamet har mistet tiden de trengte til prototypen.")

# Tredje beslutning: Motivasjon og fremdrift
print("\n3. MOTIVASJONEN I TEAMET")
if valg2 == "2":
    print("Konflikten mellom Hamdi og Hallgeir har splittet teamet.")
    print("Mye utviklingstid er allerede tapt. Nå må du forsøke å samle gruppen.")
elif silje_elias_enige and hamdi_hallgeir_enige:
    print("Begge konfliktene er dempet, og teamet har begynt å samarbeide igjen.")
    print("Nå må du vurdere hvordan dere skal bevare tilliten frem mot fristen.")
else:
    print("Teamet arbeider videre, men tidligere avgjørelser har etterlatt misnøye.")
    print("Uløste problemer preger samarbeidet når fristen nærmer seg.")
print("Fristen nærmer seg. Du må velge hva teamet skal prioritere nå.")
print("\n1: Sett av tid til relasjonsbygging og sosiale aktiviteter.")
print("2: Prioriter fremdrift og leveranse.")

valg3 = input("Hva velger du? Skriv 1 eller 2: ")
while valg3 not in ("1", "2"):
    print("Ugyldig svar. Du må skrive 1 eller 2.")
    valg3 = input("Prøv igjen: ")

if valg3 == "1":
    valg_motivasjon = "Relasjonsbygging og sosiale aktiviteter"
    print("\nTeamet setter av tid til å bli bedre kjent og gjenoppbygge tillit.")
    print("Det tar tid fra utviklingen, men gir større forståelse og bedre samarbeid.")
    if valg2 == "2":
        print("Tiltaket kommer likevel for sent til å hente inn tiden som er tapt.")
else:
    valg_motivasjon = "Fremdrift og leveranse"
    print("\nTeamet retter oppmerksomheten mot oppgavene og tidsfristen.")
    print("Det blir mindre tid til relasjoner, og stemningen blir mer anspent.")
    if not silje_elias_enige or not hamdi_hallgeir_enige:
        print("De uløste konfliktene forverres når teamet presses til å levere.")

# Viser valgene før det samlede resultatet
print("\nDINE VALG")
print("Silje og Elias:", valg_silje_elias)
print("Hamdi og Hallgeir:", valg_hamdi_hallgeir)
print("Motivasjon:", valg_motivasjon)

# God slutt krever at begge konfliktene løses, og at tilliten bygges videre.
# Å velge å ta avstand i konflikt 2 gir forsinkelse uansett siste valg.
# En uløst konflikt mellom Silje og Elias blir også alvorlig pga. leveransepress.
# De andre kombinasjonene gir delvis bedring, men fortsatt sårbare relasjoner.
if silje_elias_enige and hamdi_hallgeir_enige and valg3 == "1":
    print("\nGOD LØSNING")
    print("Begge konfliktene er håndtert, og relasjonsbyggingen styrker tilliten.")
    print("Teamet samarbeider godt og går videre fra storming til norming.")
    print("Selv med tidspress klarer dere å ferdigstille prototypen innen fristen.")
elif valg2 == "2" or (not silje_elias_enige and valg3 == "2"):
    print("\nDÅRLIG LØSNING")
    print("Konfliktene har fått utvikle seg, og samarbeidet bryter sammen.")
    print("Krangling og dårlig kommunikasjon hindrer fremdriften.")
    print("Fristen er kommet, og du har ingen ferdig prototype å vise frem.")
else:
    print("\nOK LØSNING")
    print("Teamet kommer videre, men problemene er bare delvis løst.")
    print("Relasjonene er fortsatt sårbare, og stemningen er anspent.")
    print("Du må følge opp samarbeidet for at teamet skal gå videre til norming.")
