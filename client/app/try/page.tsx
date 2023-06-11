"use client"

import Link from "next/link";
import { SetStateAction, useState, ChangeEvent } from "react";
// import { FileUploader } from "react-drag-drop-files";
import Lottie from "react-lottie-player";
import loader from "@/../../public/assets/loader.json";
const languageOptions: { label: string; value: string; }[] = [
  { label: "Afrikaans", value: "af" },
  { label: "Albanian", value: "sq" },
  { label: "Amharic", value: "am" },
  { label: "Arabic", value: "ar" },
  { label: "Armenian", value: "hy" },
  { label: "Assamese", value: "as" },
  { label: "Aymara", value: "ay" },
  { label: "Azerbaijani", value: "az" },
  { label: "Bambara", value: "bm" },
  { label: "Basque", value: "eu" },
  { label: "Belarusian", value: "be" },
  { label: "Bengali", value: "bn" },
  { label: "Bhojpuri", value: "bho" },
  { label: "Bosnian", value: "bs" },
  { label: "Bulgarian", value: "bg" },
  { label: "Catalan", value: "ca" },
  { label: "Cebuano", value: "ceb" },
  { label: "Chinese (Simplified)", value: "zh-CN" },
  { label: "Chinese (Traditional)", value: "zh-TW" },
  { label: "Corsican", value: "co" },
  { label: "Croatian", value: "hr" },
  { label: "Czech", value: "cs" },
  { label: "Danish", value: "da" },
  { label: "Dhivehi", value: "dv" },
  { label: "Dogri", value: "doi" },
  { label: "Dutch", value: "nl" },
  { label: "English", value: "en" },
  { label: "Esperanto", value: "eo" },
  { label: "Estonian", value: "et" },
  { label: "Ewe", value: "ee" },
  { label: "Filipino (Tagalog)", value: "fil" },
  { label: "Finnish", value: "fi" },
  { label: "French", value: "fr" },
  { label: "Frisian", value: "fy" },
  { label: "Galician", value: "gl" },
  { label: "Georgian", value: "ka" },
  { label: "German", value: "de" },
  { label: "Greek", value: "el" },
  { label: "Guarani", value: "gn" },
  { label: "Gujarati", value: "gu" },
  { label: "Haitian Creole", value: "ht" },
  { label: "Hausa", value: "ha" },
  { label: "Hawaiian", value: "haw" },
  { label: "Hebrew", value: "he" },
  { label: "Hindi", value: "hi" },
  { label: "Hmong", value: "hmn" },
  { label: "Hungarian", value: "hu" },
  { label: "Icelandic", value: "is" },
  { label: "Igbo", value: "ig" },
  { label: "Ilocano", value: "ilo" },
  { label: "Indonesian", value: "id" },
  { label: "Irish", value: "ga" },
  { label: "Italian", value: "it" },
  { label: "Japanese", value: "ja" },
  { label: "Javanese", value: "jv" },
  { label: "Kannada", value: "kn" },
  { label: "Kazakh", value: "kk" },
  { label: "Khmer", value: "km" },
  { label: "Kinyarwanda", value: "rw" },
  { label: "Konkani", value: "gom" },
  { label: "Korean", value: "ko" },
  { label: "Krio", value: "kri" },
  { label: "Kurdish", value: "ku" },
  { label: "Kurdish (Sorani)", value: "ckb" },
  { label: "Kyrgyz", value: "ky" },
  { label: "Lao", value: "lo" },
  { label: "Latin", value: "la" },
  { label: "Latvian", value: "lv" },
  { label: "Lingala", value: "ln" },
  { label: "Lithuanian", value: "lt" },
  { label: "Luganda", value: "lg" },
  { label: "Luxembourgish", value: "lb" },
  { label: "Macedonian", value: "mk" },
  { label: "Maithili", value: "mai" },
  { label: "Malagasy", value: "mg" },
  { label: "Malay", value: "ms" },
  { label: "Malayalam", value: "ml" },
  { label: "Maltese", value: "mt" },
  { label: "Maori", value: "mi" },
  { label: "Marathi", value: "mr" },
  { label: "Meiteilon (Manipuri)", value: "mni-Mtei" },
  { label: "Mizo", value: "lus" },
  { label: "Mongolian", value: "mn" },
  { label: "Myanmar (Burmese)", value: "my" },
  { label: "Nepali", value: "ne" },
  { label: "Norwegian", value: "no" },
  { label: "Nyanja (Chichewa)", value: "ny" },
  { label: "Odia (Oriya)", value: "or" },
  { label: "Oromo", value: "om" },
  { label: "Pashto", value: "ps" },
  { label: "Persian", value: "fa" },
  { label: "Polish", value: "pl" },
  { label: "Portuguese (Portugal, Brazil)", value: "pt" },
  { label: "Punjabi", value: "pa" },
  { label: "Quechua", value: "qu" },
  { label: "Romanian", value: "ro" },
  { label: "Russian", value: "ru" },
  { label: "Samoan", value: "sm" },
  { label: "Sanskrit", value: "sa" },
  { label: "Scots Gaelic", value: "gd" },
  { label: "Sepedi", value: "nso" },
  { label: "Serbian", value: "sr" },
  { label: "Sesotho", value: "st" },
  { label: "Shona", value: "sn" },
  { label: "Sindhi", value: "sd" },
  { label: "Sinhala (Sinhalese)", value: "si" },
  { label: "Slovak", value: "sk" },
  { label: "Slovenian", value: "sl" },
  { label: "Somali", value: "so" },
  { label: "Spanish", value: "es" },
  { label: "Sundanese", value: "su" },
  { label: "Swahili", value: "sw" },
  { label: "Swedish", value: "sv" },
  { label: "Tagalog (Filipino)", value: "tl" },
  { label: "Tajik", value: "tg" },
  { label: "Tamil", value: "ta" },
  { label: "Tatar", value: "tt" },
  { label: "Telugu", value: "te" },
  { label: "Thai", value: "th" },
  { label: "Tigrinya", value: "ti" },
  { label: "Tsonga", value: "ts" },
  { label: "Turkish", value: "tr" },
  { label: "Turkmen", value: "tk" },
  { label: "Twi (Akan)", value: "ak" },
  { label: "Ukrainian", value: "uk" },
  { label: "Urdu", value: "ur" },
  { label: "Uyghur", value: "ug" },
  { label: "Uzbek", value: "uz" },
  { label: "Vietnamese", value: "vi" },
  { label: "Welsh", value: "cy" },
  { label: "Xhosa", value: "xh" },
  { label: "Yiddish", value: "yi" },
  { label: "Yoruba", value: "yo" },
  { label: "Zulu", value: "zu" },
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

    fetch("http://localhost:5000/", requestOptions)
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
      });
  };

  return (
    <main className="flex justify-center flex-col min-h-[80vh]">
      {loading ? (
        <div className=" static backdrop-blur-sm min-h-screen flex items-center justify-center flex-col">
          <div className=" bg-white opacity-75 h-[38h] w-[38vh] rounded-lg">
            <Lottie loop animationData={loader} play className="h-[40vh]" />
          </div>
          <div className=" font-xl text-white font-semibold p-2">
            Converting...
          </div>
          <div className=" font-xl text-white font-semibold p-2">
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
