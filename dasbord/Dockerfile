FROM node:8.9.4
# COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . .
CMD ["node" , "index.js"]
