import { useState } from "react";
import axios from "axios";

export default function Analyzer() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyze = async () => {
    if (!text.trim()) return;

    setLoading(true);
    setResult(null);

    try {
      const res = await axios.post(
        "http://localhost:5000/analyze",
        { text }
      );
      setResult(res.data.prediction);
    } catch {
      setResult("ERROR");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div className="label">📰 Enter News Headline</div>

      <textarea
        placeholder="📰 Paste Breaking News or Script Draft..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <button onClick={analyze} disabled={loading}>
        {loading ? "Checking..." : "✅ Check News"}
      </button>

      {result && (
        <div
          className={`result ${
            result === "REAL" ? "real" : "fake"
          }`}
        >
          {result === "REAL" ? "✅ REAL NEWS" : "❌ FAKE NEWS"}
        </div>
      )}
    </>
  );
}