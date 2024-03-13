
[[Matte Prosjekt]]

**Variabler**
- $J$ er fluksen av et system. 
- $A$ er en overflate hvor fluks måles
- $I$ er strømmen av partikler
- $N$ er kvantitet, og $\dot N$ er den tidsderiverte til $N$ 
- $v$ er farten til et partikkel og er en vektor 
- $V$ er volumet. 
- $n$ er partikkeltettheten
- $\sigma$ er en kilde eller et sluk for $N$; hvis $\sigma = 0$ vil $N$ være bevart.
- $\sum$ er summen av alle kilder og sluk i volumet

**uttrykk og utledninger**
- $J=$ $\frac{\dot N}{A}$. endring av stoffmengde over tid delt på målområde.
- videre: $\vec J = n \vec v$. stofftettheten ganger retning og hastighet; $|v|$ $\tiny \vec J \text{ beskriver både størrelse og retning til fluksen}$
- $\int \vec J \vec{dA}$  er netto-mengden av stoff gjennom en overflate $A$. 
- $N$ kan defineres som $\int n dV$; stofftettheten i alle punkter innenfor volumet = kvantitet av stoff 
- $\dot V$ $=$ $Av$ kan manipuleres til $dV = A \cdot v dt$. $vdt$ kan også skrives som $dr$
- $n$  er definert som $\frac{N}V$; stoff per volum = tetthet av stoff
- $\sum$ er definert som $\int \sigma dV$ 

Kontinuitetslikningen: https://en.wikipedia.org/wiki/Continuity_equation
Divergensteoremet: https://en.wikipedia.org/wiki/Divergence_theorem
Fick's lover: https://en.wikipedia.org/wiki/Fick%27s_laws_of_diffusion

----

$$ \huge \underline{Utledning}$$
$$ \text{Fick's første lov: }\underline{\vec J = -D \vec{\nabla} n }$$
$$\text{Kontinuitetslikningen: }\underline{\dot{N} + \int \vec{J} \vec{dA} = \sum}$$

1) Kontinuitetslikningen ($\dot{N} + \int \vec{J} \vec{dA} = \sum$)  sier at for ethvert gitt volum, vil endringen i massen inne i volumet over tid, pluss nettofluksen av masse ut av volumet, være lik den totale tilførselen eller fjerningen fra volumet (representert ved $\sum$)
   
2) Vi skriver om likningen til $\int \dot n dV + \int \vec j \vec{dA} = \int \sigma dV$ ved hjelp av definisjonene gitt over
   
3) Divergensteoremet(omforming av overflateintegral til volumintegral) gir så: $\int \dot n dV + \int \nabla j dV = \int \sigma dV$. Dette deriverer vi mhp $V$ så vi får: $\underline{\underline{\dot n + \vec{\nabla} \vec{J} = \sigma}}$ 

4) Stoffet er bevart så $\sigma = 0$ $\mapsto$ $\dot n + \vec{\nabla} \vec{J} = 0$ 
   
5) Vi bruker definisjonen $\vec J = -D \vec{\nabla} n$ til å få: $\dot n + \vec{\nabla}(-D \vec{\nabla} n) = 0$   $\mapsto$  $\underline{\dot n -D \nabla ^2 n = 0}$ 
   
6)   $\dot n -D \nabla ^2 n = 0$; denne likningen representerer diffusjonslikningen i et homogent og isotropisk medium under en forutsetting om at det ikke er noen kilder eller sluk. Denne likningen kan brukes til å modellere varmeoverføring

7) For å modellere varmeoverføringen; fluksen av temperaturen må:
   - $n$ = temperatur $T$. videre blir da $\dot n$ til $\dot T$, altså $\frac{\partial T}{\partial t}$ den tidsderiverte av temperaturen
   - $D$ må være den termiske diffusiviteten. $D =\frac{\kappa}{c_p \rho}$, med $\kappa$ termisk konduktivitet, $\rho$ massetetthet og $c_p$ spesifikk varmekapasitet. $D$ vil være forskjellig ved forskjellige materialer og gasser
 
8) så må det defineres betingelser:
   - **Initialbetingelser:** Beskriver temperaturen i ovnen ved oppstart av oppvarmingsprosessen. For eksempel kan temperaturen initialt være romtemperatur overalt inne i ovnen.
   - **Randbetingelser:** Disse er nødvendige for å løse ligningen og kan inkludere temperaturer på ovnens indre vegger, som kan være faste (Dirichlet-betingelser) eller avhenge av varmeoverføringen til omgivelsene (Neumann-betingelser).

9) Ved å løse varmeledningsligningen med gitte initial og randbetingelser, kan man definere temperaturfordelingen i ovnen over tid. Det viser hvordan varmen diffunderer fra de varmere delene av ovnen til de kaldere, og til slutt fører til en jevn temperaturfordeling.

---- 

$$ \huge \underline{\text{Oppgaven}}$$


## Oppgave 6: Varmeligning, 2D

Nå skal vi modellere steking av et gjenstand i en ovn.

$$
u_t = \alpha(u_{xx} + u_{yy}),
$$

hvor $\alpha=\frac{\kappa}{c_p \rho}$, med $\kappa$ termisk konduktivitet, $\rho$ massetetthet og $c_p$ spesifikk varmekapasitet. Passende tall kan slås opp på nett.

Vi antar at temperaturen av luft i ovnen holdes konstant på 200 grader hele tiden, og bruker altså randbetingelsene at $u(x,y)=200$ på alle randene.

### a)

Velg et gjenstand å steke. Finn et passende tall for $\alpha$.

### b)

Hvor lang tid tar det før temperaturen i midten av legemet når 60 grader?

### c)

Hvor lang tid tar det før temperaturen ved rander overstiger 60 grader? Er det realistisk?

### d)

Legg ved noen "varmeplotter" (altså fargeplotter med rødt varmt, blått kaldt) av legemet etter en viss tid.


## Oppgave 7: Luften skal med

Våre antagelse at temperaturen i luften holdes konstant ved 200 grader er ikke realistisk. I realitet vil temperatur senke når en kaldere objekt tas inn i ovnen. I tilfelle vil det oppstå konveksjon, siden luft er en fluid.

Vi vil ignorere konveksjon, men her er et forslag til en (litt) bedre modell: vi antar at luften holder en konstant temperatur over en viss avstand (i diagrammet $c,d$) fra objektet som stekes, men modellerer luften som er nærmere med en varmeligning

$$
u_t = \alpha( u_{xx} + u_{yy} ),
$$

hvor $\alpha$ tar et annet, lavere verdi (gjerne noen som passer til luft).

La oss prøve på nytt!

### a)

Hvor lang tid tar det før temperaturen i midten av legemet når 60 grader?


### b)

Hvor lang tid tar det før temperaturen ved rander overstiger 60 grader? Er det realistisk?

### c)

Prøv å endre størrelsen på mengde luft som modelleres med varmeligningen. Hvordan påvirker det resultatene over?

----


For oppgaven vår er det ikke en homogen og isotrop massefordeling, så i utgangspunktet kan ikke kontinuitetslikningen benyttes. Men vi kan separat definere de forskjellige "legmene" i ovnen med kontinuitetslikningen og knytte de sammen med rand betingelsene; i.e. Ved grensen mellom luft og objekt, må vi sørge for at temperaturen og varmefluksen er kontinuerlig. Dette kan bety at vi setter temperaturen ved overflaten av objektet lik temperaturen i den omkringliggende luften, og/eller at varmefluksen inn i objektet fra luften er lik varmefluksen ut av objektet til luften.

poissonlikning i 2D??