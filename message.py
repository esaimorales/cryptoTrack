import applescript

script = applescript.AppleScript('''
    on run {targetBuddyPhone, targetMessage}
        tell application "Messages"
            set targetService to 1st service whose service type = iMessage
            set targetBuddy to buddy targetBuddyPhone of targetService
            send targetMessage to targetBuddy
        end tell
    end run ''')

def sendMessage(phone_number, message):
    script.run(phone_number, message)
