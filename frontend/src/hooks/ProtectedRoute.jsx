import { Navigate } from "react-router-dom";
import { useAuth } from "./AuthProvider";
import Loading from "../components/Loading";

export default function ProtectedRoute({ children }) {
  const { authUser, isCheckingAuth } = useAuth();

  if (isCheckingAuth) 
    return <Loading/>
      


  return authUser ? children : <Navigate to="/login" replace />;
}
