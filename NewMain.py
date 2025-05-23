from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
from telegram import ReplyKeyboardMarkup
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext

updater = Updater("YourTelegramBotApi",
                  use_context=True)
USER_DATA = {}

# States for ConversationHandler
SELECT_DEPARTMENT, SELECT_SEMESTER, SELECT_CATEGORY, SELECT_SUBJECT = range(4)

DATA = {
    "IT": {
        "sem 1": {
            "textbook": {
                "CSDF":
                "BQACAgUAAxkBAAEV7oRnh9QHMh2mcoxoa3E2fQAB2WimuUAAArkYAAJ9V0FUVYsgF4j9Eeg2BA",  # Telegram file_id
                "CDCT":
                "BQACAgUAAxkBAAEV7oZnh9QbJBl1zl-MsgrX0Q3pDM5ukAACuhgAAn1XQVTzrRNylM2QfDYE",
                "FOB":
                "BQACAgUAAxkBAAEV7ohnh9Qtkx0BN9Rjk8yKF-7JyHTBWwACuxgAAn1XQVTIdCRc20lhZjYE",
                "SD":
                "BQACAgUAAxkBAAEV7opnh9Q-tmi5yByzMMBMMdN1y2kBmgACvBgAAn1XQVS1gwXaHkHKLTYE",
            },
            "syllabus": {
                "sub1": "https://example.com/it_sem1_sub1_syllabus",
                "sub2": "https://example.com/it_sem1_sub2_syllabus",
            },
            "timetable": "https://example.com/it_sem1_timetable",
        },
        "sem 2": {
            "textbook": {
                "sub1": "https://example.com/it_sem2_sub1_textbook",
                "sub2": "https://example.com/it_sem2_sub2_textbook",
            },
            "syllabus": {
                "sub1": "https://example.com/it_sem2_sub1_syllabus",
                "sub2": "https://example.com/it_sem2_sub2_syllabus",
            },
            "timetable": "https://example.com/it_sem2_timetable",
        },
        "sem 3": {
            "textbook": {
                "sub1": "https://example.com/it_sem3_sub1_textbook",
                "sub2": "https://example.com/it_sem3_sub2_textbook",
            },
            "syllabus": {
                "sub1": "https://example.com/it_sem3_sub1_syllabus",
                "sub2": "https://example.com/it_sem3_sub2_syllabus",
            },
            "timetable": "https://example.com/it_sem3_timetable",
        },
        "sem 4": {
            "textbook": {
                "sub1": "https://example.com/it_sem4_sub4_textbook",
                "sub2": "https://example.com/it_sem4_sub4_textbook",
            },
            "syllabus": {
                "sub1": "https://example.com/it_sem4_sub1_syllabus",
                "sub2": "https://example.com/it_sem4_sub2_syllabus",
            },
            "timetable": "https://example.com/it_sem4_timetable",
        },
        "sem 5": {
            "textbook": {
                "sub1": "https://example.com/it_sem5_sub1_textbook",
                "sub2": "https://example.com/it_sem5_sub2_textbook",
            },
            "syllabus": {
                "sub1": "https://example.com/it_sem5_sub1_syllabus",
                "sub2": "https://example.com/it_sem5_sub2_syllabus",
            },
            "timetable": "https://example.com/it_sem5_timetable",
        },
        "sem 6": {
            "textbook": {
                "CSDF":
                "BQACAgUAAxkBAAEW71poCfW6Y4BPvhMLmTBw4PkNvrTlhwAC0xYAAk4gUFRLiosN_wSEuTYE",  # Telegram file_id
                "CDCT":
                "BQACAgUAAxkBAAIBgWe_LnP_EUi6QP9S9olE_taezFumAALEFQAC5kb5VStZiOz_GgicNgQ",
                "FOB":
                "BQACAgUAAxkBAAIBhWe_Lqa88sCR4aR7m5KyEBAf5AtPAALGFQAC5kb5Vd8QmI5mEKi3NgQ",
                "SD": "",
            },
            "syllabus": {
                "CSDF":
                "BQACAgUAAxkBAAIBg2e_Log8Ba6lyBFAOTTTToW6jAWuAALFFQAC5kb5VRmyjIWRjW9rNgQ",  # Telegram file_id
                "CDCT":
                "BQACAgUAAxkBAAIBfWe_LlRxASjMmaMNmw5eiMYz_Mw4AALCFQAC5kb5VUVyo0xW-S4TNgQ",
                "FOB":
                "BQACAgUAAxkBAAIBe2e_Lkf3kiSyXHpo9O1QxATIqmpKAALBFQAC5kb5VSNDnXisXa7ONgQ",
                "SD":
                "BQACAgUAAxkBAAIBeWe_LjzAnKC_jwN7xULiu-okHRKvAALAFQAC5kb5VU1Mrh97SkNnNgQ",
            },
            "timetable":
            "BQACAgUAAxkBAAIBd2e_Lio18d8TjSq6Mw4RdV_mcR8qAAK_FQAC5kb5VfteZNsje6p9NgQ",
        },
    },
}

semesters = list(
    DATA["IT"].keys())  # This will give ["sem 1", "sem 2", ..., "sem 6"]


