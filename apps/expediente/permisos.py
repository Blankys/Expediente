class Permisos:
    def solo_admin(user):
        if user:
            return user.groups.filter(name='Administrador').count() > 0
        return False

    def medico_denegado(user):
        if user:
            return user.groups.filter(name='Medico').count() == 0
        return False
