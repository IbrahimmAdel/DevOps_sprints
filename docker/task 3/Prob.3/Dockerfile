FROM node:16

WORKDIR ./dockerize-node-app-task

COPY package.json ./

RUN npm install

COPY . .

EXPOSE 8080

CMD [ "node", "server.js" ]
