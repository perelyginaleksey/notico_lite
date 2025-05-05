user-start_cmd =
    Hi!👋
    I am 🤖Notico — your assistant. I will help you not to forget urgent tasks and important dates.
    Set up events, and I’ll remind you about them on time.

    First of all, select a language so we can understand each other more easily!🌍

user-chose_language =
    Great🎉

    Set:
    — language: <b>{ $language }</b>.

    👀<b>Finally</b>, to ensure you receive timely reminders, please set your time zone by sending the name of your city or any other city matching your time.

user-chose_utc =
    Timezone successfully set🎉

    ⚙️ Current settings:

    — <i>language:</i> <b>{ $language }</b>
    — <i>timezone:</i> <b>{ $utc_text }</b>
    — <i>local time and date:</i> <b>{ $time }</b>
    — <i>time format:</i> <b>{ $format }h</b>

    If the information is correct, press the corresponding button, or edit the data👇

user_error_utc =
    😵‍💫Error!

    "<b>{ $message }</b>" - is either misspelled or such a time zone does not exist.

    😌Please try again.

user-back_chose_language = 🔙 Change language
user-back_chose_timezone = 🔙 Change time zone
user-confirm = 🚀 Yes, let’s go

menu_main_no =
    <b>⌚️Create a new reminder to make sure you don’t forget anything!</b>

    <i>example reminders:</i>
    <blockquote>{ $ex1 }</blockquote>
    <blockquote>{ $ex2 }</blockquote>
    <blockquote>{ $ex3 }</blockquote>

menu_main_yes =
    <b>⌚️Create a new reminder to make sure you don’t forget anything!</b>

    📢Next reminder:
    { $title } — { $time }

    <i>example reminders:</i>
    <blockquote>{ $ex1 }</blockquote>
    <blockquote>{ $ex2 }</blockquote>
    <blockquote>{ $ex3 }</blockquote>

menu_main_new =
    <b>📌Create a new reminder to make sure you don’t forget anything!</b>

    🔻You can add new reminders from the main menu, in the "Reminders" section, or by using the "add" button. Just send:
    <blockquote>{ $ex1 }</blockquote>
    <blockquote>{ $ex2 }</blockquote>
    <blockquote>{ $ex3 }</blockquote>

    🔻To add a note, send the text without specifying a time and press "save as note".

    🔻You can view your reminders and notes by pressing the corresponding buttons.
    There, you can also edit them, change reminder statuses (active/inactive), time, and so on.

    🔻In settings, you can change language, timezone, and time format.

    ❗️It is recommended to familiarize yourself with the detailed information about the bot’s functions in the "Information and Help" section before using it.

menu_main = { $title_key ->
    *[no] {menu_main_no}
    [yes] {menu_main_yes}
    [new] {menu_main_new}
}

menu_main_button = 🏠 Menu
menu_add = ➕ Add
menu_list_reminders = ⏰ Reminders
menu_list_notes = 📜 Notes
support_button = 😇 Support Notico
support_info_button = ❓ Information and Help
menu_settings = ⚙️ Settings
invoice_title = Help Notico
invoice_description = Donation amount: { $donation_amount }⭐️
user_support_text =
    Thank you for your interest in the project and for wanting to support it❤️

    To donate via Telegram ⭐️, press the button you prefer or send the desired amount.

error_successful_pay = Error processing payment.
error_invite_stars = Error: the amount must be a number only!
get_stars_error = Error: limit exceeded, maximum is 100000⭐️
pay_stars_button = Pay
cancel_pay_start_button = Cancel purchase
successful_payment =
    🤩Thank you for your donation!
    Your contribution is very important to me❤️

user_info_support = Would you like to explore information or get help?👇
user_info_button = 📖 Information
user_support_button = 🤝 Help
user_select_info =
    🔸You can add new reminders from the main menu, in the "Reminders" section, or by tapping the "Add" button.
    Simply send the reminder text and the time.

    🔸Time can be written in different formats, for example: <blockquote>9.15 — 9:15 — 9 15</blockquote>
    Formats:
    <blockquote>— today at 9 am, at 9 pm
    — tomorrow at 20
    — May 15th at 18:00
    — January 10, 2027 at 10:30
    — January 21, 2026 at 11:00
    — tomorrow at 2 am
    — Friday at 17:15
    — in 2 hours / 3 days / 3 weeks, etc.
    — Thursday morning (9:00 am by default)
    — tonight (7:00 pm by default)
    — tomorrow afternoon (3:00 pm by default)
    — today at noon (1:00 pm by default)
    — every day at 8:00 pm
    — every Friday at 9 am
    — every 15th day at 10 am check the account
    — every July 21st in the morning congratulate with Birthday</blockquote>

    🔸To create a recurring reminder, simply add the word "every".
    Example:
    <blockquote>"Do exercise tomorrow every 2 hours"</blockquote>

    ❗️Important.
    <blockquote>If you have trouble setting up a recurring reminder correctly, set the date first and then the recurrence.</blockquote>

    🔸The 🔄 button for reminders with periodicity resets the time to the current one, allowing you to shift the reminder time.
    ❗️Important.
    <blockquote>This is suitable for dynamic reminders when you need to shift the reminder time.
    However, if you have a reminder set, for example, to pay for internet every 5th of the month, it’s better not to press the button, as the time will reset to the current one, and you’ll need to set the reminder time again.</blockquote>

    🔸To add a note, send the text without specifying the time and press "Save as note".

    🌝If you have any questions or suggestions, contact us: @notico_support

