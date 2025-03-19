import { useEffect, useState } from "react";
import "./App.css";
import useDebounce from "./components/useDebounce";
import axios from "axios";

const apiUrl = import.meta.env.VITE_API_URL;

function App() {
  const [inputText, setInputText] = useState("");
  const debouncedInputText = useDebounce(inputText);
  const [outputText, setOutputText] = useState("");

  useEffect(() => {
    axios
      .post(`${apiUrl}/api/analyze`, {
        text: debouncedInputText,
      })
      .then((response) => {
        setOutputText(response.data.output);
      })
      .catch((error) => {
        console.error(error);
      });
  }, [debouncedInputText]);

  return (
    <>
      <h1>Sarcasm Detection</h1>
      <input
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter sarcastic text"
      ></input>
      <p>
        Input Text:{" "}
        {debouncedInputText != "" ? debouncedInputText : "No string entered"}
      </p>
      <p>
        Output:{" "}
        {outputText == "1" && debouncedInputText != ""
          ? "Sarcastic"
          : "Not Sarcastic"}
      </p>
    </>
  );
}

export default App;
