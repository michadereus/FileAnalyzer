FROM node:16-slim

COPY . /user/src/app

WORKDIR /user/src/app

COPY ./package.json ./

COPY ./package-lock.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]