user_select_help =
    🌝If you have any questions or suggestions, contact us: @notico_support

user_settings =
    ⚙️Current settings:

    — <i>language:</i> <b>{ $language }</b>
    — <i>time zone:</i> <b>{ $city }</b>
    — <i>local date and time:</i> <b>{ $time }</b>
    — <i>time format:</i> <b>{ $format }h</b>

    If you want to change any details, press the corresponding button👇

cancel_state = Cancelled!
user_back = 🔙 Back
user_language = 🌍 Language
user_utc = 🕑 Time zone
user_changes_language = To change the language, click on the appropriate button👇
user_changes_utc =
    🤓To change your time zone, please enter the name of the city that matches your time.

user_confirm_new_utc =
    🔍Found!

    — Time zone: <b>{ $utc_text }</b>
    — Local time and date: <b>{ $time }</b>

    Set a new time zone?👇

user_confirm_new_utc_button = 🚀Set it
user_format = 🔀 Format
send_channel_follow =
    To stay updated with the bot news, subscribe to our channel! 📢

    <i>💡Link to the channel 👉 </i> <a href="https://t.me/notico_news">Notico News</a>

check_follow_button = ✅ Check follow
check_follow_unsuccessfully_text = You are not subscribed to the channel, please try again.
check_follow_success_text =
    Thank you for your subscription!🫶
    Now you’ll be the first to know about news, updates, and useful bot information💬✨

no_thanks_text = ❌ No, thanks
user_list_reminders = ⏰Reminder List:
user_list_reminders_empty =
    🥲The reminder list is empty.

    Shall we try to add one?👇

user_title_reminders = { $title_key ->
    *[empty] {user_list_reminders_empty}
    [list] {user_list_reminders}
}

user_pre_add_reminder =
    To add a reminder, simply send the title and time.
    You can enter it in one message, for example: "Read a book today at 10 pm" or "Exercise tomorrow at 7 am."

    <i>Just a reminder that you can add reminders this way from the main menu, reminders list, etc.</i>

user_today_at = today at
user_tomorrow_at = tomorrow at
user_day_after_tomorrow_at = the day after tomorrow at
user_add_reminder =
    📅Adding a reminder.

    Text:
    <b><i>{ $title }</i></b>

    Time:
    <b><i>{ $date }</i></b>

    Repeat:
    <b><i>{ $every }</i></b>

    😉Is everything correct? I’m ready to remind you, just waiting for confirmation.

set_period = 🔁 Set repeat
change_period = 🔁 Change repeat
user_confirm_edit_time =
    New time:
    <b><i>{ $date }</i></b>

    😉Is everything correct?

user_confirm_edit_period =
    New periodicity:
    <b><i>{ $new_every }</i></b>

    😉Is everything correct?

user_confirm_reminder = 🚀 Yes
user_call_answer = 🔔Reminder added, and I’ll notify you on time!
user_error_reminder_not_future_date =
    💫Invalid time in the text.

    Text:
    <b><i>{ $title }</i></b>

    Check the possible formats and send a valid reminder time, or save the text as a note👇

user_error_edit_not_future_date =
    💫Invalid time in the text.

    Text:
    <b><i>{ $text }</i></b>

    Try again👇

user_error_reminder_no_date =
    👀Time is missing in the text.

    Text:
    <i><b>{ $title }</b></i>

    Check the possible formats and send a valid reminder time, or save the text as a note👇

