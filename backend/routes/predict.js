const express = require("express");
const axios = require("axios");
const Result = require("../models/Result");

const router = express.Router();

router.post("/", async (req, res) => {
  try {
    const { text } = req.body;

    const mlResponse = await axios.post(
      "http://127.0.0.1:8000/predict",
      { text }
    );

    await Result.create({
      text,
      prediction: mlResponse.data.prediction,
      confidence: mlResponse.data.confidence
    });

    res.json(mlResponse.data);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Prediction failed" });
  }
});

module.exports = router;