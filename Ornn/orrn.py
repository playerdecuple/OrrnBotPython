import discord
import os
import random

class orrnMain(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    
    async def on_message(self, message):
        
        user = message.author
        guild = message.guild
        tc = message.channel

        if message.content.startswith(':') == False:
            return
        else:
            msg = message.content[1:]

        args = msg.split(" ")

        if message.author == client.user:
            return
            
        if len(args) < 1:
            return
        else :
            if user.bot:
                return
            
            if args[0] == "무기":
                
                weaponNamePath = str(user.id) + "weaponName.txt"
                weaponReinforcePath = str(user.id) + "weaponReinforce.txt"

                if args[1] == "제작" or args[1] == "생성":
                    if os.path.isfile(weaponNamePath): return

                    weapon = open(weaponNamePath, 'w')
                    weapon.write(str(args[2:]).replace('\'', '').replace('[', '').replace(']', ''))
                    weapon.close()
                    await tc.send(str(args[2:]).replace('\'', '').replace('[', '').replace(']', '') + '(이)라는 무기를 만들었습니다!')

                    ## v1.0.1 : 무기 강화수치 파일 만들기
                    weaponReinforce = open(weaponReinforcePath, 'w')
                    weaponReinforce.write(str(1))
                    weaponReinforce.close()
                    return
                if args[1] == "파괴" or args[1] == "삭제":
                    if not(os.path.isfile(weaponNamePath)): return

                    weapon = open(weaponNamePath, 'rt')
                    weaponName = weapon.readline
                    await tc.send(weaponName() + " 무기를 파괴했습니다..")
                    weapon.close()
                    os.remove(weaponNamePath)
                    os.remove(weaponReinforcePath)
                    return
                if args[1] == "강화":
                    weaponReinforcePath = str(user.id) + "weaponReinforce.txt"
                    if not(os.path.isfile(weaponNamePath)): return

                    weaponNameFile = open(weaponNamePath, 'rt')
                    weaponName = weaponNameFile.readline

                    wN = weaponName()

                    weaponReinforceFile = open(weaponReinforcePath, 'rt')
                    weaponReinforce = weaponReinforceFile.read

                    wR = weaponReinforce()

                    rd = random.random

                    if rd() > (1 / float(wR) * 7):
                        await tc.send('이런, 강화에 실패했습니다.')
                        return
                    else:
                        await tc.send(wN + " 무기가 " + str(int(wR) + 1) + "성으로 강화되었습니다!")

                        weaponReinforceWrite = open(weaponReinforcePath, 'w')
                        weaponReinforceWrite.write(str(int(int(wR) + 1)))
                        weaponReinforceWrite.close()

                        weaponReinforceFile.close()

                        weaponNameFile.close()



    
client = orrnMain()
client.run('NzQ3NjY1MzgzOTI1ODc0Nzc5.X0SLpg.9M9uwL9K63Xg_-zymtP3meRwFdI')