# settings_local.py

# Clé secrète
SECRET_KEY = 'votre_clé_secrète'

# Informations de base de données
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'votre_base_de_données',
        'USER': 'votre_utilisateur',
        'PASSWORD': 'votre_mot_de_passe',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Autres informations sensibles
API_KEY = 'votre_clé_d_api'
