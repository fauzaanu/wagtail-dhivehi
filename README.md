# Wagtail Dhivehi

A quick starter for wagtail-cms in dhivehi language.

Incase someone dont want to use this starter but want to get wagtail working for dhivehi the main settings changed are in the Internationalization section of `settings/base.py` or `settings.py`

```python
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "dv"
TIME_ZONE = "Indian/Maldives"
USE_I18N = True
USE_TZ = True
WAGTAIL_I18N_ENABLED = True
USE_L10N = True
WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
    ('dv', "Dhivehi"),
]
LANGUAGES_BIDI = ["dv"]
```

In addition to that this starter is setup with the same ideas of `fauzaanu/onlydjango` + allauth-ui and a signal that automatically makes the first user a superadmin.


To help with the translation of wagtail into Dhivehi: https://app.transifex.com/torchbox/wagtail/translate/#dv

## DB setup in development

```bash
sudo docker rm -f $(sudo docker ps -aq) && sudo docker compose -f dev.docker-compose.yml up -d
```

You also need to mv .sample_env into .env
