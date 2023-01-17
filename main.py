from screen_manager import ScreenManager, Message

manager = ScreenManager()

message1=Message(1, "message 1", 2)
message2=Message(2, "message 2")
message3=Message(0, "message 3")

manager.print(message1)
manager.print(message2)
manager.print(message3)