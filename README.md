# VEFÞ2VÞ05DU

## Verkefni spurningar og linkar

### Verkefni 2
#### 1. Þegar maður notar MVC í bakendavefþróun þá eru HTTP request sent í Controllerinn sem sendir svo gögnin í Modelið og talar saman við það. Eftir það er svo svarað clientinum með því að senda View á hann.

#### 2. WebSockets leyfa client-side JavaScript að opna tengingu á server og halda henni opni til að senda gögn á server. Gögn eru sent á milli þeirra sem skilaboð sem gerist hratt vegna opni tengingu á milli servers og clients.

#### 3. MV* stendur fyrir Model, View og * þýðir hvað sem er. MV* notar sömu hugmyndir og MVC en breytir því eftir þörfum. * er það sem tengir saman View og Model og gerir því kleift að tala saman. * getur verið t.d Presenter (MVP) eða ViewModel (MVVM)

### Verkefni 3.2
#### 1. Object-relational mapping (ORM) er forritunartækni til að umbreyta gögnum milli mismunandi forritunarmála sem nota object based forritun. Þetta býr til "virtual object database" sem hægt er að nota innan forritunarmálsins.
#### Verk 3.2 Youtube link: https://www.youtube.com/watch?v=quiANhNaz6c&

### Verkefni 3.3
#### 1. Web API segir hvernig forrit ættu að tala saman og notar HTTP sem millilið. Web service er einhver partur af forriti sem makes itself available over the Internet and standardizes its communication via XML encoding. Bæði web APIs og web service eru leið fyrir client og host að tala saman. Bæði styðja XML-based data payloads, en JSON er algengara fyrir web APIs.

#### 2.a JSON: 
{"pontun": {"crust": "original","toppings": "cheese, pepperoni, garlic","status": "cooking","customer": "name, phone"}}
#### 2.b XML:
< pontun><br>
  < crust>original< /crust><br>
  < toppings>cheese, pepperoni, garlic< /toppings><br>
  < status>cooking< /status><br>
  < customer>name, phone< /customer><br>
< /pontun>

#### 3.
##### Layer 7 - Application layerinn er það sem notendur sjá og nota eins og t.d browsers eða önnur forrit.
##### Layer 6 - Presentation layerinn “presents” data for the application or the network.
##### Layer 5 - Session layerinn setur upp session tengingu milli 2 tölva.
##### Layer 4 – Transport layerinn sér um að koma öllum gögnum til skila.
##### Layer 3 - Network layerinn er ábyrgur fyrir pakkaframsendingu í gegnum routera.
##### Layer 2 – Data Link layerinn veitir node-to-node gagnaflutning milli tveggja beintengda nodes.
##### Layer 1 - Physical layerinn er allt hardware tengt.

#### 4. RESTful API er API sem notar HTTP requests til að nota GET, PUT, POST og DELETE.

#### 5.a. HTTP Request
Status line <br>
General header <br>
Request headers <br>
Entity headers <br>
Auð lína<br>
Message body <br>

#### 5.b. HTTP Response
Status line <br>
General header <br>
Response headers <br>
Entity headers <br>
Auð lína<br>
Message body <br>

#### 6. Token based authentication leyfa notendum að slá inn notandanafn og lykilorð til þess að fá token sem leyfir þeim að sækja specific resource á vefsíðum án þess að nota notandanafn og lykilorð. OAuth gerir notendum kleift að veita third-party access að vefsíðum án þess að deila lykilorði.
