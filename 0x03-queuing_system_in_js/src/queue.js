const kue = require('kue');
const queue = kue.createQueue();

queue.on('error', (err) => {
  console.error('Queue error:', err);
});

module.exports = queue;
