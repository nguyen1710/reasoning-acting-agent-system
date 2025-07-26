import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { Route, Routes } from 'react-router-dom'
import { Toaster } from "react-hot-toast";
import HomePage from './pages/HomePage'
import SignUpPage from './pages/SignUpPage'
import LoginPage from './pages/LoginPage'
import Navbar from './components/Navbar';
function App() {
  const [count, setCount] = useState(0)

  return (
    <div >
      <Navbar />

      <Routes>
          <Route path="/" element={<HomePage /> } />
          <Route path="/signup" element={<SignUpPage /> } />
          <Route path="/login" element={<LoginPage /> } />
          {/* <Route path="/" element={<SettingsPage /> } />
          <Route path="/" element={<ProfilePage /> } /> */}
      </Routes>
       
       <Toaster/>
    </div>
  )
}

export default App
