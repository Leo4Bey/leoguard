import discord
from discord.ext import commands
import requests,json
from config import *
from twilio.rest import Client
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)

account_sid = ('twilo_account_sid') #Buraya yapıştıracaksınız
auth_token = ('twilo_auth_token') #Buraya yapıştıracaksınız
client = Client(account_sid, auth_token)


bot = commands.Bot(command_prefix="!", intents=intents) #! olan kısım prefixiniz değiştirebilirsiniz


#KANAL OLUŞTURMA ENGEL
@bot.event
async def on_guild_channel_create(channel):
    entry = await channel.guild.audit_logs(action=discord.AuditLogAction.channel_create, limit=1).get()
    user = entry.user
    user3 = str(entry.user.id)
    user4 = str(entry.user)
    channel22 = channel.name
    channel8 = channel
    member = channel.guild.get_member(user.id) or await channel.guild.fetch_member(user.id)
    channel99 = bot.get_channel(954724771034198036) #Buraya log kanal id sini gireceksiniz
    if user3 in güvenli:
        return
    else:
        embed = discord.Embed (
        title = "Bir kanal Oluşturuldu !",
        description = "・Kanalı Oluşturan Kişi: ``" + user4 + "`` \n ・ Kanalı Oluşturan Kişi id: ``" + user3 + "`` \n・ Oluşturulan Kanal: ``" + channel22 + "`` \n ・ ``" + user4 + "`` Hakkında Gerekli İşlemler Yapıldı. \n・ Oluşturulan ``" + channel22 + "`` Adlı kanal silindi.",
        colour = discord.Colour.random() 
        )
        await member.ban(reason = f"{user4} Adlı Yetkili - {channel22} - Adlı Kanalı İzinsiz Oluşturdu Bundan Dolayı Ban Yedi. | Leo Guard System")
        await channel99.send(embed=embed)
        await channel8.delete()
        message = client.messages \
        .create(
            body= user4 + " adlı kullanıcı \n" + channel22 + " Adlı kanalı Oluşturdu Gerekli işlemler uygulandı",
            from_= gönderici,
            to= alici
        )
        print(f"{user4} Adlı Yetkili - {channel22} - Adlı Kanalı İzinsiz Oluşturdu Bundan Dolayı Ban Yedi.")

#KANAL SİLME ENGEL
@bot.event
async def on_guild_channel_delete(channel):
    entry = await channel.guild.audit_logs(action=discord.AuditLogAction.channel_delete, limit=1).get()
    user = entry.user
    user3 = str(entry.user.id)
    user4 = str(entry.user)
    channel22 = channel.name
    channel8 = channel
    member = channel.guild.get_member(user.id) or await channel.guild.fetch_member(user.id)
    channel99 = bot.get_channel(954724771034198036) #Buraya log kanal id sini gireceksiniz
    if user3 in güvenli:
        return
    else:
        embed = discord.Embed (
        title = "Bir kanal Silindi !",
        description = "・Kanalı Silen Kişi: ``" + user4 + "`` \n ・ Kanalı Silen Kişi id: ``" + user3 + "`` \n・ Silinen Kanal: ``" + channel22 + "`` \n ・ ``" + user4 + "`` Hakkında Gerekli İşlemler Yapıldı. \n・ Silinen ``" + channel22 + "`` Adlı kanal Yeniden Oluşturuldu.",
        colour = discord.Colour.random() 
        )
        await member.ban(reason = f"{user4} Adlı Yetkili - {channel22} - Adlı Kanalı İzinsiz Sildi Bundan Dolayı Ban Yedi. | Leo Guard System")
        await channel99.send(embed=embed)
        new_channel = await channel.clone()
        message = client.messages \
        .create(
            body= user4 + " adlı kullanıcı \n" + channel22 + " Adlı kanalı Sildi Gerekli işlemler uygulandı",
            from_= gönderici,
            to= alici
        )
        print(f"{user4} Adlı Yetkili - {channel22} - Adlı Kanalı İzinsiz Sildi Bundan Dolayı Ban Yedi.")

