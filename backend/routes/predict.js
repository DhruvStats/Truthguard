/**
 * Prediction route for TruthGuard backend
 *
 * Responsibilities:
 * - Accept news text from frontend
 * - Forward request to ML inference service
 * - Return prediction + confidence to frontend
 *
 * This version:
 * ✅ Uses environment variable for ML service URL
 * ✅ Has a safe localhost fallback
 * ✅ Works in local, Docker, CI/CD, and Kubernetes setups
 */

const express = require("express");
const axios = require("axios");

const router = express.Router();

// Resolve ML service base URL safely
const ML_BASE_URL =
  process.env.ML_BASE_URL || "http://127.0.0.1:8000";

/**
 * POST /analyze
 * Body: { text: string }
 */
router.post("/analyze", async (req, res) => {
  try {
    const { text } = req.body;

    // Basic validation (backend-level safety)
    if (!text || typeof text !== "string") {
      return res.status(400).json({
        error: "Request must contain a non-empty 'text' field"
      });
    }

    // Forward request to ML inference service
    const mlResponse = await axios.post(
      `${ML_BASE_URL}/predict`,
      { text }
    );

    // Return ML response directly to frontend
    return res.status(200).json({
      prediction: mlResponse.data.prediction,
      confidence: mlResponse.data.confidence
    });

  } catch (error) {
    console.error("Prediction error:", error.message);

    // Handle ML service failures gracefully
    return res.status(500).json({
      error: "Failed to analyze text. ML service unavailable."
    });
  }
});

module.exports = router;