# Department selection
def initiate_department(update: Update, context: CallbackContext):
    keyboard = [["Mechanical", "IT", "Civil"], ["Cancel"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)
    update.message.reply_text("Please choose your department:",
                              reply_markup=reply_markup)
    return SELECT_DEPARTMENT


# Department selection handler
def select_department(update: Update, context: CallbackContext):
    department = update.message.text.upper()
    if department == "CANCEL":
        return cancel(update, context)

    USER_DATA[update.effective_user.id] = {"department": department}

    # Semester selection keyboard
    keyboard = [[semester for semester in semesters], ["Back"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)
    update.message.reply_text("Please select your semester:",
                              reply_markup=reply_markup)
    return SELECT_SEMESTER


# Semester selection handler
def select_semester(update: Update, context: CallbackContext):
    user_input = update.message.text

    if user_input == "Back":
        return initiate_department(update,
                                   context)  # Go back to department selection

    semester = user_input.split()[
        1]  # Extract semester number (e.g., "Semester 1")
    USER_DATA[update.effective_user.id]["semester"] = semester

    # Category selection keyboard
    keyboard = [["Timetable", "Textbook", "Syllabus"], ["Back"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)
    update.message.reply_text("Please select the category:",
                              reply_markup=reply_markup)
    return SELECT_CATEGORY


# Category selection handler
# Category selection handler
def select_category(update: Update, context: CallbackContext):
    category = update.message.text.lower()
    user_data = USER_DATA[update.effective_user.id]
    user_data["category"] = category
    department = user_data["department"]
    semester = user_data["semester"]

    if category == "back":
        # Go back to semester selection
        keyboard = [[semester for semester in semesters], ["Back"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,
                                           one_time_keyboard=True,
                                           resize_keyboard=True)
        update.message.reply_text("Please select your semester:",
                                  reply_markup=reply_markup)
        return SELECT_SEMESTER

    if category == "timetable":
        # Get timetable for the selected department and semester
        timetable = DATA[department][f"sem {semester}"]["timetable"]

        # Check if the timetable is a file ID or URL
        print(f"Timetable: {timetable}")

        # Send file or URL
        if timetable.startswith("BQAC"):  # If it's a file ID
            context.bot.send_document(chat_id=update.effective_chat.id,
                                      document=timetable)
        elif timetable.startswith("http"):  # If it's a URL
            update.message.reply_text(f"Here is the timetable: {timetable}")
        else:
            update.message.reply_text("Invalid timetable reference.")
        return SELECT_CATEGORY

    # Handle textbook or syllabus
    subjects_data = DATA[department][f"sem {semester}"].get(category, {})

    if not isinstance(subjects_data,
                      dict):  # Check if the category is not a dictionary
        update.message.reply_text(
            f"The selected category {category} does not contain subjects.")
        return SELECT_CATEGORY

    subjects = list(subjects_data.keys())  # Fetch subjects dynamically
    keyboard = [[subject] for subject in subjects] + [["Back"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)
    update.message.reply_text("Please select your subject:",
                              reply_markup=reply_markup)
    return SELECT_SUBJECT


def select_subject(update: Update, context: CallbackContext):
    subject = update.message.text
    user_data = USER_DATA[update.effective_user.id]
    department = user_data["department"]
    semester = user_data["semester"]
    category = user_data["category"]

    if subject.lower() == "back":
        # Go back to category selection (Timetable, Textbook, Syllabus)
        keyboard = [["Timetable", "Textbook", "Syllabus"], ["Back"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,
                                           one_time_keyboard=True,
                                           resize_keyboard=True)
        update.message.reply_text("Please select a category:",
                                  reply_markup=reply_markup)
        return SELECT_CATEGORY

    # Send the file corresponding to the category and subject
    send_file(category, subject, user_data, update, context)

    # After showing the subject details, ask if they need anything else
    keyboard = [["Timetable", "Textbook", "Syllabus"], ["Back"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)
    update.message.reply_text(
        "Is there anything else you need? 😊\nSelect another category or go back if you're done!",
        reply_markup=reply_markup,
    )
    return SELECT_CATEGORY


# Cancel handler
def cancel(update: Update, context: CallbackContext):
    update.message.reply_text("Operation canceled. Thank you!")
    return ConversationHandler.END


# Function to send files instead of links
def send_file(category, subject, user_data, update, context):
    department = user_data["department"]
    semester = user_data["semester"]

    subjects_data = DATA[department][f"sem {semester}"][category]
    file_data = (subjects_data.get(subject)
                 or subjects_data.get(subject.upper())
                 or subjects_data.get(subject.lower()))

    if not file_data:
        update.message.reply_text(
            f"Sorry, the file for {subject} is currently unavailable. Please try another subject."
        )
        return

    if file_data.startswith("BQAC"):  # Telegram file_id
        try:
            context.bot.send_document(chat_id=update.effective_chat.id,
                                      document=file_data)
        except Exception as e:
            update.message.reply_text(
                f"[Testing]An error occurred while sending the file: {str(e)}")
    elif file_data.startswith("http"):  # URL
        try:
            context.bot.send_document(chat_id=update.effective_chat.id,
                                      document=file_data)
        except Exception as e:
            update.message.reply_text(
                f"An error occurred while sending the file: {str(e)}")
    else:
        update.message.reply_text(
            "Invalid file reference. Please contact support.")


# Setup conversation handler
conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", initiate_department)],
    states={
        SELECT_DEPARTMENT:
        [MessageHandler(Filters.text & ~Filters.command, select_department)],
        SELECT_SEMESTER:
        [MessageHandler(Filters.text & ~Filters.command, select_semester)],
        SELECT_CATEGORY:
        [MessageHandler(Filters.text & ~Filters.command, select_category)],
        SELECT_SUBJECT:
        [MessageHandler(Filters.text & ~Filters.command, select_subject)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)

updater.dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()
