import { useState } from "react";

export default function App() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async (e: { preventDefault: () => void; }) => {
    e.preventDefault();

    // Simulating API call to FastAPI backend
    const response = await fetch("http://localhost:8000/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    const data = await response.json();
    if (response.ok) {
      alert("✅ Login Successful!");
    } else {
      setError(data.detail || "Login failed");
    }
  };

  return (
    <div className="flex h-screen items-center justify-center bg-gradient-to-r from-purple-600 to-blue-500">
      <div className="bg-white p-8 shadow-2xl rounded-2xl w-96">
        <h2 className="text-3xl font-extrabold text-center text-gray-800 mb-6">
          Sign In
        </h2>

        {error && (
          <p className="text-red-500 text-center bg-red-100 p-2 rounded-md">
            {error}
          </p>
        )}

        <form onSubmit={handleLogin} className="space-y-4">
          <input
            type="email"
            placeholder="Email"
            className="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <input
            type="password"
            placeholder="Password"
            className="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button
            type="submit"
            className="w-full bg-blue-500 text-white p-3 rounded-lg font-semibold hover:bg-blue-600 transition duration-300"
          >
            Login
          </button>
        </form>

        <div className="mt-6 text-center space-y-3">
          <p className="text-gray-600 text-sm">Or login with</p>
          <button className="w-full bg-red-500 text-white p-3 rounded-lg font-semibold hover:bg-red-600 transition duration-300">
            Login with Google
          </button>
          <button className="w-full bg-blue-700 text-white p-3 rounded-lg font-semibold hover:bg-blue-800 transition duration-300">
            Login with Facebook
          </button>
        </div>

        <p className="mt-4 text-center text-gray-500 text-sm">
          Don't have an account?{" "}
          <a href="#" className="text-blue-500 font-semibold hover:underline">
            Sign up
          </a>
        </p>
      </div>
    </div>
  );
}
