import pywhatkit as pw
txt = """Set a target date (next attempt or next exam).

Break subjects into chunks (weekly goals instead of cramming).

Use the Pomodoro method (25 min study + 5 min break).

Practice past papers — exams test patterns more than surprise.

End each day by quickly revising what you studied."""
pw.text_to_handwriting(txt,"demo1.png",[0,0,138])
print(" END ")

# import pywhatkit as pyw
# pyw.sendwhatmsg("+929269698122","Welcome",15,23)