user_time_formats =
    🔸Time can be written in different formats, for example: <blockquote>9.15 — 9:15 — 9 15</blockquote>
    Formats:
    <blockquote>— today at 9 am, at 9 pm
    — tomorrow at 20
    — May 15th at 18:00
    — January 10, 2027 at 10:30
    — January 21, 2026 at 11:00
    — tomorrow at 2 am
    — Friday at 17:15
    — in 2 hours / 3 days / 3 weeks, etc.
    — Thursday morning (9:00 am by default)
    — tonight (7:00 pm by default)
    — tomorrow afternoon (3:00 pm by default)
    — today at noon (1:00 pm by default)
    — every day at 8:00 pm
    — every Friday at 9 am
    — every 15th day at 10 am check the account
    — every July 21st in the morning congratulate with Birthday</blockquote>

    🔸To create a recurring reminder, simply add the word "every".
    For example:
    <blockquote>"Do exercises every 2 hours tomorrow morning"</blockquote>

    ❗️Important.
    <blockquote>If you have trouble setting up a recurring reminder correctly, set the date first and then the recurrence.</blockquote>

user_error_edit_no_date =
    👀Time is missing in the text.

    Text:
    <i><b>{ $text }</b></i>

    Try again👇

user_error_reminder =
    { $title_key ->
    *[text] {user_error_reminder_no_date}
    [past] {user_error_reminder_not_future_date}
}

user_error_edit_time =
    { $title_key ->
    *[text] {user_error_edit_no_date}
    [past] {user_error_edit_not_future_date}
}

user_error_edit_period =
    👀Couldn’t recognize the repeat periodicity.

    Text:
    <i><b>{ $text }</b></i>

    Try again👇

user_edit_time =
    Set time:
    <b><i>{ $base_time }</i></b>

    Send the new time👇

user_edit_period =
    Set repeat:
    <b><i>{ $every }</i></b>

    Send the new time👇
    <blockquote>example: every hour</blockquote>

reminder_error_button_name = Change title
reminder_error_button_formats = Formats
reminder_error_button_note = Save as note

user_list_notes = 📜Note List:
user_list_notes_empty =
    🥲The note list is empty.

    Shall we try to add one?👇

user_title_notes = { $title_key ->
    *[empty] {user_list_notes_empty}
    [list] {user_list_notes}
}

user_pre_add_note =
    First, send the text, then the note title.

user_add_note =
    📝Adding a note

    Title:
    <b><i>{ $title }</i></b>

    Text:
    <b><i>{ $text }</i></b>

    To continue, send the note title👇

user_confirm_note =
    📝Adding a note

    Title:
    <b><i>{ $title }</i></b>

    Text:
    <b><i>{ $text }</i></b>

    Everything is ready now, save?👇

edit_button = ✍️ Edit
user_selected_note = { $text }
user_edit_name =
    <code>{ $title }</code>

    Send a new title for editing👇

user_edit_text_note =
    <code>{ $text }</code>

    Send new text for editing👇

user_edit_note =
    Title:
    <b><i>{ $title }</i></b>

    Text:
    <b><i>{ $text }</i></b>

edit_name_button = 🏷 Title
edit_text_button = 📜 Text
edit_time_button = ⏳ Time
edit_period_button = 🔁 Repeat
button_refresh = 🔄 Refresh
user_selected_reminder =
    🏷Title: <b><i>{ $title }</i></b>

    📨Time: <b><i>{ $time }</i></b>

    Notification schedule:
    <b><i>{ $time }</i></b>

    Repeat: <b><i>{ $every }</i></b>

    👇Change status

user_edit_reminder =
    🏷Title: <b><i>{ $title }</i></b>

    📨Time: <b><i>{ $time }</i></b>

    Notification schedule:
    <b><i>{ $time }</i></b>

    Repeat: <b><i>{ $every }</i></b>

user_del_reminder_button = 🗑 Delete
reminder_active_button = 🔊 Active
reminder_inactive_button = 🔇 Inactive
user_reminder_status_button = { $status_key ->
    *[active] {reminder_active_button}
    [inactive] {reminder_inactive_button}
}

user_switch_status_no_alert = ⚠️Error! Reminder time has passed, set a new one.
user_error_recover = ⚠️Recovery error! More than 2 hours have passed.
user_error_recover_15 = ⚠️Recovery error! More than 15 minutes have passed.
user_delete_reminder =
    😵The reminder was removed from the list.

    Deleted by mistake?👇

user_delete_note =
    😵The note was successfully deleted.

    Deleted by mistake?👇

recover_reminder_button = 💊 Restore
next_send_reminder = next notification:
user_get_reminder =
    🔔 <b>{ $title }</b>

    📨 {next_send_reminder}
    — { $time }

user_update_not_period = Unavailable! No repeat period set
reminder_rescheduled =
    👌Alright!

    I’ll remind you about <b><i>{ $title }</i></b> — <b><i>{ $time }</i></b>.

