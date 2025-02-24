import { useState } from "react";
import { ToastContainer, toast } from "react-toastify";
import { GoogleOAuthProvider, GoogleLogin } from "@react-oauth/google";
import { jwtDecode } from "jwt-decode";
import "react-toastify/dist/ReactToastify.css";

export default function App() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e: { preventDefault: () => void; }) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await fetch("http://localhost:8000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      const data = await response.json();
      if (response.ok) {
        toast.success("✅ Login Successful!", { position: "top-center" });
      } else {
        toast.error(data.detail || "Invalid email or password.", { position: "top-center" });
      }
    } catch (err) {
      toast.error("⚠️ Unable to connect to the server.", { position: "top-center" });
    } finally {
      setLoading(false);
    }
  };

  // Handle Google login success
  const handleGoogleSuccess = (credentialResponse: { credential?: string }) => {
    if (credentialResponse.credential) {
      const decoded = jwtDecode<{ name: string }>(credentialResponse.credential);
      console.log("Google User:", decoded);
      toast.success(`✅ Welcome, ${decoded.name}!`, { position: "top-center" });

      // TODO: Send Google token to backend for verification
    } else {
      toast.error("❌ Google Login Failed: No credential received.", { position: "top-center" });
    }
  };

  // Handle Google login failure
  const handleGoogleFailure = () => {
    toast.error("❌ Google Login Failed.", { position: "top-center" });
  };

  return (
      <div className="flex h-screen items-center justify-center bg-gradient-to-r from-purple-600 to-blue-500">
        <ToastContainer />
        <div className="bg-white p-8 shadow-2xl rounded-2xl w-96">
          <h2 className="text-3xl font-extrabold text-center text-gray-800 mb-6">
            Sign In
          </h2>

          <form onSubmit={handleLogin} className="space-y-4">
            <input
              name = "email"
              type="email"
              placeholder="Email"
              className="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <input
              name = "password"
              type="password"
              placeholder="Password"
              className="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <button
              name = "Submit"
              type="submit"
              className="w-full bg-blue-500 text-white p-3 rounded-lg font-semibold hover:bg-blue-600 transition duration-300"
              disabled={loading}
            >
              {loading ? "Logging in..." : "Login"}
            </button>
          </form>

          <div className="mt-6 text-center space-y-3">
            <p className="text-gray-600 text-sm">Or login with</p>
            <GoogleOAuthProvider clientId="227145979883-8tabm5ujec4plc9q0ueidk5rignmoicm.apps.googleusercontent.com">
              <GoogleLogin onSuccess={handleGoogleSuccess} onError={handleGoogleFailure} />   
            </GoogleOAuthProvider>
          </div>
        </div>
      </div>
  );
}
