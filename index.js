/**
 * Libs
 */
require('dotenv').config()
const config = require('./config')
const Discord = require('discord.js')
const client = new Discord.Client()
const fs = require('fs')

client.once('ready', () => {
  console.log('Ready!')
  client.user.setActivity('', { type: 'PLAYING' })
  client.users.cache.forEach(user => {
    if (user.username === 'lukynmatuska') {
      console.log(user)
      // user.send('hell.o')
      user.send(new Discord.MessageAttachment(fs.readFileSync('./math.gif'), 'math.gif'))
    }
  })
})

client.on('message', message => {
  //   console.log(message.content)
  if (message.content === `${config.prefix}ping`) {
    // send back "Pong." to the channel the message was sent in
    message.channel.send('Pong.')
  } else if (message.content === `${config.prefix}server`) {
    message.channel.send(`Server name: ${message.guild.name}\nTotal members: ${message.guild.memberCount}`)
  }
})

// Bot login
client.login(process.env.DISCORD_TOKEN)
