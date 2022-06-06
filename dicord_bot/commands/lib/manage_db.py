import sqlite3, requests
from cryptography.fernet import Fernet
from dhooks import Embed


class manage_db:
    def __init__(self, key):
        self.db = 'database.db'
        if key is not None:
            self.f = Fernet(key)

    async def set_command_status(self, command=str, active=int):
        database = sqlite3.connect('database.db')
        cursor = database.cursor()
        req = "update commands set active = ? WHERE command = ?"
        cursor.execute(req, (active, command))
        database.commit()
        database.close()

    async def get_command_status(self, command=str):
        database = sqlite3.connect('database.db')
        cursor = database.cursor()
        req = "select * from commands"
        cursor.execute(req)
        for row in cursor:
            if command == row[0]:
                database.close()
                return row[1]
        database.close()
        return None

    async def get_all_command_status(self):
        embed = Embed(title='Commands status', color=0xf1c40f, timestamp='now')
        database = sqlite3.connect('database.db')
        cursor = database.cursor()
        req = "select * from commands"
        cursor.execute(req)
        for row in cursor:
            val = row[1]
            if int(val) == 1:
                embed.add_field(name=str(row[0]).capitalize(), value='Enabled', inline=True)
            else:
                embed.add_field(name=str(row[0]).capitalize(), value='Disabled', inline=True)
        database.close()
        return embed

    def is_link_valid(self, link=str):
        if link.startswith('https://intra.epitech.eu/auth-'):
            if requests.get(link).status_code == 200:
                return True
        return False

    def is_login_link_updated(self, discord_id=str):
        database = sqlite3.connect('database.db')
        cursor = database.cursor()
        req = "select * from loginlinks"
        cursor.execute(req)
        for row in cursor:
            if discord_id == row[0]:
                database.close()
                return True
        database.close()
        return False

    def get_login_link(self, discord_id=str):
        print(discord_id)
        database = sqlite3.connect('database.db')
        cursor = database.cursor()
        req = "select * from loginlinks"
        cursor.execute(req)
        for row in cursor:
            if discord_id == row[0]:
                database.close()
                return self.f.decrypt(str(row[1]).encode()).decode()
        database.close()
        return None

    def register_new_login_link(self, discord_id=str, link=str, discord_name=str):
        link = (self.f.encrypt(link.encode())).decode()
        if self.is_login_link_updated(discord_id) == True:
            database = sqlite3.connect('database.db')
            cursor = database.cursor()
            req = "update loginlinks set login_link = ? WHERE discord_user_id = ?"
            cursor.execute(req, (link, discord_id))
            database.commit()
            database.close()
        else:
            database = sqlite3.connect('database.db')
            cursor = database.cursor()
            req = f"insert into loginlinks (discord_user_id, login_link, discord_name) values ('{discord_id}', '{link}', '{discord_name}')"
            cursor.execute(req)
            database.commit()
            database.close()