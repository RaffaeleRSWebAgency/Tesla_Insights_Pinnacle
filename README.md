# Tesla_Insights_Pinnacle

![Tesla Logo](tesla_logo.png)

## Introduzione

**Tesla_Insights_Pinnacle** è un progetto finale che dimostra un approccio end-to-end nell’analisi dei dati e nello sviluppo di soluzioni di intelligenza artificiale. Realizzato da **Raffaele Schiavone**, il progetto integra competenze avanzate in Data Engineering, Data Analysis, Machine Learning, Forecasting, Deep Learning, API AI, SQL, Python e R. L'obiettivo è trasformare i dati storici di Tesla (TSLA) in insight strategici utili a investitori e manager, evidenziando la capacità di combinare diverse tecnologie e metodologie per una soluzione completa.

---

## Contenuti del Progetto

Il progetto copre le seguenti fasi:

1. **Setup e Configurazione**  
   - Creazione di un ambiente virtuale.
   - Installazione delle librerie necessarie (consultare il file `requirements.txt` per l’elenco completo).
   - Configurazione specifica (ad esempio, Developer Mode su Windows per supportare rpy2).

2. **Data Engineering & Raccolta Dati**  
   - Download dei dati storici di TSLA (dal 30/06/2010 ad oggi).
   - Salvataggio dei dati in formato CSV e successivo caricamento in un database SQLite (file `tesla.db`).
   - Gestione della connessione e salvataggio in una tabella SQL denominata `tsla_data`.

3. **Feature Engineering & Analisi Esplorativa (EDA)**  
   - Calcolo degli indicatori tecnici:  
     - **Daily Return**: variazione percentuale giornaliera basata sul prezzo di chiusura.  
     - **Medie Mobili (MA20, MA50)**: media mobile a 20 e 50 giorni per identificare trend di prezzo.  
     - **Volatilità**: deviazione standard dei rendimenti giornalieri su una finestra mobile.
     - **RSI (Relative Strength Index)**: indicatore di momentum che aiuta a identificare condizioni di ipercomprato o ipervenduto.
   - Visualizzazione grafica dei trend storici del prezzo e delle medie mobili.
   - Statistiche descrittive per un’analisi approfondita dei dati.

4. **Modelli Predittivi e Forecasting**

   ### 4.1 RandomForest ed Ensemble Avanzato
   - Suddivisione dei dati in training e test, mantenendo l'ordine temporale.
   - Tuning iperparametrico del modello RandomForest tramite GridSearchCV.
   - Creazione di un ensemble avanzato (VotingRegressor) che combina RandomForest, GradientBoosting e XGBoost.
   - Confronto visivo e valutazione delle performance tramite metriche come MSE (Mean Squared Error) e R².

   ### 4.2 Forecasting con Prophet
   - Preparazione dei dati per Prophet, rinominando le colonne (`date` in `ds` e `close` in `y`).
   - Addestramento del modello Prophet con stagionalità giornaliera.
   - Previsione del prezzo di chiusura per i prossimi 6 mesi e visualizzazione delle componenti (trend, stagionalità, ecc.).
   
   ### 4.3 Previsione con Reti Neurali (LSTM)
   - Costruzione di sequenze temporali a partire dalla serie storica del prezzo di chiusura.
   - Addestramento di un modello LSTM per la previsione basata su sequenze di 60 giorni.
   - Esempio di generazione di sequenze con dati normalizzati (MinMaxScaler o dati dummy).

5. **Interpretabilità del Modello con SHAP**  
   - Utilizzo di SHAP per interpretare il modello RandomForest.
   - Generazione di un summary plot per visualizzare l’impatto delle feature sui valori predetti.

6. **Integrazione MLOps con MLflow**  
   - Tracciamento degli esperimenti e salvataggio dei modelli.
   - Logging dei parametri, metriche e della signature del modello RandomForest.
   - Assicurare la riproducibilità degli esperimenti e il monitoraggio continuo delle performance.

7. **Integrazione API AI con FastAPI**  
   - Sviluppo di un’API AI che espone due endpoint fondamentali:
     - **POST /sentiment:** Per l’analisi del sentiment utilizzando il modello `nlptown/bert-base-multilingual-uncased-sentiment`.
     - **POST /summarize:** Per la generazione di riassunti, sfruttando il modello `sshleifer/distilbart-cnn-12-6`.
   - Avvio del server API con Uvicorn e test degli endpoint tramite richieste HTTP.

8. **Integrazione SQL e Analisi con R**  
   - Caricamento dei dati dal CSV in un database SQLite.
   - Utilizzo di `rpy2` per connettersi a R e svolgere analisi statistiche.
   - Esecuzione di script R per generare visualizzazioni, ad esempio un boxplot dei Daily Return, con gestione della codifica e del locale per caratteri accentati.

