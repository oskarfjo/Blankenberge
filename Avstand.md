
[[Sensorer]]


**applikasjoner**
- lokalisering inne
- hastighet
- krasje forebygging


**båten**
- docking
- relativ posisjonering
- avstand til andre bevegelige/faste objekter


**typer**
flygetid (time of flight)
- aukustisk: ultralyd, sonar
- laser
- ultralyd
- radar

**aukustisk**
sonar
unøyaktig
emitter and reciever
kan brukes til å definere underlag
enkle ting som ryggesensorer og div
40 til 180 KHz (mennesker hører opp til 20 KHz)

**infrarød**
bølgelengde: 750nm til 1mm
mellom synlig og mikrobølger
emitter og sensor
relativt billing

**Radar**
radiobølger sendes og return leses

radar for navigasjon (bølgeanalyse): 8 til 12 GHz

spinner og jevnlig sender signaler

elektromagnetiske bølger


**arduino aukustisk**

HC_SR04

tig pin, starter sending output
echo pin, sensor pinnen input

trig pin på HIGH i delayMicroseconds(10)

måle HIGH verdien på pulsein etterpå

konvertere til avstand med (duration * 0.0343)/2 ; /2 pga halve distansen. 0.0343 lydens hastighet i cm/us