reminder_inactive_text = <i><s>{ $time }</s></i> (inactive)
reminder_past_text = <i><s>{ $time }</s></i> (past, will be deleted soon)
reminder_button_5m = 5m
reminder_button_15m = 15m
reminder_button_30m = 30m
reminder_button_1h = 1h
reminder_button_1d = 1d
reminder_button_time = ⌛️ Time
reminder_button_del = 🗑 Delete
reminder_button_menu = 🏠 Menu
start_group_yes =
    Bot is set up!🎉
    Add a reminder via the command <code>/rem</code>.
    Example: <code>/rem Report today at 7 pm</code>
    You can also add reminders directly in the bot in the "Group Reminders" section.

start_group_no =
    The bot is not ready to work in this group!
    Complete the setup in the bot — @NoticoBot, in the "Group Reminders" section.

    <blockquote>In the future, you can add reminders via the <code>/rem</code> command in the group chat.
    Example: <code>/rem Report today at 7 pm</code>
    You can also add reminders directly in the bot in the "Group Reminders" section.</blockquote>

rem_group = The command is used to add reminders only in group chats!
rem_group_mem = Only group administrators can add reminders!
rem_group_empty = Empty message! Example: <code>/rem Report today at 7 pm</code>
text_group_error = Incorrect reminder.
text_group_no_date = Date not found in the text, try again.
reminder_group_cancel = ❌ Cancel
text_group_incorrect = Incorrect time in the reminder.
time_group_expired = Confirmation time has expired.
confirm_group_reminder = Reminder <b><i>{ $title }</i></b> confirmed and will be sent at <b><i>{ $time }</i></b>!
rem_group_mem_alert = Only administrators can interact with reminders!

group_reminder_expired = The reminder date has already passed, add a new reminder.
group_reminder_main_button = ⌚️ Group Reminders
menu_group_empty =
    🥲Your group list is empty.

    Press the button below and add Notico to a group or do it manually.

    Then press 🔄 refresh and select your group from the list to continue setup.
    ❗️If the bot is already in the group and doesn’t appear in the list, send the <code>/check</code> command in the group and 🔄 refresh the list.
    This will work if you are an administrator in the group.
    ❔Select the desired group for initial setup or to add new reminders.

menu_group_extra =
    ❗️If the bot is already in the group and doesn’t appear in the list, send the <code>/check</code> command in the group and 🔄 refresh the list.
    This will work if you are an administrator in the group.
    ❔Select the desired group for initial setup or to add new reminders.

menu_group_list =
    💬Group List:

menu_group = { $title_key ->
    *[empty] {menu_group_empty}
    [list] {menu_group_list}
}

send_group = Add to group
group_start =
    Setting up the group to enable sending reminders.

    Select the bot’s language for the group👇

group_chose_language =
    Great🎉

    Set:
    — language: <b>{ $language }</b>.

    👀Send the name of a city matching the time zone the bot should use in the group.

group_chose_utc =
    Timezone successfully set🎉

    ⚙️Current group settings:

    — <i>language:</i> <b>{ $language }</b>
    — <i>timezone:</i> <b>{ $utc_text }</b>
    — <i>local time and date:</i> <b>{ $time }</b>

    If the information is correct, press the corresponding button, or edit the data👇

select_group =
    Selected group:

    <b>{ $chat_name }</b> — id(<code>{ $chat_id }</code>)

group_check_new =
    Access granted! Add a reminder via the command <code>/rem</code>.
    Example: <code>/rem Report today at 7 pm</code>

group_check_old =
    Access already granted! Add a reminder via the command <code>/rem</code>.
    Example: <code>/rem Report today at 7 pm</code>

group_list_reminders = ⏰Reminder List in group "{ $name }":
group_list_reminders_empty =
    🥲The reminder list in group "{ $name }" is empty.

    Shall we try to add one?👇

group_title_reminders = { $title_key ->
    *[empty] {group_list_reminders_empty}
    [list] {group_list_reminders}
}

group_settings =
    ⚙️Current group settings:

    — <i>language:</i> <b>{ $language }</b>
    — <i>timezone:</i> <b>{ $utc_text }</b>
    — <i>local time and date:</i> <b>{ $time }</b>

    If you want to change any details, press the corresponding button👇

user_pre_add_reminder_group =
    To add a reminder to a group, simply send the title and time.
    You can enter it in one message, for example: "Meeting today at 10 pm" or "Work report every day at 7:30 pm."

    <i>Just a reminder that you can add reminders directly in the group with the <code>/rem</code> command.</i>
    <i>Type the <code>/rem</code> command + reminder.</i>
    <i>Example: <code>/rem Work report every day at 7:30 pm</code></i>

user_delete_reminder_group =
    😵The reminder was removed from the list.

user_add_reminder_group =
    📅Adding a reminder to group "{ $name }".

    Text:
    <b><i>{ $title }</i></b>

    Time:
    <b><i>{ $date }</i></b>

    Repeat:
    <b><i>{ $every }</i></b>

    😉Is everything correct? I’m ready to remind you, just waiting for confirmation.