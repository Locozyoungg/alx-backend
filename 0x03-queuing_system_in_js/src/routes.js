const express = require('express');
const router = express.Router();
const { storeHash } = require('./operations');

// Example route to set a hash value in Redis
router.post('/hash', (req, res) => {
  const { key, value } = req.body;
  storeHash(key, value);
  res.status(200).send('Hash stored in Redis');
});

module.exports = router;