#KANAL GÜNCELLEME ENGEL
@bot.event
async def on_guild_channel_update(before, after):
    entry = await guild.audit_logs(action=discord.AuditLogAction.channel_update, limit=1).get()
    user = entry.user
    user3 = str(entry.user.id)
    user4 = str(entry.user)
    channel22 = channel.name
    channel8 = channel
    member = channel.guild.get_member(user.id) or await channel.guild.fetch_member(user.id)
    channel99 = bot.get_channel(954724771034198036) #Buraya log kanal id sini gireceksiniz
    if user3 in güvenli:
        return
    else:
        embed = discord.Embed (
        title = "Bir kanal güncellendi !",
        description = "・Kanalı Güncelleyen Kişi: ``" + user4 + "`` \n ・ Kanalı Güncelleyen Kişi id: ``" + user3 + "`` \n・ Güncellenen Kanal: ``" + channel22 + "`` \n ・ ``" + user4 + "`` Hakkında Gerekli İşlemler Yapıldı. \n・ Güncellenen ``" + channel22 + "`` Adlı kanal Eski Haline Getirildi .",
        colour = discord.Colour.random() 
        )
        #await member.ban(reason = f"{user4} Adlı Yetkili - {channel22} - Adlı Kanalı İzinsiz Güncelledi Bundan Dolayı Ban Yedi. | Leo Guard System")
        await channel99.send(embed=embed)
        message = client.messages \
        .create(
            body= user4 + " adlı kullanıcı \n" + channel22 + " Adlı kanalı Sildi Gerekli işlemler uygulandı",
            from_= gönderici,
            to= alici
        )
        print(f"{user4} Adlı Yetkili - {channel22} - Adlı Kanalı İzinsiz Sildi Bundan Dolayı Ban Yedi.")

#ROL OLUŞTURMA ENGEL
@bot.event
async def on_guild_role_create(role):
    entry = await role.guild.audit_logs(action=discord.AuditLogAction.role_create, limit=1).get()
    user = entry.user
    user3 = str(entry.user.id)
    user4 = str(entry.user)
    role22 = role.name
    role8 = role
    member = role.guild.get_member(user.id) or await role.guild.fetch_member(user.id)
    channel99 = bot.get_channel(954724771034198036) #Buraya log kanal id sini gireceksiniz
    if user3 in güvenli:
        return
    else:
        embed = discord.Embed (
        title = "Bir Rol Oluşturuldu",
        description = "・Rolü Oluşturan Kişi: ``" + user4 + "`` \n ・ Rolü Oluşturan Kişi id: ``" + user3 + "`` \n・ Oluşturulan Rol Adı: ``" + role22 + "`` \n ・ ``" + user4 + "`` Hakkında Gerekli İşlemler Yapıldı. \n・ Oluşturulan ``" + role22 + "`` Adlı Rol Silindi.",
        colour = discord.Colour.random() 
        )
    await member.ban(reason = f"{user4} Adlı Yetkili - {role22} - Adlı Rolü İzinsiz Oluşturdu Bundan Dolayı Ban Yedi. | Leo Guard System")
    await channel99.send(embed=embed)
    await role8.delete()
    message = client.messages \
    .create(
        body= user4 + " adlı kullanıcı \n" + role22 + " Adlı Rolü Oluşturdu Gerekli işlemler uygulandı",
        from_= gönderici,
        to= alici
    )
    print(f"{user4} Adlı Yetkili - {role22} - Adlı Rolü İzinsiz Oluşturdu Bundan Dolayı Ban Yedi.")

#ROL SİLME ENGEL
@bot.event
async def on_guild_role_delete(role):
    entry = await role.guild.audit_logs(action=discord.AuditLogAction.role_delete, limit=1).get()
    user = entry.user
    user3 = str(entry.user.id)
    user4 = str(entry.user)
    role22 = role.name
    role01 = role.colour
    role02 = role.permissions
    role8 = role
    guild = bot.guilds[0]
    member = role.guild.get_member(user.id) or await role.guild.fetch_member(user.id)
    channel99 = bot.get_channel(954724771034198036) #Buraya log kanal id sini gireceksiniz
    if user3 in güvenli:
        return
    else:
        embed = discord.Embed (
        title = "Bir Rol Silindi",
        description = "・Rolü Silen Kişi: ``" + user4 + "`` \n ・ Rolü Silen Kişi id: ``" + user3 + "`` \n・ Silinen Rol Adı: ``" + role22 + "`` \n ・ ``" + user4 + "`` Hakkında Gerekli İşlemler Yapıldı. \n・ Silinen ``" + role22 + "`` Adlı Rol Oluşturuldu.",
        colour = discord.Colour.random() 
        )
    await member.ban(reason = f"{user4} Adlı Yetkili - {role22} - Adlı Rolü İzinsiz Sildi Bundan Dolayı Ban Yedi. | Leo Guard System")
    await channel99.send(embed=embed)
    new_role = await guild.create_role(name = role22, colour = role.colour, permissions=role.permissions)
    message = client.messages \
    .create(
        body= user4 + " adlı kullanıcı \n" + role22 + " Adlı Rolü Sildi Gerekli işlemler uygulandı",
        from_= gönderici,
        to= alici
    )
    print(f"{user4} Adlı Yetkili - {role22} - Adlı Rolü İzinsiz Sildi Bundan Dolayı Ban Yedi.")

