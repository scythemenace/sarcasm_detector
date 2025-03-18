import { useEffect, useState } from "react";

const useDebounce = (value: string, delay: number = 1000) => {
  const [returnValue, setReturnValue] = useState("");

  useEffect(() => {
    const timer = setTimeout(() => {
      setReturnValue(value);
    }, delay);

    return () => {
      clearTimeout(timer);
    };
  }, [value, delay]);

  return returnValue;
};

export default useDebounce;
