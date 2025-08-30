import { createContext, useContext, useState, useEffect } from "react";
import {axiosInstance} from "../lib/axios.js";
import {useNavigate} from 'react-router-dom'
const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [authUser, setAuthUser] = useState(null);
  const [isCheckingAuth, setIsCheckingAuth] = useState(true);
    const navigate = useNavigate()
  // Hàm checkAuth (thay thế cho Zustand)
  const checkAuth = async () => {
    try {
      const res = await axiosInstance.get("/auth/checkAuth");
      setAuthUser(res.data); // Nếu thành công, lưu user
    } catch (error) {
      console.log("Error in checkAuth:", error);
      setAuthUser(null); // Nếu lỗi, user = null
      // if(window.location.pathname !== "/signup") {
      //   navigate('/login')
      // }
    } finally {
      setIsCheckingAuth(false); // Dù thành công hay lỗi đều báo xong
    }
  };

  // Khi App load lần đầu thì kiểm tra đăng nhập
  useEffect(() => {
    checkAuth();
  }, []);

  return (
    <AuthContext.Provider
      value={{ authUser, isCheckingAuth, checkAuth, setAuthUser }}
    >
      {children}
    </AuthContext.Provider>
  );
}

// Hook tiện lợi để dùng ở component
export const useAuth = () => useContext(AuthContext);
