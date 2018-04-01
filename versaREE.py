import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import asyncio
import random
import time
from datetime import datetime


now = datetime.now()
server = discord.Server
Client = discord.Client()
client = commands.Bot(command_prefix = "$")

def isVowel(char):
    if char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u':
        return True
    else:
        return False

def is_me(m):
    print("ree")
    return m.author == client.user

def is_fred(m):
    return m.author.id == "184405311681986560"




@client.event
async def on_ready():
    print("REEEEEEEEE")
    
    
#serv = Client.get_server(
#chann = ge
#temp = await client.send_message(message.channel, ".")
#bot = temp.author
#await client.remove_message
#apr_f_temp = 0

bot_id = "428981357440532482"


@client.event
async def on_message(message):

#encryptor/decryptor program
    if message.author.id != "428981357440532482" and message.author.id != "154075805775822848":

        #april fools

        if True == False:
            nick = message.author.display_name
            #avi = message.author.avatar
            serv = message.author.server
            me = serv.get_member("270022629174280192")
            bot_user = serv.get_member(bot_id)
            #c_avi = me.avatar
            await client.change_nickname(bot_user, nick)
            #await client.edit_profile(avatar=avi)
            await client.delete_message(message)
            apr_message = message.content[::-1]
            await client.send_message(message.channel, apr_message)
            await client.change_nickname(bot_user, "APRIL FUCKING FOOLS")
            #await client.edit_profile(avatar=c_avi)
        if message.content == "april start":
            april_work = 1
        elif message.content == "april stop":
            april_work = 0

        surefire = 0
        entry = 0
        order = 0
        print(str(message.author.id) + ": " + str(message.content))
        if message.content[:8] == "encrypt ":
            statement = message.content[8:]
            length = len(statement)
            while length > 0:
                raw_letter = statement[order]
                order += 1
                if not raw_letter.isalpha():
                    raw_num = raw_letter
                elif raw_letter.isupper():
                    raw_num = raw_letter
                else:
                    numbah = ord(raw_letter) + 5
                    if numbah > 122:
                        numbah -= 26
                    raw_num = chr(numbah)
                if entry == 0:
                    final = raw_num
                    entry = 1
                else: final = final + raw_num
                length -= 1
            await client.delete_message(message)
            await client.send_message(message.channel, final)
        if message.content[:8] == "decrypt ":
            statement = message.content[8:]
            length = len(statement)
            while length > 0:
                raw_letter = statement[order]
                order += 1
                if not raw_letter.isalpha():
                    raw_num = raw_letter
                elif raw_letter.isupper():
                    raw_num = raw_letter
                else:
                    numbah = ord(raw_letter) - 5
                    if numbah < 97:
                        numbah += 26
                    raw_num = chr(numbah)
                if entry == 0:
                    final = raw_num
                    entry = 1
                else: final = final + raw_num
                length -= 1
            await client.delete_message(message)
            await client.send_message(message.channel, final)

    #ree/REE program

        if message.content[:3] == "ree":
            await client.send_message(message.channel, "http://www.stickpng.com/assets/images/58486a72849cf46a2a931338.png")
        if message.content[:21] == "<@270022629174280192>":
            await client.send_message(message.channel, "leave me the fuck alone bitch")
        elif message.content[-21:] == "<@270022629174280192>":
            await client.send_message(message.channel, "leave me the fuck alone bitch")
        if message.content[:3] == "REE":
            await client.send_message(message.channel, "https://img.fireden.net/tg/image/1458/54/1458542400677.jpg")

    #
    #adorable kitty gifs!!
    #

    #for at the beginning of the message:
            
        if message.content.lower()[:5] == "pussy":
            kitty = random.randint(1,10)
            if kitty == 1:
                await client.send_message(message.channel, "https://media2.giphy.com/media/TA6Fq1irTioFO/giphy.gif")
            elif kitty == 2:
                await client.send_message(message.channel, "https://media3.giphy.com/media/VxbvpfaTTo3le/giphy.gif")
            elif kitty == 3:
                await client.send_message(message.channel, "https://media3.giphy.com/media/11hKUEMqvFVHwI/giphy.gif")
            elif kitty == 4:
                await client.send_message(message.channel, "https://media0.giphy.com/media/cfuL5gqFDreXxkWQ4o/giphy.gif")
            elif kitty == 5:
                await client.send_message(message.channel, "https://media1.giphy.com/media/5exwXWg9u7yow/giphy.gif")
            elif kitty == 6:
                await client.send_message(message.channel, "https://media0.giphy.com/media/YxA2PPkXbwRTa/giphy.gif")
            elif kitty == 7:
                await client.send_message(message.channel, "https://media2.giphy.com/media/3xz2BrtIc89HzgFiBG/giphy.gif")
            elif kitty == 8:
                await client.send_message(message.channel, "https://media0.giphy.com/media/LMn7PRCVDcnvO/giphy.gif")
            elif kitty == 9:
                await client.send_message(message.channel, "https://media1.giphy.com/media/yLxS1bC7Lx23S/giphy.gif")
            elif kitty == 10:
                await client.send_message(message.channel, "https://images.sex.com/images/pinporn/2015/12/16/620/14558051.gif")

    #for at the end of the message:
                
        elif message.content.lower()[-5:] == "pussy":
            kitty = random.randint(1,10)
            if kitty == 1:
                await client.send_message(message.channel, "https://media2.giphy.com/media/TA6Fq1irTioFO/giphy.gif")
            elif kitty == 2:
                await client.send_message(message.channel, "https://media3.giphy.com/media/VxbvpfaTTo3le/giphy.gif")
            elif kitty == 3:
                await client.send_message(message.channel, "https://media3.giphy.com/media/11hKUEMqvFVHwI/giphy.gif")
            elif kitty == 4:
                await client.send_message(message.channel, "https://media0.giphy.com/media/cfuL5gqFDreXxkWQ4o/giphy.gif")
            elif kitty == 5:
                await client.send_message(message.channel, "https://media1.giphy.com/media/5exwXWg9u7yow/giphy.gif")
            elif kitty == 6:
                await client.send_message(message.channel, "https://media0.giphy.com/media/YxA2PPkXbwRTa/giphy.gif")
            elif kitty == 7:
                await client.send_message(message.channel, "https://media2.giphy.com/media/3xz2BrtIc89HzgFiBG/giphy.gif")
            elif kitty == 8:
                await client.send_message(message.channel, "https://media0.giphy.com/media/LMn7PRCVDcnvO/giphy.gif")
            elif kitty == 9:
                await client.send_message(message.channel, "https://media1.giphy.com/media/yLxS1bC7Lx23S/giphy.gif")
            elif kitty == 10:
                await client.send_message(message.channel, "https://images.sex.com/images/pinporn/2015/12/16/620/14558051.gif")

    #auto-reactions specific to selected users
                
        if message.author.id == "165643480964661259":
            rand = random.randint(1,18)
            if rand == 1:
                await client.add_reaction(message, "\U0001F1EB")
                await client.add_reaction(message, "\U0001F1E6")
                await client.add_reaction(message, "\U0001F1EC")
                await client.add_reaction(message, "\U0001F602")
        if message.author.id == "332208526552334336":
            rand = random.randint(1,18)
            if rand == 1:
                await client.add_reaction(message, "\U0001F1EB")
                await client.add_reaction(message, "\U0001F1E6")
                await client.add_reaction(message, "\U0001F1EC")
                await client.add_reaction(message, "\U0001F602")
        if message.author.id == "168842662516883456":
            rand = random.randint(1,18)
            if rand == 1:
                await client.add_reaction(message, "\U0001F1EB")
                await client.add_reaction(message, "\U0001F1E6")
                await client.add_reaction(message, "\U0001F1EC")
                await client.add_reaction(message, "\U0001F602")
        if message.author.id == "239959517444571136":
            await client.add_reaction(message, "\U0001F493")
        if message.author.id == "199964351451365377":
            await client.add_reaction(message, "\U0001F346")
        if message.author.id == "211867840628654081":
            alien = random.randint(1,50)
            if alien == 1:
                await client.add_reaction(message, "\U0001F914")
        if message.author.id == "152236460483805184":
            anthony = random.randint(1,18)
            if anthony == 1:
                await client.add_reaction(message, "\U0001F914")
        



    #the GOLDEN KAPPA


        golden_kappa = random.randint(1,2000)
        if golden_kappa == 1:
            await client.add_reaction(message, "\:golden_kappa:429107313723310091")
            await client.send_message(message.channel, "THE GOLDEN KAPPA HAS APPEARED! (0.05% probability!)")

    #no u auto-response
            
        if message.content[:10] == "ur mom gay":
            await client.send_message(message.channel, "no u")
        elif message.content[-10:] == "ur mom gay":
            await client.send_message(message.channel, "no u")
        elif message.content[:12] == "your mom gay":
            await client.send_message(message.channel, "no u")
        elif message.content[-12:] == "your mom gay":
            await client.send_message(message.channel, "no u")
        elif message.content[:6] == "ur gay":
            await client.send_message(message.channel, "no u")
        elif message.content[-6:] == "ur gay":
            await client.send_message(message.channel, "no u")
        elif message.content[:10] == "you're gay":
            await client.send_message(message.channel, "no u")
        elif message.content[-10:] == "you're gay":
            await client.send_message(message.channel, "no u")
        elif message.content[:3] == "gay":
            await client.send_message(message.channel, "no u")
        elif message.content[-3:] == "gay":
            await client.send_message(message.channel, "no u")

    #no u squared to a no u auto-response

        if message.content[:4] == "no u":
            if not message.author.id == "428981357440532482":
                entry = 1
                s_check = 4
                if message.content[:5] == "no u¹" or message.content[:5] == "no u²" or message.content[:5] == "no u³" or message.content[:5] == "no u⁴" or message.content[:5] == "no u⁵" or message.content[:5] == "no u⁶" or message.content[:5] == "no u⁷" or message.content[:5] == "no u⁸" or message.content[:5] == "no u⁹" or message.content[:5] == "no u⁰":
                    s_check = 4
                    raw_num = str()
                    print(len(message.content))
                    while not len(message.content) <= s_check:
                        if message.content[s_check] ==  "¹" or message.content[s_check] == "²" or message.content[s_check] == "³" or message.content[s_check] == "⁴" or message.content[s_check] == "⁵" or message.content[s_check] == "⁶" or message.content[s_check] == "⁷" or message.content[s_check] == "⁸" or message.content[s_check] == "⁹" or message.content[s_check] == "⁰":
                            if message.content[s_check] == "¹":
                                if entry == 1:
                                    raw_num = "1"
                                    entry = 0
                                else:
                                    raw_num = raw_num + "1"
                                s_check += 1
                            elif message.content[s_check] == "²":
                                if entry == 1:
                                    raw_num = "2"
                                    entry = 0
                                else:
                                    raw_num = raw_num + "2"
                                s_check += 1
                            elif message.content[s_check] == "³":
                                if entry == 1:
                                    raw_num = "3"
                                    entry = 0
                                else:
                                    raw_num = raw_num + "3"
                                s_check += 1
                            elif message.content[s_check] == "⁴":
                                if entry == 1:
                                    raw_num = "4"
                                    entry = 0
                                else:
                                    raw_num = raw_num + "4"
                                s_check += 1
                            elif message.content[s_check] == "⁵":
                                if entry == 1:
                                    raw_num = "5"
                                    entry = 0
                                else:
                                    raw_num = raw_num + "5"
                                s_check += 1
                            elif message.content[s_check] == "⁶":
                                if entry == 1:
                                    raw_num = "6"
                                    entry = 0
                                else:
                                    raw_num = raw_num + "6"
                                s_check += 1
                            elif message.content[s_check] == "⁷":
                                if entry == 1:
                                    raw_num = "7"
                                    entry = 0
                                else:
                                    raw_num = raw_num + "7"
                                s_check += 1
                            elif message.content[s_check] == "⁸":
                                if entry == 1:
                                    raw_num = "8"
                                    entry = 0
                                else:
                                    raw_num = raw_num + "8"
                                s_check += 1
                            elif message.content[s_check] == "⁹":
                                if entry == 1:
                                    raw_num = "9"
                                    entry = 0
                                else:
                                    raw_num = raw_num + "9"
                                s_check += 1
                            elif message.content[s_check] == "⁰":
                                if entry == 1:
                                    raw_num = "0"
                                    entry = 0
                                else:
                                    raw_num = raw_num + "0"
                                s_check += 1
                            print(raw_num)
                            print(s_check)
                    print(raw_num)
                    raw_num = int(raw_num) + 1
                    raw_num = str(raw_num)
                    r_check = 0
                    entry2 = 1
                    final = str()
                    while  r_check < len(raw_num):
                        if raw_num[r_check] == "0":
                            if entry2 == 1:
                                final = "⁰"
                                entry2 = 0
                            else:
                                final = final + "⁰"
                            r_check += 1
                        elif raw_num[r_check] == "1":
                            if entry2 == 1:
                                final = "¹"
                                entry2 = 0
                            else:
                                final = final + "¹"
                            r_check += 1
                        elif raw_num[r_check] == "2":
                            if entry2 == 1:
                                final = "²"
                                entry2 = 0
                            else:
                                final = final + "²"
                            r_check += 1
                        elif raw_num[r_check] == "3":
                            if entry2 == 1:
                                final = "³"
                                entry2 = 0
                            else:
                                final = final + "³"
                            r_check += 1
                        elif raw_num[r_check] == "4":
                            if entry2 == 1:
                                final = "⁴"
                                entry2 = 0
                            else:
                                final = final + "⁴"
                            r_check += 1
                        elif raw_num[r_check] == "5":
                            if entry2 == 1:
                                final = "⁵"
                                entry2 = 0
                            else:
                                final = final + "⁵"
                            r_check += 1
                        elif raw_num[r_check] == "6":
                            if entry2 == 1:
                                final = "⁶"
                                entry2 = 0
                            else:
                                final = final + "⁶"
                            r_check += 1
                        elif raw_num[r_check] == "7":
                            if entry2 == 1:
                                final = "⁷"
                                entry2 = 0
                            else:
                                final = final + "⁷"
                            r_check += 1
                        elif raw_num[r_check] == "8":
                            if entry2 == 1:
                                final = "⁸"
                                entry2 = 0
                            else:
                                final = final + "⁸"
                            r_check += 1
                        elif raw_num[r_check] == "9":
                            if entry2 == 1:
                                final = "⁹"
                                entry2 = 0
                            else:
                                final = final + "⁹"
                            r_check += 1
                        else:
                            r_check += 1
                        print(final)
                    await client.send_message(message.channel, "no u" + final)
                        
                else:
                    await client.send_message(message.channel, "no u²")
        elif message.content[-4:] == "no u":
            if not message.author.id == "428981357440532482":
                await client.send_message(message.channel, "no u ²")


    #turns any text into aNy TeXt

        if message.content[0] == ".":
            trigger = 0
            entry = 0
            raw = message.content.lower()[1:]

            while raw[0] == ".":
                raw = raw[1:]
            length = len(raw)
            while length > 0:
                if trigger == 0:
                    if raw[0].isalpha():
                        trigger = 1
                        if entry == 0:
                            final = raw[0]
                            entry += 1
                        else:
                            final = final + raw[0]
                    else:
                        if entry == 0:
                            final = raw[0]
                            entry += 1
                        else:
                            final = final + raw[0]
                else:
                    if raw[0].isalpha():
                        trigger = 0
                        if entry == 0:
                            final = raw.upper()[0]
                            entry += 1
                        else:
                            final = final + raw.upper()[0]
                    else:
                        if entry == 0:
                            final = raw[0]
                            entry += 1
                        else:
                            final = final + raw[0]
                raw = raw[1:]
                length -= 1
            await client.send_message(message.channel, final)



        if message.content[:2] == "b_":
            trigger = 1
            final = str()
            entry = 1
            raw = message.content[2:]
            await client.delete_message(message)
            length = len(raw)
            while length > 0:
                char = raw[0]
                if trigger == 1:
                    trigger = 0
                    if not isVowel(char):
                        if entry == 1:
                            final = "\U0001F171"
                            entry = 0
                        else:
                            final = final + "\U0001F171"
                    else:
                        if entry == 1:
                            final = char
                            entry = 0
                        else:
                            final = final + char
                elif char == " ":
                    trigger = 1
                    final = final + " "
                else:
                    if entry == 1:
                        final = char
                        entry = 0
                    else:
                        final = final + char
                raw = raw[1:]
                length -= 1
            await client.send_message(message.channel, final)


    #auto 'kappa' response


        if message.content.lower()[:5] == "kappa":
            await client.send_message(message.channel, "https://pbs.twimg.com/media/CVz0ZTeWoAAVCXo.jpg:large")
        elif message.content.lower()[-5:] == "kappa":
            await client.send_message(message.channel, "https://pbs.twimg.com/media/CVz0ZTeWoAAVCXo.jpg:large")

    #auto 'bamboozled' response

        if message.content.lower()[:10] == "bamboozled":
            await client.send_message(message.channel, "https://media1.tenor.com/images/a83cf8a4ff8fce40eaa8392314ce9a74/tenor.gif?itemid=10384533")
        elif message.content.lower()[-10:] == "bamboozled":
            await client.send_message(message.channel, "https://media1.tenor.com/images/a83cf8a4ff8fce40eaa8392314ce9a74/tenor.gif?itemid=10384533")



