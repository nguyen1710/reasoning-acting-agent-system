// AppLayout.jsx
import { Outlet } from "react-router-dom";
import Navbar from "~/components/Navbar";

export default function AppLayout() {
  return (
    <div>
      <Navbar />
      <main>
        <Outlet /> {/* Chứa HomePage, Dashboard,... */}
      </main>
    </div>
  );
}
