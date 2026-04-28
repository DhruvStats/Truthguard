import Analyzer from "./components/Analyzer";
import "./index.css";

export default function App() {
  return (
    <div className="app">
      <div className="title">
        TruthGuard for Newsrooms 🛡️
      </div>

      <div className="subtitle">
        Real‑time AI verification to protect editorial integrity and prevent misinformation🌍
      </div>

      <Analyzer />
    </div>
  );
}