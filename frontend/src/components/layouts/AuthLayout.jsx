// AuthLayout.jsx
import { Outlet } from "react-router-dom";

export default function AuthLayout() {
  return (
    <div className="auth-container">
      <Outlet /> {/* Chứa login/signup */}
    </div>
  );
}
