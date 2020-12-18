Spiegazione Lettore e Scrittore

Il problema dei lettori e scrittori è un classico problema di condivisione dell’informazione che richiede sincronizzazione. Abbiamo alcuni thread che accedono in sola lettura, i lettori, e altri che possono scrivere, quindi modificare che chiameremo scrittori.

Una delle possibili soluzioni che si possono adottare viene spiegata di seguito



Spiegazione Codice

La classe LettoriScrittori, presentata di seguito, risolve il problema dei
lettori e degli scrittori. Per semplicità la soluzione fa riferimento a due
lettori e a un solo scrittore, ma la soluzione con molti scrittori e molti 
lettori è praticamente identica: basta attivare più volte il processo lettore e
il processo scrittore.
Il programma utilizza i semafori scrivi e mutex. Il semaforo scrivi ha la scopo
di garantire l'accesso in mutua esclusione alle operazioni di scrittura e viene
usato sia dai lettori che dagli scrittori. Il semaforo mutex garantisce che
alcune operazioni di controllo dei processi lettori avvengano in mutua
esclusione, in particolare il conteggio dei lettori attivi, memorizzato nella
variabile intera lettori. Il valore 1 per la variabile lettori indica l'arrivo
del primo lettore, mentre il valore 0 per la stessa variabile indica che non ci
sono altri lettori.