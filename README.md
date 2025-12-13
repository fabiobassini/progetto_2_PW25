# 💧 Gestione Idrica - Distribuzione Acqua

![Python](https://img.shields.io/badge/Python-3.9.5-blue?style=flat&logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?style=flat&logo=django)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=flat&logo=mysql)

Applicazione web full-stack per la gestione del servizio idrico integrato. Permette la gestione di clienti, utenze, fatture e letture attraverso una dashboard moderna e un pannello di amministrazione.

---

## Prerequisiti

Prima di iniziare, assicurati di avere installato:

1.  **Git**: Per clonare la repository.
2.  **MySQL Server**: Il database relazionale.
3.  **Python 3.9.5**: Versione specifica richiesta per questo progetto.

---

## Guida all'Installazione (Step-by-Step)

### 1. Clona la repository
Apri il terminale (o PowerShell) e scarica il progetto:

```bash
git clone https://github.com/fabiobassini/progetto_2_pw25.git
cd progetto_2_pw25
```


### 2. Preparazione Ambiente Python (3.9.5)
Il progetto richiede Python 3.9.5. Segui le istruzioni per il tuo sistema operativo.



 macOS / Linux (Unix)
Se non hai Python 3.9.5, si consiglia di usare pyenv:

```bash
# Se usi pyenv
pyenv install 3.9.5
pyenv local 3.9.5

# Crea il virtual environment
python3 -m venv venv

# Attiva l'ambiente
source venv/bin/activate
```

 Windows
Assicurati di aver scaricato e installato Python 3.9.5 dal sito ufficiale e di aver selezionato "Add Python to PATH" durante l'installazione.

```bash 
# Crea il virtual environment
python -3.9 -m venv venv

# Attiva l'ambiente
.\venv\Scripts\activate
```

Verifica: Dopo l'attivazione, digitando 
```bash
python --version
``` 
dovresti vedere 
```bash
Python 3.9.5.
```

### 3. Installazione Dipendenze
Con l'ambiente virtuale attivo, installa le librerie necessarie (Django, MySQL driver, Dotenv):

```bash
pip install -r requirements.txt
```

### 4. Configurazione e Avvio Database MySQL
Devi assicurarti che il servizio MySQL sia attivo sul tuo computer.

 ### macOS

✅ Opzione 1 — Installazione Tramite DMG (la più semplice e stabile)
1. Vai alla pagina ufficiale: https://dev.mysql.com/downloads/mysql/
2. Scarica la versione MySQL Community Server (DMG Installer).
3. Apri il pacchetto .dmg e segui l’installer:
- Ti verrà chiesto di creare una password per l’utente root (conservala!)
- Verrai guidato nell’installazione del pannello di controllo MySQL.prefPane
4. Al termine troverai:
- MySQL installato
- Un pannello nelle Preferenze di Sistema per avviare/fermare il server

#### Avvio / Stop del server
- Dalle Preferenze di Sistema → MySQL → Start
- Oppure da terminale:
```bash
sudo /usr/local/mysql/support-files/mysql.server start
```
- Verifica:

```bash
mysql -u root -p
```


✅ Opzione 2 — Installazione con Homebrew (per chi usa brew)

Se preferisci usare Homebrew:
```bash
brew update
brew install mysql
```

Avvia il server:
```bash
brew services start mysql
```
Imposta la password root (solo al primo avvio):
```bash
mysql_secure_installation
```
 ### Linux (Ubuntu / Debian / Mint)

1. Installa MySQL Server
```bash
sudo apt update
sudo apt install mysql-server
```
2. Proteggi l’installazione e imposta password root
```bash
sudo mysql_secure_installation
```
3. Avvia il servizio
```bash
sudo service mysql start
```
4. Entra nella console MySQL
```bash
sudo mysql -u root -p
```

 ### Windows

1. Scarica il MySQL Installer: https://dev.mysql.com/downloads/installer/
2. Durante l’installazione seleziona:
- MySQL Server 8.0
- MySQL Workbench (facoltativo ma utile)
3. Al termine, MySQL si avvia automaticamente come servizio di Windows.

Avvio / Stop manuale
1. Premi Win + R
2. Scrivi: services.msc
3. Cerca “MySQL80”
4. Click destro → Start

Verifica:
Apri PowerShell:
```bash
mysql -u root -p
```

### 5. Configurazione Variabili d'Ambiente (.env)
Il progetto usa un file .env per gestire le password in sicurezza.

1. Copia il file di esempio:

```bash
# macOS/Linux
cp .env.example .env
# Windows
copy .env.example .env
```

2. Apri il file .env con un editor di testo e configura la password del tuo database MySQL locale:
```bash
DB_NAME=distribuzione_acqua
DB_USER=root
DB_PASSWORD=latuapassword  <-- INSERISCI QUI LA TUA PASSWORD MYSQL
DB_HOST=localhost
```


### 6. Inizializzazione Database (Automatica)
Esegui lo script per automatizzare la creazione del DB e delle tabelle. Esegui questi comandi in sequenza:

A. Crea il Database vuoto
Questo script si connette a MySQL e crea il DB distribuzione_acqua se non esiste.
```bash
python create_db.py
```

B. Crea la struttura (Tabelle)
Applica le migrazioni di Django per creare le tabelle (Cliente, Utenza, Fattura, Lettura).

```bash
python manage.py migrate
```

C. Popola con dati di prova
Carica i dati iniziali (Rossi Srl, Bianchi Spa, ecc.) per non partire da zero.

```bash
python manage.py loaddata initial_data.json
```

### 7. Creazione Utente Amministratore (Opzionale)
Per accedere al pannello di controllo completo (/admin), crea un superuser:

```bash
python manage.py createsuperuser
```

Inserisci username (es. admin), email (puoi lasciarla vuota) e password.

## ▶️ Avvio dell'Applicazione
Tutto è pronto! Avvia il server di sviluppo:

```bash
python manage.py runserver
```

Ora apri il browser e visita:

- Dashboard: http://127.0.0.1:8000
- Pannello Admin: http://127.0.0.1:8000/admin

## 🛠 Troubleshooting (Problemi Comuni)

***Errore: Access denied for user 'root'@'localhost'***
- Hai inserito una password sbagliata nel file .env. Controlla la tua password di MySQL.

***Errore: Can't connect to MySQL server***
- Il servizio MySQL non è avviato. Rivedi il Punto 4.
