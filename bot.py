import telebot			
from os import environ	
from random import randrange

bot = telebot.TeleBot(environ['TELEGRAM_TOKEN']) 


bot_text = '''				
Hola Meg!
Te adoro...
github.com/mrnettlepatch/botDeProbas
'''.format(environ['PROJECT_NAME'])



@bot.message_handler(commands=['start', 'help']) 						
def send_welcome(message):			 	
	bot.reply_to(message, bot_text)			

 #AYUDA PROVISIONAL
@bot.message_handler(commands=['ayuda'])		
def ayuda(message):					
	bot.reply_to(message, 'Habla con mi creador @mrnettlepatch si necesitas ayuda!')   

  #ID
@bot.message_handler(commands=['miid'])		
def ayuda(message):					
	bot.reply_to(270803389, message.from_user)  
  
@bot.message_handler(commands=['chatid'])		
def ayuda(message):					
	bot.send_message(270803389, message.chat) 

#RULETA
@bot.message_handler(commands=['ruleta'])
def ruleta(message):

  cid = message.chat.id					
  title  = message.chat.title
  nombreUsuario = message.from_user.username		
  idUsuario = message.from_user.id			
  rnd = randrange(0, int(5))				

  if rnd == 4:						
    bot.send_message(cid, "Estás morrido @" + nombreUsuario )	
    bot.kick_chat_member(cid,idUsuario)					
    bot.unban_chat_member(cid, idUsuario)		
    bot.send_message(chat_id  =  message.from_user.id,  text  =  'Has perdido la ruleta del grupo:  '  +  title  +  ', toma el link de invitación para volver al grupo: ' + str(bot.export_chat_invite_link(cid)))
  else:								
    bot.send_message(cid, "Tuveches suerte @" + nombreUsuario)	

#CARA O CRUZ	

@bot.message_handler(commands=['moneda'])
def moneda(message):
  cid = message.chat.id								
  rnd = randrange(0,int(2))
  if rnd == 0:
	  bot.send_message(cid, "Cara")
  elif rnd == 1:
	  bot.send_message(cid, "Cruz")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
  if message.text.lower() == "holi":
    username = message.from_user.username
    id = message.from_user.id
    cid = message.chat.id

    if id == 270803389 :
        bot.send_message( cid, 'Hola mi creador 😙')

    else:
      
       bot.send_message( cid, 'Cala, basurillas')   
  
bot.set_webhook("https://{}.glitch.me/{}".format(environ['PROJECT_NAME'], environ['TELEGRAM_TOKEN']))
