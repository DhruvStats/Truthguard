const mongoose = require("mongoose");

const ResultSchema = new mongoose.Schema({
  text: String,
  prediction: String,
  confidence: Number,
  createdAt: { type: Date, default: Date.now }
});

module.exports = mongoose.model("Result", ResultSchema);