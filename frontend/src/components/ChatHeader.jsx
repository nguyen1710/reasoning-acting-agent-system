import { X } from "lucide-react";

const ChatHeader = () => {
  // Dữ liệu mẫu để hiển thị UI
  const selectedUser = {
    _id: "2",
    fullName: "AI Agent",
    profilePic: "https://play-lh.googleusercontent.com/kyqwKigFeMK--sLP227HkpbZuICH5FR9oh1UiND4ly_IdnySC1axnCzSu3yXkpWE2Jc",
    online: true
  };

  return (
    <div className="p-2.5 border-b border-base-300">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          {/* Avatar */}
          <div className="avatar">
            <div className="size-10 rounded-full relative">
              <img src={selectedUser.profilePic} alt={selectedUser.fullName} />
            </div>
          </div>

          {/* User info */}
          <div>
            <h3 className="font-medium">{selectedUser.fullName}</h3>
            <p className="text-sm text-base-content/70">
              {selectedUser.online ? "Online" : "Offline"}
            </p>
          </div>
        </div>

        {/* Close button - không có xử lý */}
        <button>
          <X />
        </button>
      </div>
    </div>
  );
};

export default ChatHeader;
