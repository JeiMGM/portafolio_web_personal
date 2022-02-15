from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
    verbose_name="Portafolio" 
    #nota si se cambia el verbose name, como es una configuracion extendida se debe colocar en installed apps asi ej:"portfolio.apps.PortfolioConfig",
    #nota el verbose name hace que se muestre distinto en el panel admin