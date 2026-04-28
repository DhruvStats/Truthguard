import express from "express";
import axios from "axios";
import Result from "../models/Result.js";

const router = express.Router();

router.post("/", async (req, res) => {
    try {
        const { text } = req.body;

        const mlResponse = await axios.post(
            "http://localhost:8000/predict",
            { text }
        );

        const savedResult = await Result.create({
            text,
            prediction: mlResponse.data.prediction,
            confidence: mlResponse.data.confidence
        });

        res.json(mlResponse.data);
    } catch (error) {
        res.status(500).json({ error: "Prediction failed" });
    }
});

export default router;