#auto 'lul' response

        if message.content.lower()[:8] == "omegalul":
            await client.send_message(message.channel, "https://ih1.redbubble.net/image.364225782.1573/flat,800x800,070,f.jpg")
        elif message.content.lower()[-8:] == "omegalul":
            await client.send_message(message.channel, "https://ih1.redbubble.net/image.364225782.1573/flat,800x800,070,f.jpg")

        elif message.content.lower()[:3] == "lul":
            await client.send_message(message.channel, "https://ih1.redbubble.net/image.481229447.9121/flat,800x800,075,f.u1.jpg")
        elif message.content.lower()[-3:] == "lul":
            await client.send_message(message.channel, "https://ih1.redbubble.net/image.481229447.9121/flat,800x800,075,f.u1.jpg")





    #definitely not cyber bullying


        if message.content.lower()[:4] == "http":
            if message.author.id == "211867840628654081":
                await client.add_reaction(message, "\U0001F644")
                await client.send_message(message.channel, "oh boy, he's sendin links again.. ⁽ⁿᵒᵗ ᵗᵒˣᶦᶜ ᵗʰᵒ⁾")


    #delete all the bots messages

        if message.content.lower() == "clear":
            if message.author.id == "129457966901362689" or message.author.id == "152236460483805184" or message.author.id == "239515551867600896" or message.author.id == "270022629174280192":
                print("starting")
                deleted = await client.purge_from(message.channel, limit=100, check=is_me)
                await client.send_message(channel, 'Deleted {} message(s)'.format(len(deleted)))

        if message.content.lower()[:2] == ";;":
            time.sleep(30)
            await client.delete_message(message)
        elif message.author.id == "184405311681986560":
            time.sleep(30)
            await client.delete_message(message)

        if message.content == "secret delete command hehe":
            await client.delete_channel(message.channel)



        if message.content == "APRIL FOOLS BITCHES":
            await client.edit_server(message.author.server, name = "aneeG fo htlaewnommoC")
            geezy = message.author.server.get_member("213033406408294400")
            await client.change_nickname(geezy, "yzeeGi")
            dom = message.author.server.get_member("239519276279529473")
            await client.change_nickname(dom, "xaf ytlas mi")
            kh3 = message.author.server.get_member("165643480964661259")
            await client.change_nickname(kh3, "..gnol oot gnikat si 3HK")
            ybl = message.author.server.get_member("167438425534758912")
            await client.change_nickname(ybl, "ycageLraeBihsoY")
            ybl2 = message.author.server.get_member("332208526552334336")
            await client.change_nickname(ybl2, "2ycageLraeBihsoY")
            baze = message.author.server.get_member("244943372786204673")
            await client.change_nickname(baze, "ezaB")
            rob = message.author.server.get_member("192107050170449920")
            await client.change_nickname(rob, "luoscoD")
            deku = message.author.server.get_member("168842662516883456")
            await client.change_nickname(deku, "xaf daer tnac i")
            matt = message.author.server.get_member("155807079272153088")
            await client.change_nickname(matt, "edomemag tseb lla rof nauj")
            anth = message.author.server.get_member("152236460483805184")
            await client.change_nickname(anth, "nilgnuoY")
            vers = message.author.server.get_member("270022629174280192")
            await client.change_nickname(vers, "aerok tseb aerok htron")
            dad = message.author.server.get_member("247852652019318795")
            await client.change_nickname(dad, "toB daD")
            ali2 = message.author.server.get_member("271805949960781835")
            await client.change_nickname(ali2, "2-24toboRneilA")
            fty = message.author.server.get_member("342447674928136204")
            await client.change_nickname(fty, "RVS epyt-F")
            ali = message.author.server.get_member("211867840628654081")
            await client.change_nickname(ali, "xaf gniyonna mi")
            adr = message.author.server.get_member("393531600702537729")
            await client.change_nickname(adr, "not ok")
            imy = message.author.server.get_member("170269007037857793")
            await client.change_nickname(imy, "xitsyMi")
            saif = message.author.server.get_member("154075805775822848")
            await client.change_nickname(saif, "rydoG ehT")
            melee = message.author.server.get_member("185915115642683392")
            await client.change_nickname(melee, "u on")
            fred = message.author.server.get_member("184405311681986560")
            await client.change_nickname(fred, "♪♪taoBderF")
            general = message.author.server.get_channel("353687505121312771")
            await client.edit_channel(general, name="lareneg")
            general = message.author.server.get_channel("353687505121312771")
            await client.edit_channel(general, topic="ecalp lufituaeb tey ,ylgu na si dlrow ehT")
            memes = message.author.server.get_channel("428770933629517825")
            await client.edit_channel(memes, name="semem")
            games = message.author.server.get_channel("416411424424722452")
            await client.edit_channel(games, name="semag")
            nsfw = message.author.server.get_channel("417178552962646028")
            await client.edit_channel(nsfw, name="wfsn")
            v_gen = message.author.server.get_channel("353687505121312772")
            await client.edit_channel(v_gen, name="lareneG\U0001F30F")
            v_gen2 = message.author.server.get_channel("422326184576286720")
            await client.edit_channel(v_gen2, name="2 lareneG")
            rr = message.author.server.get_channel("420314276243439626")
            await client.edit_channel(rr, name="moor deknaR")
            rr2 = message.author.server.get_channel("420391458453848064")
            await client.edit_channel(rr2, name=")scca 2 s'nitsuJ rof 3( 2#  moor deknaR")


        if message.content == "create clicker":
            await client.create_channel(message.author.server, "clickergame")

        if message.content == "secret clear message":
            await client.purge_from(message.channel)

        if message.content == "clicker startup":
            await client.delete_message(message)
            await client.send_message(message.channel, "This is the coin clicker game! Say \"play clicker\" to begin. \n Click the coin reaction to get more coins! \n If you have 100 coins, you can buy an automatic clicker that will produce 10 coins every hour! \n --------------------------------")
                
        if message.content == "play clicker" and message.channel.name == "clickergame" or message.channel.name == "bot-devolper":
            await client.delete_message(message)
            clicks = 0
            current_hour = now.hour
            auto_clickers = 3600
            clicker_mess = await client.send_message(message.channel, str(message.author.display_name) + " has " + str(clicks) + " coins")
            for c_emoji in client.get_all_emojis():
                if c_emoji.name == 'Coin':
                    coin = c_emoji
