from flask import Flask

from develop.controllers.abonent import abonent_route
from develop.controllers.panel import panel_route

from flask_principal import identity_loaded, UserNeed, RoleNeed
from flask_login import current_user

from develop.extentions import (
    login_manager,
    toolbar,
    assets_env,
    cache,
    moment,
    principal
)

from develop.models import (
    db,
    User
)

from flask_socketio import SocketIO
socketio = SocketIO()

def create_app(config_object):

    app = Flask(__name__)
    app.config.from_object(config_object)

    ######## Register Database ########

    db.init_app(app)
    # csrf.init_app(app)

    ######## Register Extentions ########

    login_manager.init_app(app)
    toolbar.init_app(app)
    assets_env.init_app(app)
    moment.init_app(app)
    principal.init_app(app)

    socketio.init_app(app)

    ######## Register Routes ########

    app.register_blueprint(abonent_route)
    app.register_blueprint(panel_route)

    # Identify the users roles
    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        # Set the identity user object
        identity.user = current_user

        # Add the UserNeed to the identity
        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        # Add each role to the identity
        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.name))

    return app
