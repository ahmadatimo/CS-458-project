import { useNavigate } from "react-router-dom";
export default function SuccessfulLogin() {
  const navigate = useNavigate();

  return (
    <div className="flex h-screen items-center justify-center bg-gradient-to-r from-green-400 to-blue-500">
      <div className="bg-white p-8 shadow-2xl rounded-2xl w-96 text-center">
        <h2 className="text-4xl font-extrabold text-gray-800 mb-4">✅ Success!</h2>
        <p className="text-gray-600 text-lg mb-6">You have successfully logged in.</p>

        <button
          className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-6 rounded-lg transition duration-300"
          onClick={() =>navigate("/")} // Change this based on navigation
        >
          Go to LoginPage
        </button>
      </div>
    </div>
  );
}
