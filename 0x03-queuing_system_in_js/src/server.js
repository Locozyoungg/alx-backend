const express = require('express');
const redisClient = require('./redisClient');
const queue = require('./queue');
const routes = require('./routes');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware and routes setup
app.use(express.json());
app.use('/', routes);

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