#BAN KORUMA
@bot.event
async def on_member_ban(guild, user):
    entry = await guild.audit_logs(action=discord.AuditLogAction.ban, limit=1).get()
    user = entry.user
    user3 = str(entry.user.id)
    user4 = str(entry.user)
    member = guild.get_member(user.id) or await guild.fetch_member(user.id)
    target = entry.target
    target2 = str(entry.target)
    target3 = str(entry.target.id)
    target4 = str(entry.target.name)
    channel99 = bot.get_channel(954724771034198036) #Buraya log kanal id sini gireceksiniz
    if user3 in güvenli:
        return
    else:
        embed = discord.Embed (
        title = "Bir Kişi Banlandı !",
        description = "・Ban Atan Kişi: ``" + user4 + "`` \n ・Ban Atan Kişi id: ``" + user3 + "`` \n ・Banlanan Kişi Adı: ``" + target2 + "`` \n ・Banlanan Kişi id: ``" + target3 + "`` \n・ ``" + user4 + "`` Hakkında Gerekli İşlemler Yapıldı.",
        colour = discord.Colour.random() 
        )
        await guild.unban(discord.Object(id=target.id), reason = f"{user4} Adlı Yetkili {target4} Adlı Kişiyi İzinsiz Banladığı İçin Banı Açıldı")
        await member.ban(reason = f"{target.name} Adlı Kişiyi İzinsiz Banladığı İçin Sunucudan Yasaklandı")
        await channel99.send(embed=embed)
    message = client.messages \
    .create(
        body= user4 + " adlı kullanıcı \n" + target2 + " Adlı Kişiyi İzinsiz Banladı Gerekli işlemler uygulandı",
        from_= gönderici,
        to= alici
    )
    print(f"{user4} Adlı Yetkili - {target4} - Adlı Kişiyi İzinsiz Banladı Bundan Dolayı Ban Yedi.")

#UNBAN KORUMA
@bot.event
async def on_member_unban(guild, user):
    entry = await guild.audit_logs(action=discord.AuditLogAction.unban, limit=1).get()
    user = entry.user
    user3 = str(entry.user.id)
    user4 = str(entry.user)
    member = guild.get_member(user.id) or await guild.fetch_member(user.id)
    target = entry.target
    target2 = str(entry.target)
    target3 = str(entry.target.id)
    target4 = str(entry.target.name)
    channel99 = bot.get_channel(954724771034198036) #Buraya log kanal id sini gireceksiniz
    if user3 in güvenli:
        return
    else:
        embed = discord.Embed (
        title = "Bir Kişinin Banı Açıldı !",
        description = "・Banı Açan Kişi: ``" + user4 + "`` \n ・Banı Açan Kişi id: ``" + user3 + "`` \n ・Banı açılan Kişi Adı: ``" + target2 + "`` \n ・Banı açılan Kişi id: ``" + target3 + "`` \n・ ``" + user4 + "`` ve ``" + target2 + "`` Hakkında Gerekli İşlemler Yapıldı.",
        colour = discord.Colour.random() 
        )
        await guild.ban(discord.Object(id=target.id), reason = f"{user4} Adlı Yetkili {target4} Adlı Kişinin Banını İzinsiz Açtı Gerekli İşlemler Yapıldı")
        await member.ban(reason = f"{target.name} Adlı Kişinin Banını izinsiz Açtığı için Sunucudan Yasaklandı")
        await channel99.send(embed=embed)
    message = client.messages \
    .create(
        body= user4 + " adlı kullanıcı \n" + target2 + " Adlı Kişinin Banını izinsiz Kaldırdı Gerekli işlemler uygulandı",
        from_= gönderici,
        to= alici
    )
    print(f"{user4} Adlı Yetkili - {target4} - Adlı Kişinin Banını izinsiz Kaldırdı Bundan Dolayı Ban Yedi.")

@bot.event
async def on_ready():
    print(bot.user.name)
    await bot.change_presence(activity=discord.Game(name="<3 LEO4BEY")) 

bot.run(token)

#LEO4BEY TARAFINDAN YAZILMIŞTIR İZİNSİZ PAYLAŞILMASI YASAKTIR
#SOT [ÇAKA BEYLİĞİ] Sunucusu için Yazılmıştır
#https://discord.gg/5bbvAcWdu2 #SOT [ÇAKA BEYLİĞİ]
#https://discord.gg/QTsB54eWJq # Bot hakkında destek almak için 
