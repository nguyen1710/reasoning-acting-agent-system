import ChatHeader from "./ChatHeader";
import TextInput from "./TextInput";
import { formatMessageTime } from "~/lib/utils";
import AvatarAgent from "~/assets/img/agent-avt.png"

const ChatContainer = () => {
  // Dữ liệu mẫu để hiển thị UI
  const authUser = {
    _id: "1",
    profilePic: "https://randomuser.me/api/portraits/men/1.jpg",
  };

  const selectedUser = {
    _id: "2",
    profilePic: AvatarAgent,
  };

  const messages = [
    {
      _id: "msg1",
      senderId: "1",
      text: "Hello!",
      createdAt: new Date().toISOString(),
    },
    {
      _id: "msg2",
      senderId: "2",
      text: "Hi, Tôi có thể giúp gì cho bạn?",
      createdAt: new Date().toISOString(),
    },
    {
      _id: "msg3",
      senderId: "1",
      text: "I'm good, thankssdfasdfasfasdfaskdfhalkdnsfl;kdfasfasdfaskdfhalkdnsfl;kasndf;lasfasdfaskdfhaldfasfasdfaskdfhalkdnsfl;kasndf;lasfasdfaskdfhaldfasfasdfaskdfhalkdnsfl;kasndf;lasfasdfaskdfhaldfasfasdfaskdfhalkdnsfl;kasndf;lasfasdfaskdfhaldfasfasdfaskdfhalkdnsfl;kasndf;lasfasdfaskdfhalasndf;lasfasdfaskdfhalkdnsfl;kasndf;lansdlk;fnal;sdsfasdfaskdfhalkdnsfl;kasndf;lansdlk;fnal;sdsfasdfaskdfhalkdnsfl;kasndf;lansdlk;fnal;sdnsdlk;fnal;sdnkndflnal;sdnf!",
      createdAt: new Date().toISOString(),
    },
    {
      _id: "msg4",
      senderId: "2",
      text: "Tôi không hiểu bạn nói gì?",
      createdAt: new Date().toISOString(),
    },
    {
      _id: "msg5",
      senderId: "1",
      text: "I'm good, thankssdfasdfasfasdfaskdfhalkdnsfl;kdfasfasdfaskdfhalkdnsfl;kasndf;lasfasdfaskdfhaldfasfasdfaskdfhalkdnsfl;kasndf;lasfasdfaskdfhaldfasfasdfaskdfhalkdnsfl;kasndf;lasfasdfaskdfhaldfasfasdfaskdfhalkdnsfl;kasndf;lasfasdfaskdfhaldfasfasdfaskdfhalkdnsfl;kasndf;lasfasdfaskdfhalasndf;lasfasdfaskdfhalkdnsfl;kasndf;lansdlk;fnal;sdsfasdfaskdfhalkdnsfl;kasndf;lansdlk;fnal;sdsfasdfaskdfhalkdnsfl;kasndf;lansdlk;fnal;sdnsdlk;fnal;sdnkndflnal;sdnf!",
      createdAt: new Date().toISOString(),
    },

  ];

  return (
    <div className="flex-1 flex flex-col overflow-auto">
      <ChatHeader />

      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((message) => (
          <div
            key={message._id}
            className={`chat ${message.senderId === authUser._id ? "chat-end" : "chat-start"}`}
          >
            <div className="chat-image avatar">
              <div className="size-10 rounded-full border">
                <img
                  src={
                    message.senderId === authUser._id
                      ? authUser.profilePic
                      : selectedUser.profilePic
                  }
                  alt="profile pic"
                />
              </div>
            </div>
            <div className="chat-header mb-1">
              <time className="text-xs opacity-50 ml-1">
                {formatMessageTime(message.createdAt)}
                {/* {message.createdAt} */}
              </time>
            </div>
            <div className="chat-bubble flex flex-col ">
              {message.image && (
                <img
                  src={message.image}
                  alt="Attachment"
                  className="sm:max-w-[200px] rounded-md mb-2"
                />
              )}
              {message.text && <p className="break-words">{message.text}</p>}
            </div>
          </div>
        ))}
      </div>

      <TextInput/>
    </div>
  );
};

export default ChatContainer;
