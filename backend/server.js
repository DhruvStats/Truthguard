/**
 * TruthGuard Backend Server
 * Works in:
 * 1) Normal local development
 * 2) Docker / DevOps environment
 * Uses environment variables safely without breaking current setup
 */

const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const axios = require("axios");
const Result = require("./models/Result");

const app = express();

/* =========================
   CONFIGURATION
========================= */

// MongoDB (local or docker)
const MONGO_URI =
  process.env.MONGO_URI || "mongodb://127.0.0.1:27017/newsguard-ai";

// ML Service (local or docker)
const ML_BASE_URL =
  process.env.ML_BASE_URL || "http://127.0.0.1:8000";

// Server Port
const PORT = 5000;

/* =========================
   MIDDLEWARE
========================= */
app.use(cors());
app.use(express.json());

/* =========================
   DATABASE CONNECTION
========================= */
mongoose
  .connect(MONGO_URI)
  .then(() => console.log("✅ MongoDB connected"))
  .catch((err) =>
    console.error("❌ MongoDB connection failed:", err.message)
  );

/* =========================
   HEALTH CHECK (DevOps)
========================= */
app.get("/health", (req, res) => {
  res.json({ status: "Backend service running" });
});

/* =========================
   MAIN AI ANALYSIS API
========================= */
app.post("/analyze", async (req, res) => {
  try {
    const { text } = req.body;

    if (!text || !text.trim()) {
      return res.status(400).json({ error: "Text is required" });
    }

    // Call ML inference service
    const mlResponse = await axios.post(
      `${ML_BASE_URL}/predict`,
      { text },
      { timeout: 5000 }
    );

    const { prediction, confidence } = mlResponse.data;

    // Store prediction for MLOps tracking
    await Result.create({
      text,
      prediction,
      confidence,
    });

    // Send response to frontend
    res.json({ prediction, confidence });

  } catch (err) {
    console.error("🔥 ML CALL FAILED");
    console.error(err.message);
    res.status(500).json({ error: "Prediction failed" });
  }
});

/* =========================
   START SERVER
========================= */
app.listen(PORT, "0.0.0.0", () => {
  console.log(`✅ Backend running on port ${PORT}`);
});