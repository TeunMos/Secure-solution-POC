# Secure-solution bagageafhandelingsysteem POC

## Inleiding
Dit is een proof of concept voor een bagageafhandelingssysteem (en vooral het beveligen ervan) voor de secure-solution.





## architectuur
De architectuur van het systeem is als volgt:
![architectuur](DocumentatieResources/c4-bagageafhandeling.svg)

**De rode objecten vallen buiten de scope**. Want die zijn te groot om te implementeren in deze POC. Dus die worden gesimuleerd, hardcoded of weggelaten.

### Bagage Tracking Systeem (Python, Flask)
> [/bagage-tracking-systeem](/bagage-tracking-systeem)
>
> TODO: Database apart hosten i.p.v. met sqlite (want dat is niet realistisch)

Dit is een simpele python (flask) api die de bagage bijhoudt. De bagage wordt nu opgeslagen in een sqlite database. het gebruikt websockets om veranderingen in de database door te geven aan de clients/front-end.

### Bagage Tracking Systeem Front-end (React)
> [/bagage-tracking-frontend](/bagage-tracking-frontend)

Dit is een simpele react app die de status en locatie bagage weergeeft. Het gebruikt websockets om veranderingen in de database door te krijgen van de server.

### Bagage Inlever Systeem (TODO - Python, Flask)
> TODO

> Een API met simpele front-end dat bagage aanneemt van passagiers en deze in het Bagage Tracking Systeem zet.



## Beveiliging


### Gebruikte technieken:
#### Bagage Tracking Systeem
- [X] Prepared statements tegen SQL injection
- [ ] Rate limiting
- [ ] separatie door firewalls (netwerk tekening maken en uitleggen)


Misschien toevoegen:
- [ ] Authenticatie?
- [ ] load balancing?
#### Bagage Inlever Systeem
- [ ] Rate limiting


### SQL injection (Bagage Tracking Systeem)
> TODO: uitleggen

### Rate limiting
> TODO: uitleggen en implementeren



