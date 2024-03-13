[[Sensorer]]

bimetalltermostat
- ulik tep åpner/lukker krets
- mekanisk bryter > 2 metall, en hurtig utviding, en sakte > klikker bryter
- 

termokopling
- temp avhengig spenning mellom metaller
- funksjon av materialene og temp på det varme punktet
- mindre presis en RTD
- utnytter seebeck-effekten
- større intervall
- vanskelige miljøer

termistor
- halvleder
- negativ/positiv endring i resistans
- temp avhengig resistans
- tilfører litt energi til sensor > unøyaktig
 $$R_t = Ke^\frac{\beta}{t}$$

RTD (resistance temp detector)
- temp avhengig resistans i metall
- tilfører litt energi til sensor > unøyaktigheter
- NB! termistor har større endring i resistans per grad en RTD > høyere sensitivitet
- $$R_t = R_0(1+\alpha \cdot t)$$

bandgap
- temp avhengig spenning i transistor
- typisk base emitter spenning på en transistor
- typisk på integrert krets
- 2 typer (ds12b20, TMP36) arduino har TMP


