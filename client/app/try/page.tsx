"use client"

import Link from "next/link";
import { SetStateAction, useState, ChangeEvent } from "react";
// import { FileUploader } from "react-drag-drop-files";
import Lottie from "react-lottie-player";
import loader from "@/../../public/assets/loader.json";
const languageOptions: { label: string; value: string; }[] = [
  { label: "Afrikaans", value: "af-ZA" },
  { label: "Arabic", value: "ar-XA" },
  { label: "Bengali", value: "bn-IN" },
  { label: "Chinese (Simplified)", value: "zh-CN" },
  { label: "Chinese (Traditional)", value: "zh-TW" },
  { label: "English India", value: "en-IN" },
  { label: "English UK", value: "en-GB" },
  { label: "English US", value: "en-US" },
  { label: "French", value: "fr-FR" },
  { label: "German", value: "de-DE" },
  { label: "Greek", value: "el-GR" },
  { label: "Gujarati", value: "gu-IN" },
  { label: "Hindi", value: "hi-IN" },
  { label: "Kannada", value: "kn-IN" },
  { label: "Korean", value: "ko-KR" },
  { label: "Malayalam", value: "ml-IN" },
  { label: "Marathi", value: "mr-IN" },
  { label: "Punjabi", value: "pa-IN" },
  { label: "Tamil", value: "ta-IN" },
  { label: "Telugu", value: "te-IN" },
];

export default function Dashboard() {
  const [userInput, setUserInput] = useState("");
  const [file, setFile] = useState<SetStateAction<File | null>>(null);
  const handleChange = (file: File) => {
    setFile(file);
  };
  const [loading, setLoading] = useState(false);
  const [selectedLanguage, setSelectedLanguage] = useState('');

  const fileTypes = ["MP4"];

  const handleLanguageChange = (event: ChangeEvent<HTMLSelectElement>) => {
    setSelectedLanguage(event.target.value);
  };

  const clickHandler = () => {
    setLoading(true);
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        userInput: userInput,
        language: selectedLanguage,
      }),
      redirect: "follow",
    } as RequestInit;

    fetch("http://127.0.0.1:5000/", requestOptions)
      .then((response) => response.blob())
      .then((blob) => {
        const downloadUrl = URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.href = downloadUrl;
        link.setAttribute("download", "Chalchitra-ai.mp4"); // Specify the filename for the downloaded file
        document.body.appendChild(link);
        link.click();
        link.remove();

        setLoading(false);
        setUserInput("");
      })
      .catch((error) => {
        console.error("Error downloading file:", error);
        setLoading(false);
      });
  };

  return (
    <main className="flex justify-center flex-col min-h-[80vh]">
      {loading ? (
        <div className=" static backdrop-blur-sm min-h-screen flex items-center justify-center flex-col">
          <div className=" bg-white opacity-75 h-[38h] w-[38vh] rounded-lg">
            <Lottie loop animationData={loader} play className="h-[40vh]" />
          </div>
          <div className=" font-xl text-gray-500 font-semibold p-2">
            Converting...
          </div>
          <div className=" font-xl text-gray-500 font-semibold p-2">
            It might take upto several minutes, so please be patient
          </div>
        </div>
      ) : (
        <div className="flex justify-center gap-5 mt-12 drop-shadow-2xl">
          <section className="flex flex-col items-center bg-white border border-gray-200 rounded-lg shadow md:flex-row md:max-w-xl hover:bg-gray-100 h-[550px] w-[600px]">
            <div className="flex flex-col h-full w-full p-4 leading-normal">
              <label
                htmlFor="UserMessage"
                className="block text-xs font-medium text-gray-700"
              >
                Story or Ideas
              </label>

              <textarea
                rows={4}
                cols={50}
                id="UserMessage"
                placeholder="Let your imagination run wild! Describe your story or ideas here."
                value={userInput}
                className="mt-1 w-full p-4 rounded-md border-gray-300 shadow-sm sm:text-sm focus:border-indigo-200 h-full"
                onChange={(e) => setUserInput(e.target.value)}
              />
              <label
                htmlFor="languageSelect"
                className="block text-xs font-medium text-gray-700 mt-2"
              >
                Language
              </label>
              <select id="languageSelect" value={selectedLanguage} onChange={handleLanguageChange} className="w-full p-2 mt-2 rounded-md border-gray-300 shadow-sm sm:text-sm focus:border-indigo-200">
                <option value="">Select</option>
                {languageOptions.map((option) => (
                  <option key={option.value} value={option.value}>
                    {option.label}
                  </option>
                ))}
              </select>
              <button
                className="bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded drop-shadow-2xl font-poppins text-bold mt-6 "
                onClick={() => clickHandler()}
              >
                Submit
              </button>
            </div>
          </section>
        </div>
      )}
    </main>
  );
}
