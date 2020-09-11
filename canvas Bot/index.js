const Discord = require('discord.js');
 const client = new Discord.Client();

client.on('ready', () => {
 console.log(`Logged in as ${client.user.tag}!`);
 });

client.on('message', msg => {
 if (msg.content === 'ping') {
 msg.reply('pong');
 }
 });

client.login('NzUxNDc3Mzk4MDI5MDc0NTE0.X1Jp3Q.KAcxA-I3MX40zW1ORx_49SfbLpc');