from aiogram.fsm.state import State, StatesGroup


class StartBot(StatesGroup):
    choice_language = State()
    choice_utc = State()
    confirm_settings = State()
    error_utc = State()


class MainMenu(StatesGroup):
    main_menu = State()


class UserSupport(StatesGroup):
    user_support = State()


class UserInfo(StatesGroup):
    user_support_info = State()
    user_select_support = State()
    user_select_info = State()


class UserSettings(StatesGroup):
    user_settings = State()
    user_changes_language = State()
    user_changes_utc = State()
    user_confirm_utc = State()
    user_error_utc = State()


class UserReminders(StatesGroup):
    user_reminders_main_window = State()
    user_pre_add_reminder = State()
    user_add_reminder = State()
    user_error_add_reminder = State()
    user_time_formats = State()
    user_selected_reminder = State()
    user_edit_reminder = State()
    user_edit_name_reminder = State()
    user_edit_time_reminder = State()
    user_error_edit_time_reminder = State()
    user_confirm_edit_time_reminder = State()
    user_edit_period_reminder = State()
    user_error_edit_period_reminder = State()
    user_confirm_edit_period_reminder = State()
    user_delete_reminder = State()
    user_follow_channel = State()
    send_settings = State()
    reminder_preview = State()
    add_buttons = State()
    preview_reminders = State()


class GroupReminders(StatesGroup):
    select_group_window = State()
    reminders_window = State()
    pre_add_reminder = State()
    add_reminder = State()
    confirm_reminder = State()
    error_add_reminder = State()
    selected_reminder = State()
    time_formats = State()
    edit_reminder = State()
    edit_name_reminder = State()
    edit_time_reminder = State()
    error_edit_time_reminder = State()
    confirm_edit_time_reminder = State()
    edit_period_reminder = State()
    error_edit_period_reminder = State()
    follow_channel = State()
    confirm_edit_period_reminder = State()
    send_settings = State()
    reminder_preview = State()
    add_buttons = State()
    preview_reminders = State()


class GroupMenu(StatesGroup):
    main_window = State()
    add_group = State()
    select_group = State()


class GroupStart(StatesGroup):
    choice_language = State()
    choice_utc = State()
    confirm_settings = State()
    error_utc = State()


class GroupSettings(StatesGroup):
    window_settings = State()
    changes_language = State()
    changes_utc = State()
    error_utc = State()
    confirm_utc = State()
