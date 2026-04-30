/**
 * Analyzer component
 *
 * Responsibilities:
 * - Accept news text input
 * - Send request to backend /analyze endpoint
 * - Display prediction and confidence score
 *
 * This version:
 * ✅ Shows confidence alongside REAL/FAKE
 * ✅ Uses env-based backend URL
 * ✅ Has safe localhost fallback
 */

import { useState } from "react";

const BACKEND_URL =
  import.meta.env.VITE_BACKEND_URL || "http://localhost:5000";

function Analyzer() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [confidence, setConfidence] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const analyzeNews = async () => {
    if (!text.trim()) {
      setError("Please enter some news text.");
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);
    setConfidence(null);

    try {
      const response = await fetch(`${BACKEND_URL}/analyze`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ text })
      });

      if (!response.ok) {
        throw new Error("Backend request failed");
      }

      const data = await response.json();

      setResult(data.prediction);
      setConfidence(data.confidence);
    } catch (err) {
      setError("Failed to analyze news. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="analyzer-container">
      <h2>TruthGuard News Analyzer</h2>

      <textarea
        rows="6"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Paste news text here..."
      />

      <button onClick={analyzeNews} disabled={loading}>
        {loading ? "Analyzing..." : "Check News"}
      </button>

      {error && <p className="error">{error}</p>}

      {result && (
        <div className="result">
          <h3>
            Result:{" "}
            <span
              style={{
                color: result === "REAL" ? "green" : "red",
                fontWeight: "bold"
              }}
            >
              {result}
            </span>
          </h3>

          <p>
            Confidence: <strong>{confidence}%</strong>
          </p>
        </div>
      )}
    </div>
  );
}

export default Analyzer;