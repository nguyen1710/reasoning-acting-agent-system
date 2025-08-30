/* eslint-disable no-unused-vars */
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { Route, Routes } from 'react-router-dom'
import { AuthProvider } from './hooks/AuthProvider'
import { Toaster } from "react-hot-toast";
import HomePage from './pages/HomePage'
import SignUpPage from './pages/SignUpPage'
import LoginPage from './pages/LoginPage'
import Navbar from './components/Navbar';
import { useAuth } from './hooks/AuthProvider'
import ProtectedRoute from './hooks/ProtectedRoute'
import AuthLayout from './components/layouts/AuthLayout'
import AppLayout from './components/layouts/AppLayout'
function App() {
  const [count, setCount] = useState(0)

  return (
    <div >
     <AuthProvider>
       <Routes>
      {/* Auth Layout */}
      <Route element={<AuthLayout />}>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/signup" element={<SignUpPage />} />
      </Route>

      {/* App Layout (có navbar) */}
      <Route element={<AppLayout />}>
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <HomePage />
            </ProtectedRoute>
          }
        />
      </Route>
    </Routes>
     </AuthProvider>
     <Toaster duration='5000'/>
    </div>
  )
}

export default App
