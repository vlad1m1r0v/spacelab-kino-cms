FROM node:14

WORKDIR /code

COPY package.json /code/package.json
COPY package-lock.json /code/package-lock.json

RUN npm install

COPY adminlte /code

CMD ["npm", "run", "dev"]
