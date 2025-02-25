import { GoogleOAuthProvider, GoogleLogin } from "@react-oauth/google";

interface GoogleLoginProps {
  onSuccess: (credentialResponse: { credential?: string }) => void;
  onFailure: () => void;
}

export default function GoogleLoginComponent({ onSuccess, onFailure }: GoogleLoginProps) {
  return (
    <GoogleOAuthProvider clientId="227145979883-8tabm5ujec4plc9q0ueidk5rignmoicm.apps.googleusercontent.com">
      <GoogleLogin onSuccess={onSuccess} onError={onFailure} />
    </GoogleOAuthProvider>
  );
}