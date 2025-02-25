import { useState } from "react";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import EmailPasswordLogin from "../components/NormalLogin.tsx";
import GoogleLoginComponent from "../components/GoogleLogin.tsx";
import { jwtDecode } from "jwt-decode";
import { useNavigate } from "react-router-dom";

export default function LoginPage() {
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleLogin = async (email: string, password: string) => {
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
        setTimeout(() => {
          navigate("/Successful");
        }, 1000);
      } else {
        toast.error(data.detail || "Invalid email or password.", { position: "top-center" });
      }
    } catch (err) {
      toast.error("⚠️ Unable to connect to the server.", { position: "top-center" });
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleSuccess = (credentialResponse: { credential?: string }) => {
    if (credentialResponse.credential) {
      const decoded = jwtDecode<{ name: string }>(credentialResponse.credential);
      console.log("Google User:", decoded);
      toast.success(`✅ Welcome, ${decoded.name}!`, { position: "top-center" });
    } else {
      toast.error("❌ Google Login Failed: No credential received.", { position: "top-center" });
    }
  };

  const handleGoogleFailure = () => {
    toast.error("❌ Google Login Failed.", { position: "top-center" });
  };

  return (
    <div className="flex h-screen items-center justify-center bg-gradient-to-r from-purple-600 to-blue-500">
      <ToastContainer />
      <div className="bg-white p-8 shadow-2xl rounded-2xl w-96">
        <h2 className="text-3xl font-extrabold text-center text-gray-800 mb-6">Sign In</h2>

        <EmailPasswordLogin onLogin={handleLogin} loading={loading} />

        <div className="mt-6 text-center space-y-3">
          <p className="text-gray-600 text-sm">Or login with</p>
          <GoogleLoginComponent onSuccess={handleGoogleSuccess} onFailure={handleGoogleFailure} />
        </div>
      </div>
    </div>
  );
}