import requests, pendulum
from dhooks import Webhook, Embed
import sqlite3
from commands.lib.manage_db import manage_db


class EpicLib:
    def __init__(self):
        self.s = requests.session()

    def get_token_params(self):
        for i in range(len(self.activities)):
            if self.content[1].lower() in str(self.activities[i]['acti_title']).lower() and self.content[2].lower() in str(self.activities[i]['acti_title']).lower():
                self.scolaryear = self.activities[i]['scolaryear']
                self.codemodule = self.activities[i]['codemodule']
                self.codeinstance = self.activities[i]['codeinstance']
                self.codeacti = self.activities[i]['codeacti']
                self.codeevent = self.activities[i]['codeevent']
                print(self.scolaryear, self.codemodule, self.codeinstance, self.codeacti, self.codeevent)
                return True
        return False


    def send_token(self, sy, cm, ci, ca, ce):
        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
            'sec-ch-ua-platform': '"Linux"',
            'Origin': 'https://intra.epitech.eu',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://intra.epitech.eu/planning/',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        params = {
            'format': 'json',
        }

        data = {
            'token': str(self.content[3]),
            'rate': '0',
            'comment': '',
        }

        response = self.s.post(f'https://intra.epitech.eu/module/{sy}/{cm}/{ci}/{ca}/{ce}/token', headers=headers, params=params, data=data)


    def get_intra_activities(self):
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Referer': 'https://intra.epitech.eu/planning/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        today = pendulum.now()
        start = str(today.start_of('week').format('YYYY-MM-DD'))
        end = str(today.end_of('week').format('YYYY-MM-DD'))

        params = {
            'format': 'json',
            'start': start,
            'end': end,
        }

        response = self.s.get('https://intra.epitech.eu/planning/load', params=params, headers=headers)
        self.activities = response.json()

    async def epitech_login(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        self.s.get(self.loginlink, headers=headers)

    async def find_subject(self):
        for i in range(len(self.subject_activities)):
            if self.project.lower() in str(self.subject_activities[i]['acti_title']).lower():
                sy = self.subject_activities[i]['scolaryear']
                cm = self.subject_activities[i]['codemodule']
                ci = self.subject_activities[i]['codeinstance']
                ca = self.subject_activities[i]['codeacti']
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'none',
                    'Sec-Fetch-User': '?1',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }

                response = self.s.get(f'https://intra.epitech.eu/module/{sy}/{cm}/{ci}/{ca}/project/file/?format=json', headers=headers)
                embed = Embed(
                    title=f'{self.project}'.capitalize(),
                    url = f'https://intra.epitech.eu/module/{sy}/{cm}/{ci}/{ca}/project',
                    color = 0x206694,
                    timestamp = 'now'
                )
                for i in range(len(response.json())):
                    name = str(response.json()[i]["title"]).split('_')
                    name = name[len(name) - 1]
                    embed.add_field(name=name, value=f'[Direct link]({"https://intra.epitech.eu"+str(response.json()[i]["fullpath"])})', inline=False)
                return embed
        return False

    async def find_project(self):
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Referer': 'https://intra.epitech.eu/module/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        today = pendulum.now()
        start = str(today.start_of('week').format('YYYY-MM-DD'))
        end = str(today.end_of('week').format('YYYY-MM-DD'))
        params = {
            'format': 'json',
            'start': start,
            'end': end,
        }

        response = self.s.get('https://intra.epitech.eu/module/board/', params=params, headers=headers)
        self.subject_activities = response.json()
        print(self.project)

    async def get_student_stats(self):
        print('get_stdudent_stats')
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Referer': 'https://intra.epitech.eu/user/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
        }

        params = {
            'format': 'json',
        }

        response = self.s.get('https://intra.epitech.eu/user/', params=params, headers=headers)
        stats = response.json()
        embed = Embed(
            title = stats['title'],
            url = 'https://intra.epitech.eu/user/',
            color = 0x206694,
            timestamp = 'now'
        )
        embed.add_field(name='Credits', value=stats['credits'], inline=True)
        embed.add_field(name='GPA', value=stats['gpa'][0]['gpa'], inline=True)
        return embed

    async def reset_login_link_req(self):
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Origin': 'https://intra.epitech.eu',
            'Referer': 'https://intra.epitech.eu/admin/autolog',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
        }

        params = {
            'format': 'json',
        }

        response = self.s.post('https://intra.epitech.eu/admin/autolog/generate', params=params, headers=headers)
        self.newlogin = response.json()['autologin']

    async def get_project_subject(self, project, loginlink):
        self.project = project
        self.loginlink = loginlink
        await self.epitech_login()
        await self.find_project()
        embed = await self.find_subject()
        return embed

    async def get_student_infos(self, loginlink):
        self.loginlink = loginlink
        await self.epitech_login()
        return await self.get_student_stats()

    def validate_token(self, content, loginlink):
        self.loginlink = loginlink
        self.content = content
        self.epitech_login()
        self.get_intra_activities()
        if self.get_token_params() == False:
            return "params"
        # if self.send_token(self.scolaryear, self.codemodule, self.codeinstance, self.codeacti, self.codeevent) == False:
        #     return "token"

    async def reset_login_link(self, discord_id, loginlink, key):

        self.discord_id = discord_id
        self.loginlink = loginlink
        await self.epitech_login()
        await self.reset_login_link_req()
        manage_db(key=key).register_new_login_link(discord_id=discord_id, link=self.newlogin, discord_name=None)
