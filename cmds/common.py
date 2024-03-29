from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
from random import randint


with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Common(Cog_Extension):
#    #ping
#    @commands.command(name= 'ping', aliases=['延遲' , '機器人延遲' , 'delay'])
#    async def ping(self, ctx):
#        await ctx.send(f'{round(self.bot.latency*1000)} 毫秒 (ms)')

    #隨機傳送圖片網址
    @commands.command(name= 'picture', aliases=['pic' , '圖片'])
    async def picture(self,ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)
    #查詢user資訊
    @commands.command(name= 'user', aliases=['使用者資訊' , '用戶資訊'])
    async def user(self,ctx):
        arg = ctx.message.channel
        args = str(arg).split(' ')
        CMD = 'Direct Message with'
        CMDs = CMD.split(' ')
        msg = 'Author:'+str(ctx.message.author)+'\nAuthor ID:'+ str(ctx.message.author.id)+'\nChannel:'+str(ctx.message.channel)+'\nChannel ID:'+str(ctx.message.channel.id)
        if CMDs[0] == args[0] and CMDs[1] == args[1] and CMDs[2] == args[2]:
            print('私人訊息')
            await ctx.send(msg)
        else:
            print('群組訊息')
            msg = msg +'\nGuild.owner:'+str(ctx.guild.owner) +'\nGuild.owner_id:' +str(ctx.guild.owner_id)+'\nGuild.name:' +str(ctx.guild.name)
            await ctx.send(msg)
    #說
    @commands.command(name= 'sayd', aliases=['說' , '機器人說'])
    async def sayd(self,ctx,*value):
      if value == ():
        await ctx.send(jdata['command_prefix']+"sayd [msg]")
      else:
        msg = ' '.join(value)
        await ctx.message.delete()
        await ctx.send(msg)
        
    @commands.command()
    async def emmsg(self,ctx,msgid,em):
        msg = await ctx.message.channel.fetch_message(int(msgid))
        print(msg.content)
        await ctx.message.delete()
        if len(em)<18:
            await msg.add_reaction(em)
        else:
            emoji = self.bot.get_emoji(int(((em.split('>'))[0])[-18:]))
            await msg.add_reaction(emoji)
        
    #近戰有塞急進猛突12x下的暴擊機率計算器
    @commands.command(name='ccc', aliases=['急進猛突' , '急進' , '極盡'])
    async def ccc(self,ctx,*,num):
      try:
        i1, i2, i3 = num.split(' ')
        if int(i2) <= 13:
          sum= float(i1) * ( 100 + 60 * ( float(i2) - 1 ) + float(i3) )  / 100
          #總暴率=基礎暴率× (1 + 急進猛突的加成 × (連擊倍率-1)+其他暴擊加成)
          await ctx.send('近戰總爆擊機率：' + str(sum) + '%')
        else:
          await ctx.send('連擊最高只有到13x啦！')
      except:
        await ctx.send(jdata['command_prefix']+'ccc [基礎近戰暴率 連擊數 額外暴率加成]')
    #----------------------------------
    #近戰有塞創口潰爛12x下的觸發機率計算器    
    @commands.command(name= 'wws', aliases=['創口潰爛' , '創口'])
    async def wws(self,ctx,*,num):
      try:
        i1, i2, i3 = num.split(' ')
        if int(i2) <= 13:
          sum= float(i1) * ( 100 + 40 * ( float(i2) - 1 ) + float(i3) )  / 100
          #總觸發=基礎觸發× (1 + 觸發加成 × (連擊倍率-1)+其他觸發加成)
          await ctx.send('近戰總觸發機率：' + str(sum) + '%')
        else:
          await ctx.send('連擊最高只有到13x啦！')
      except:
        await ctx.send(jdata['command_prefix']+'wws [基礎近戰觸發 連擊數 額外觸發加成]')

    #環形裝置
    @commands.command()
    async def 環形裝置(self,ctx):
      await ctx.send(f'```維加環形裝置→太空站          & 微蟎蛛型機\n告達環形裝置→昇華實驗室      & 賽托蛛型機(瓦內蜘蛛)\n索拉環形裝置→潤盈寺          & 凱塔蛛型機\n聖油環形裝置→利潤收割者圓蛛\n天藍環形裝置→剝削者圓蛛```')

    #香蕉君
    @commands.command(name= 'Milos', aliases=['香蕉君' , '象徵自由的男人' , '自由'])
    async def Milos(self,ctx):
      #await ctx.channel.purge(limit=1)
      await ctx.send(self.bot.get_emoji(int(710157217948631085)))

    #踩地雷   
    @commands.command(name='ms', aliases=['踩地雷'])
    async def minesweeper(self, ctx, width: int = 10, height: int = 10, difficulty: int = 30):
      grid = tuple([['' for i in range(width)] for j in range(height)])
      num = ('0⃣','1⃣','2⃣','3⃣','4⃣','5⃣','6⃣','7⃣','8⃣')
      msg = ''

      if not (1 <= difficulty <= 100):
        await ctx.send("Please enter difficulty in terms of percentage (1-100).")
        return
      if width <= 0 or height <= 0:
        await ctx.send("Invalid width or height value.")
        return
      if width * height > 198:
        return await ctx.channel.send("Your grid size is too big.")
        return
      if width * height <= 4:
        await ctx.send("Your grid size is too small.")
        return
      
      # set bombs in random location
      for y in range(0, height):
        for x in range(0, width):
          if randint(0, 100) <= difficulty:
            grid[y][x] = '💣'

      # now set the number emojis
      for y in range(0, height):
        for x in range(0, width):
          if grid[y][x] != '💣':
            grid[y][x] = num[sum((
              grid[y-1][x-1]=='💣' if y-1>=0 and x-1>=0 else False,
              grid[y-1][x]=='💣' if y-1>=0 else False,
              grid[y-1][x+1]=='💣' if y-1>=0 and x+1<width else False,
              grid[y][x-1]=='💣' if x-1>=0 else False,
              grid[y][x+1]=='💣' if x+1<width else False,
              grid[y+1][x-1]=='💣' if y+1<height and x-1>=0 else False,
              grid[y+1][x]=='💣' if y+1<height else False,
              grid[y+1][x+1]=='💣' if y+1<height and x+1<width else False
            ))]
      await ctx.send(grid[y][x])

      # generate message
      for i in grid:
        for tile in i:
          msg += '||' + tile + '|| '
        msg += '\n'
      await ctx.send(msg)

  
    
def setup(bot):
    bot.add_cog(Common(bot))