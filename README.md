Tesla_Insights_Pinnacle
Introduzione
Tesla_Insights_Pinnacle è il mio progetto finale che dimostra un approccio end-to-end nell’analisi dei dati e nello sviluppo di soluzioni di intelligenza artificiale. Utilizzando dati storici di TSLA, il progetto combina Data Engineering, Data Analysis, Machine Learning, Forecasting, Deep Learning e API AI per trasformare i dati in insight strategici. L’obiettivo è quello di offrire una panoramica completa, dalla raccolta dei dati alla creazione di dashboard interattive, passando per modelli predittivi e interpretabilità.

Caratteristiche Principali
Raccolta & Storage Dati: Download dei dati storici di TSLA (dal 30/06/2010 ad oggi), salvataggio in CSV e in un database SQLite.
Feature Engineering & EDA: Calcolo di indicatori tecnici (Daily Return, Medie Mobili, Volatilità, RSI) e analisi esplorativa con visualizzazioni dettagliate.
Modelli Predittivi e Forecasting:
RandomForest con tuning iperparametrico e ensemble avanzato (inclusi GradientBoosting e XGBoost).
Forecasting con Prophet per previsioni a 6 mesi.
Reti Neurali LSTM per la previsione delle serie temporali.
Interpretabilità del Modello: Utilizzo di SHAP per analizzare l’impatto delle feature sui modelli predittivi.
MLOps: Tracciamento degli esperimenti e salvataggio dei modelli con MLflow per garantire riproducibilità.
API AI: Implementazione di un’API con FastAPI che espone endpoint per analisi del sentiment e riassunti testuali.
Integrazione SQL e R: Caricamento dei dati in un database SQL e analisi avanzata in R tramite rpy2, con generazione di grafici statistici.
Dashboard Interattiva: Creazione di una dashboard con Plotly Dash, che permette una visualizzazione dinamica dei dati e l’esportazione in JSON per l’integrazione con Tableau Public.
Requisiti e Setup
Assicurati di avere Python 3, R e tutte le librerie elencate nel file requirements.txt. Segui le istruzioni per la creazione di un ambiente virtuale e l’installazione delle dipendenze. Sono necessarie configurazioni particolari per l’integrazione con R (impostazione del PATH e della codifica).

Esecuzione del Progetto
Data Engineering: Esegui lo script per caricare i dati da CSV e salvarli nel database SQLite.
EDA e Feature Engineering: Analizza i dati e genera i grafici per la valutazione dei trend.
Modellazione: Addestra e valuta i modelli predittivi (RandomForest, Prophet, LSTM) e visualizza i risultati.
Interpretabilità: Utilizza SHAP per comprendere l’importanza delle feature.
MLOps: Avvia MLflow per tracciare gli esperimenti e salvare i modelli.
API AI: Avvia il server FastAPI per esporre gli endpoint di NLP.
Dashboard: Avvia la dashboard con Plotly Dash per esplorare interattivamente i dati.
Contatti
Per maggiori informazioni e approfondimenti, visita il mio profilo LinkedIn: Raffaele Schiavone

Chi sono:
Data Scientist, AI Expert & Data Engineer | Creazione di Soluzioni AI e Dashboard di Business Intelligence | Oltre 70 aziende supportate in progetti di Digital Transformation

