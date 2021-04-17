from pyrogram import Client
from config import Config


plugins = dict(root="plugins")


app = Client('GDrive-Bot',
        bot_token = Config.1779555807:AAH-Lb92tr99Ctbr7s_hNciBL9nM5GvX4c8,
        api_id = Config.5952297,
        api_hash = Config.f091a877e6760e4e51e0989531e3d430,
        plugins = plugins
      )


app.run()
