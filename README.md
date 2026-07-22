<p align="center">
  <img src="app/static/img/logo.png" alt="shot-url logo" width="120">
</p>

<h1 align="center">shot-url</h1>

<p align="center">
  Une solution open-source pour raccourcir et gérer vos liens (LinkedIn, YouTube, etc.) en toute sérénité.
</p>

---

## ✨ Fonctionnalités

- 🔗 **Raccourcissement d'URL** — génère un lien court unique (hash MD5 encodé en base64) à partir de n'importe quelle URL
- 👤 **Authentification** — inscription et connexion des utilisateurs (mots de passe hashés avec bcrypt)
- 📊 **Suivi des clics** — chaque lien conserve un compteur de clics (`nb_click`)
- 🖥️ **Tableau de bord** — interface pour créer et visualiser ses liens
- 🔳 **Génération de QR code** — *(prévu, pas encore implémenté)*

## 🛠️ Stack technique

| Composant       | Technologie                                      |
|-----------------|---------------------------------------------------|
| Backend         | [Flask](https://flask.palletsprojects.com/) via [APIFlask](https://apiflask.com/) |
| Base de données | SQLAlchemy + Flask-Migrate (Alembic) — SQLite par défaut |
| Authentification| Flask-Login, Flask-Bcrypt, Flask-JWT-Extended     |
| Formulaires     | Flask-WTF / WTForms                               |
| Frontend        | Templates Jinja2, Tailwind CSS + DaisyUI, HTMX     |
| Déploiement     | Docker, Gunicorn                                  |

## 📁 Structure du projet

```
shot-url/
├── app/
│   ├── model/        # Modèles SQLAlchemy (User, Url)
│   ├── view/          # Blueprints (auth, url, main)
│   ├── templates/      # Templates Jinja2
│   ├── static/         # CSS (Tailwind), images
│   ├── form.py         # Formulaires WTForms
│   ├── utils.py        # Logique de raccourcissement d'URL
│   └── __init__.py     # Factory de l'application (create_app)
├── migrations/        # Migrations de base de données (Alembic)
├── config.py          # Configuration (dev / prod)
├── main.py            # Point d'entrée de l'application
└── requirement.txt     # Dépendances Python
```

## 🚀 Installation

### Prérequis

- Python >= 3.14
- Node.js (pour compiler le CSS avec Tailwind)

### 1. Cloner le dépôt

```bash
git clone https://github.com/jjk361282-beep/shot-url.git
cd shot-url
```

### 2. Installer les dépendances Python

**Avec pip :**

```bash
python -m venv .venv
. .venv/bin/activate       # sous Windows : .venv\Scripts\activate
pip install -r requirement.txt
```

**Avec uv :**

```bash
uv sync
```

### 3. Configurer les variables d'environnement

Copiez le fichier d'exemple et complétez-le :

```bash
cp .env.example .env
```

```env
DATABASE_URL=
JWT_SECRET=
SECRET_KEY=
APP_ENV=dev
```

### 4. Initialiser la base de données

```bash
flask db upgrade
```

### 5. Compiler les styles (Tailwind CSS)

```bash
npm install
npm run css
```

### 6. Lancer l'application

```bash
flask run
```

L'application est accessible sur `http://127.0.0.1:5000`.

## 🐳 Docker

```bash
docker build -t shot-url .
docker run -p 5000:5000 shot-url
```

## 🗺️ Roadmap

- [ ] Génération de QR code pour chaque lien raccourci
- [ ] Statistiques avancées (clics par jour, provenance, etc.)
- [ ] Expiration automatique des liens (`date_expirate` déjà présent dans le modèle)
- [ ] API publique documentée (APIFlask/OpenAPI)

## 🤝 Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## 📄 Licence

Aucune licence n'est actuellement définie pour ce projet.