const express = require('express');
const path = require('path');
const http = require('http');
const socketio = require('socket.io');
const formatMessage = require('./utils/messages');
const { userJoin, getCurrentUser, userLeave, getRoomUsers } = require('./utils/users.js');

const app = express();
const server = http.createServer(app);
const io = socketio(server);

const botName = 'Admin';

//Set static folder
app.use(express.static(path.join(__dirname, 'public')));

io.on('connection', socket => {
    socket.on('joinRoom', ({ username, room }) => {
        const user = userJoin(socket.id, username, room);
        socket.join(user.room);
        
        //Welcome current user
        socket.emit('message', formatMessage(botName, 'Welcome to Simple Chat App'));
        
        //Broadcast when user is connect
        socket.broadcast.to(user.room).emit('message', formatMessage(botName, `${user.username} has joined the chat`));

        //Send users and room info
        io.to(user.room).emit('roomUsers', {
            room:user.room,
            users:getRoomUsers(user.room)
        });

        //Run when client disconnect
        socket.on('disconnect', () => {
            const user = userLeave(socket.id);
            if (user) {
                io.to(user.room).emit('message', formatMessage(botName, `${user.username} has left the chat`));
            };

            //Send users and room info
            io.to(user.room).emit('roomUsers', {
                room:user.room,
                users:getRoomUsers(user.room)
            });
        });

        //Listen for chat message
        socket.on('chatMessage', (msg) => {
            const user = getCurrentUser(socket.id);
            io.to(user.room).emit('message', formatMessage(user.username, msg));
        })
    });
});



const PORT = process.env.PORT || 3000;

server.listen(PORT, () => console.log(`Server running on port ${PORT}`));
