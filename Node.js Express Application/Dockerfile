FROM node:22-alpine
WORKDIR /app
COPY package.json .
RUN npm install ci --only=production
COPY . .
EXPOSE 3000
CMD ["node","server.js"]