
[[Sensorer]]

---

**absolutt**
- koordinat i rommet
- satelitt
**relativ**
- til andre objekt
- sener og motaker lokalt
- vinkelposisjon

**satelitt**
globale systemer
- GPS, USA
- Glonass, Russland
- Beidou, Kina
- Galileo, EU
- QZSS, Japan
- IRNSS, India

prinsipp for satelitt
trilaterasjon
- krever 3(4) satelitter
- kjent satelittposisjon
- kjent sendetid fra satelitt

**[[GPS]]** {
- satelitt
- monitor
- kontroll
- stasjon for oppdatering
- så oppdatere satelitt og kjøre igjenn

en målefeil i tid på 1$\mu$ gir 300km feil

**signal fra satelitt**

frequ,
L1 = 1575.42 MHz
L2 = 1227.60 MHz
L5 = 1176.45 MHz

PRN(Pseudo Random Noise), identifikasjon
navigasjonsmelding, bane og posisjon

**feilkilder**
- bane
- lonosfæren
- troposfæren
- transmisjonsforrhold
- geometriske forrhold
- refleksjoner (multipath)

Multipath: signal får ulik flygetid. f.eks spretter av en bygning før rettlinjet mot satelitt. og direkte rettlinjet blir blokkert.

**maskinvare**
systemet: sender/satelitt, kintroll- og monitorstasjoner
bruker: mottaker, antenne, prosessor og kommunikasjon(for hjelpe/korrigering)


---

**oppsett**
ultimate GPS Breakout v3. E487316. PA6H1F1702
- lodde
- kommunikasjon?
- arduino bibliotek: adafruit GPS library
- plassere så den får godt signal
}

