import discord
from discord.ext import commands
import os
import json
from datetime import datetime,timedelta


os.system('pip install --upgrade pip')
os.system('pip install --upgrade discord.py')

intents = discord.Intents.all()


with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='-',intents = intents)

@bot.event
async def on_ready():
    bot.unload_extension(F'cmds.test')
    print(">> 目前版本：v2.1.8 <<")
    print(">> Meow_Bot is online <<")
   

#----------------------------------------------------------------------------
bot.remove_command('help')
#help指令
@bot.group(name='help', aliases=['說明' , '機器人使用說明' , '幫助'])
async def help(ctx):
    await ctx.send('普通功能：\n```css\n'
    +str(jdata['command_prefix'])+'ping 顯示機器人的延遲\n'
    +str(jdata['command_prefix'])+'ccc [基礎近戰暴率 連擊數 額外暴率加成] 計算近戰塞急進猛突暴率\n'
    +str(jdata['command_prefix'])+'wws [基礎近戰觸發 連擊數 額外觸發加成] 計算近戰塞創口潰爛觸發\n'
    +str(jdata['command_prefix'])+'sayd [msg] 使機器人說話\n'
    +str(jdata['command_prefix'])+'member 顯示伺服器中所有人的狀態\n'
    +str(jdata['command_prefix'])+'online 顯示上線名單\n'
    +str(jdata['command_prefix'])+'offline 顯示離線名單\n'
    +str(jdata['command_prefix'])+'picture 隨機發送一張圖片\n'
    +str(jdata['command_prefix'])+'ms 踩地雷\n'
    +str(jdata['command_prefix'])+'calc [數學算式]簡易的運算(支援: + - * / ( ) 小數 科學記號)中間不能有空格 不支援指數運算 \n'
    +str(jdata['command_prefix'])+'alias 顯示各個指令的別名\n'
    +str(jdata['command_prefix'])+'user 顯示個人訊息\n```僅限管理員的功能：\n```css\n'
    +str(jdata['command_prefix'])+'clear [num] 刪除指定數量的聊天內容\n```')


@bot.command(name='alias', aliases=['別名'])
async def alias(ctx):
  await ctx.send('這些指令的別名：\n```css\n'
    +str(jdata['command_prefix'])+'help：[說明 , 機器人使用說明 , 幫助]\n'
    +str(jdata['command_prefix'])+'ping：[延遲 , 機器人延遲 , delay]\n'
    +str(jdata['command_prefix'])+'ccc：[急進猛突 , 急進 , 極盡]\n'
    +str(jdata['command_prefix'])+'wws：[創口潰爛 , 創口]\n'
    +str(jdata['command_prefix'])+'sayd：[說 , 機器人說]\n'
    +str(jdata['command_prefix'])+'member [顯示成員 , 成員]\n'
    +str(jdata['command_prefix'])+'online [顯示上線成員 , 上線 , 在線]\n'
    +str(jdata['command_prefix'])+'offline [顯示下線成員 , 下線 , 顯示離線成員 , 離線]\n'
    +str(jdata['command_prefix'])+'picture：[pic , 圖片]\n'
    +str(jdata['command_prefix'])+'ms：[踩地雷]\n'
    +str(jdata['command_prefix'])+'calc：[計算機 , 計算]\n'
    +str(jdata['command_prefix'])+'user：[使用者資訊 , 用戶資訊]\n'
    +str(jdata['command_prefix'])+'clear：[clean , 清除]\n```')
 
#-----------------------------------------------------------------------------
f = '[%Y-%m-%d %H:%M:%S]'
time_delta = timedelta(hours=+8)
utc_8_date_str = (datetime.utcnow()+time_delta).strftime(f)
#-----------------------------------------------------------------------------

@bot.command(name= 'load', aliases=['載入' , '載入模組' , '啟用'])
async def load(ctx, extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(f'\n已加載：{extension}')
    print('\n---------------------------------\n' + utc_8_date_str + f'\n已加載 {extension}\n---------------------------------\n')


@bot.command(name= 'unload', aliases=['卸載' , '卸載模組' , '停用'])
async def unload(ctx, extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(f'\n已卸載：{extension}')
    print('\n---------------------------------\n' + utc_8_date_str + f'\n已卸載 {extension}\n---------------------------------\n')

@bot.command(name= 'reload', aliases=['重載' , '重載模組' , '重新載入模組', '重新加載', '重啟'])
async def reload(ctx, extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(f'\n已重新載入：{extension}')
    print('\n---------------------------------\n' + utc_8_date_str + f'\n已重新載入 {extension}\n---------------------------------\n')
#機器人關閉系統--------------------------------------------   

@bot.command(name= 'disconnect', aliases=['disable' , 'shutdown' , '關閉機器人' , '關機' , '關閉'])
async def turn_off_bot(ctx):
  if ctx.message.author.id == jdata['owner']:
    print(utc_8_date_str + '機器人已關閉')
    await ctx.send(utc_8_date_str + '\n機器人已關閉') #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    await bot.close()
  else:
    await ctx.send('權限不足 本指令只提供給Meow_Bot擁有者 \n擁有者為 <@436866339731275787> [小翔]')
    
#--------------------------------

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')
        
if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
