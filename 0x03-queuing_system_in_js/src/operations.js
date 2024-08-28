const client = require('./redisClient');

// Example: Store a hash in Redis
function storeHash(key, value) {
  client.hmset(key, value, (err, res) => {
    if (err) {
      console.error('Error storing hash:', err);
    } else {
      console.log('Hash stored:', res);
    }
  });
}

module.exports = { storeHash };
