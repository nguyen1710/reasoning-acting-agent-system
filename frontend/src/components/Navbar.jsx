import React from 'react'
import { LogOut, Bot , Settings, User } from "lucide-react";
import { Link } from "react-router-dom";
import { axiosInstance } from '../lib/axios';
import { useAuth } from '../hooks/AuthProvider';
import { useState } from 'react';
function Navbar() {
   const [loading, setLoading] = useState(false);
    const { setAuthUser } = useAuth(); // 👈 để lưu user vào context

    const handleLogout = async () => {
    try {
      await axiosInstance.post("/auth/logout");
      setAuthUser(null); // clear user trong context
    } catch (err) {
      console.error("Logout error:", err);
    }
  };
  return (
    <header
      className="bg-base-100 border-b border-base-300 fixed w-full top-0 z-40 
    backdrop-blur-lg bg-base-100/80"
    >
      <div className=" w-full px-6 h-16">
        <div className="flex items-center justify-between h-full">
          <div className="flex items-center gap-8">
            <Link to="/" className="flex items-center gap-2.5 hover:opacity-80 transition-all">
              <div className="size-9 rounded-lg bg-primary/10 flex items-center justify-center">
                <Bot className="w-7 h-7 text-primary" />
              </div>
              <h1 className="text-lg font-bold">AI Agent</h1>
            </Link>
          </div>

          <div className="flex items-center gap-2">
            <Link
              to={"/settings"}
              className={`
              btn btn-sm gap-2 transition-colors
              
              `}
            >
              <Settings className="w-4 h-4" />
              <span className="hidden sm:inline">Settings</span>
            </Link>

              <>
                <Link to={"/profile"} className={`btn btn-sm gap-2`}>
                  <User className="size-5" />
                  <span className="hidden sm:inline">Profile</span>
                </Link>

                <button className="flex gap-2 items-center" onClick={handleLogout}>
                  <LogOut className="size-5" />
                  <span className="hidden sm:inline">Logout</span>
                </button>
              </>

          </div>
        </div>
      </div>
    </header>
  )
}

export default Navbar