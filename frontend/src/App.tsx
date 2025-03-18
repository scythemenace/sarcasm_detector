import { useState } from "react";
import "./App.css";
import useDebounce from "./components/useDebounce";

function App() {
  const [inputText, setInputText] = useState("");
  const debouncedInputText = useDebounce(inputText);

  return (
    <>
      <h1>Sarcasm Detection</h1>
      <input
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter sarcastic text"
      ></input>
      <p>{debouncedInputText}</p>
    </>
  );
}

export default App;