#            for c_emoji in client.get_all_emojis():
#                if c_emoji.name == 'Blank':
#                    blank = c_emoji
#            for c_emoji in client.get_all_emojis():
#                if c_emoji.name == 'Buy':
#                    buy = c_emoji
            await client.add_reaction(clicker_mess, coin)
#            await client.add_reaction(clicker_mess, blank)
#            await client.add_reaction(clicker_mess, buy)
            clicker_start = True
            click = "l"
            noc = "l"
            while True == True:
                click = await client.wait_for_reaction(emoji=coin, user=message.author, timeout=0.05, message=clicker_mess)
                if not click is None:
                    if len(click) > 1:
                        clicks = clicks + 1
                        await client.edit_message(clicker_mess, new_content=str(message.author.display_name) + " has " + str(clicks) + " coins")
                        await client.remove_reaction(clicker_mess, coin, message.author)
                        click = "l"
                        print(len(click))
            
#                print("hello")
#                noc = await client.wait_for_reaction(emoji=buy, user=message.author, timeout=0.05, message=clicker_mess)
#                print("hello")
#                if not noc is None:
#                    if len(noc) > 1:
#                        print("hello")
#                        if clicks >= 100:
#                            clicks -= 100
#                            auto_clickers += 1
#                        client.edit_message(clicker_mess, new_content=str(message.author.display_name) + " has " + str(clicks) + " coins and " + str(auto_clickers) + " autoclickers")
#                        noc = "l"
#                        await client.remove_reaction(clicker_mess, buy, message.author)

            
#                if auto_clickers > 0:
#                    if current_hour != now.hour:
#                        clicks += auto_clickers * 10
#                        current_hour = now.hour
                    

        if message.channel.name == "clickergame":
            await client.delete_message(message)
            
            
            

            




      


            





    #clear fredboat

                
@client.event
async def on_message_edit(bef, aft):
    if bef.author.id == "184405311681986560":
        print(aft.content[:4])
        if aft.content[:4] == "Song":
            await client.purge_from(aft.channel, before=aft, limit=100, check=is_fred)

    
                         
        



client.run("NDI4OTgxMzU3NDQwNTMyNDgy.DZ7CsQ.T5EXx4MOF5B5UzU73uwLXjfnShQ")