9. **Dashboard Interattiva con Plotly Dash**  
   - Creazione di una dashboard interattiva per la visualizzazione dinamica dei grafici (ad es. trend del prezzo di TSLA).
   - Esportazione dei dati in formato JSON per la successiva integrazione con Tableau Public tramite un Web Data Connector.
   - Codice eseguibile come script Python (`dashboard.py`).

10. **Report Finale e Conclusioni**  
    - Sintesi di tutte le fasi del progetto.
    - Approfondimenti sul tuning iperparametrico, l'ottimizzazione mediante tecniche di ensemble e l'integrazione di dati esterni (indicatori macroeconomici e feedback da API esterne).
    - Riflessioni sul valore strategico che la trasformazione dei dati in insight può avere per decisioni di business e investimenti.

---

## Requisiti

- **Linguaggi e Tecnologie:**  
  - Python 3  
  - R  
  - SQL (SQLite)

- **Librerie Python:**  
  - `yahooquery`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `xgboost`, `statsmodels`, `prophet`, `tensorflow`, `keras`, `fastapi`, `uvicorn`, `pydantic`, `mlflow`, `sqlalchemy`, `rpy2`, `tf-keras`, `plotly`, `dash`, `requests`

- **Ambiente R:**  
  - R 4.4.2 (o superiore)  
  - ggplot2

---

## Setup e Configurazione

1. **Ambiente Virtuale e Installazione delle Dipendenze:**  
   Creare un ambiente virtuale (ad es. con `venv` o `conda`) e installare le librerie necessarie con:
   ```bash
   pip install -r requirements.txt
## Configurazione di R e rpy2

- **Impostazione delle Variabili d’Ambiente:**  
  Impostare la variabile `R_HOME` e aggiornare `PATH` in modo che rpy2 trovi l’installazione di R.
  
- **Codifica:**  
  Verificare la corretta codifica (cp1252) per gestire i caratteri accentati in Windows.

- **Developer Mode (Windows):**  
  Abilitare Developer Mode se richiesto per supportare funzionalità avanzate (es. rpy2).

---

## Guida all'Esecuzione

1. **Data Engineering**  
   Eseguire lo script che carica i dati dal file `tsla_yahooquery.csv` e li salva in un database SQLite (`tesla.db`).

2. **Feature Engineering ed EDA**  
   Calcolare gli indicatori tecnici e generare grafici per analizzare trend e distribuzioni.

3. **Modellazione e Forecasting**  
   Addestrare e testare i modelli predittivi:
   - RandomForest con tuning ed ensemble.
   - Forecasting con Prophet.
   - Previsione con LSTM.  
   Visualizzare le performance e i confronti tra i modelli.

4. **Interpretabilità del Modello**  
   Utilizzare SHAP per visualizzare l'importanza delle feature e interpretare i risultati del modello RandomForest.

5. **MLOps**  
   Avviare MLflow per tracciare gli esperimenti, loggare parametri, metriche e salvare il modello.

6. **API AI**  
   Avviare l’API FastAPI per esporre gli endpoint di NLP:
   ```bash
   uvicorn api.ai_api:app --host 0.0.0.0 --port=8000 --reload
## Testare gli Endpoint

- Testare gli endpoint per sentiment analysis e summarization.

---

## Analisi con R

- Eseguire lo script che carica i dati in SQLite e li analizza con R tramite rpy2, generando il boxplot dei Daily Return.

---

## Dashboard Interattiva

- Avviare la dashboard eseguendo lo script `dashboard.py`:
  ```bash
  python dashboard.py
## Esplorazione e Verifica

- Esplorare i grafici interattivi e verificare l’esportazione dei dati in JSON.

---

## Contatti

Per ulteriori informazioni, approfondimenti o collaborazioni, visita il mio profilo LinkedIn:  
**Raffaele Schiavone**

**Chi sono:**  
Data Scientist, AI Expert & Data Engineer | Creazione di Soluzioni AI e Dashboard di Business Intelligence | Oltre 70 aziende supportate in progetti di Digital Transformation

---

## Conclusioni

**Tesla_Insights_Pinnacle** rappresenta un esercizio completo che unisce l’ingegneria dei dati, la modellazione predittiva, l’analisi interpretativa e l’integrazione di sistemi MLOps e API AI. Questo progetto evidenzia come l’integrazione di tecnologie avanzate possa trasformare dati grezzi in insight strategici, supportando decisioni di business e guidando la trasformazione digitale.

Buon lavoro e buona esplorazione dei dati!
