import { NotebookTabs  } from "lucide-react";

const Sidebar = () => {
  // Dữ liệu mẫu đơn giản để hiển thị UI
  const histories = [
    {
      _id: "1",
      chatHistory: [
        "Nội dung 1",
        "Nội dung 2"
      ]
    },

    {
      _id: "1",
      chatHistory: [
        "Nội dung 1",
        "Nội dung 2"
      ]
    },
  ];

  return (
    <aside className="h-full w-20 lg:w-72 border-r border-base-300 flex flex-col transition-all duration-200">
      <div className="border-b border-base-300 w-full p-5">
        <div className="flex items-center gap-2">
          <NotebookTabs className="size-6" />
          <span className="font-medium hidden lg:block">Lịch sử đoạn chat</span>
        </div>
      </div>

      <div className="overflow-y-auto w-full py-3">
        {histories.map((history) => (
          <button
            key={history._id}
            className={`
              w-full p-3 flex items-center gap-3
              hover:bg-base-300 transition-colors
            `}
          >
            {/* <div className="relative mx-auto lg:mx-0">
              <img
                src={user.profilePic}
                alt={user.fullName}
                className="size-12 object-cover rounded-full"
              />
              {user.online && (
                <span
                  className="absolute bottom-0 right-0 size-3 bg-green-500 
                  rounded-full ring-2 ring-zinc-900"
                />
              )}
            </div> */}

            <div className="hidden lg:block text-left min-w-0">
              <div className="font-medium truncate">{history.chatHistory[0]}</div>
            </div>
          </button>

        ))}
      </div>
    </aside>
  );
};

export default Sidebar;
