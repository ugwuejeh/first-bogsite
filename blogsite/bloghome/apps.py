from django.apps import AppConfig


class BloghomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bloghome'
    
    def ready(self):
        import bloghome.signals
