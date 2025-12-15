import os
from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message

app = Flask(__name__)

# SECRET KEY FOR FLASH MESSAGES
app.secret_key = "supersecretkey123"

# ------------------------------
# EMAIL CONFIGURATION (GMAIL)
# ------------------------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'umamco2016@gmail.com'       # your Gmail
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")           # REMOVE SPACES
app.config['MAIL_DEFAULT_SENDER'] = 'umamco2016@gmail.com' # must match Gmail account

mail = Mail(app)

# ------------------------------
# ROUTES
# ------------------------------

@app.route("/")
def home():
    return render_template("index.html", title="Home | Amin Umar")

@app.route("/about")
def about():
    return render_template("about.html", title="About | Amin Umar")

@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projects | Amin Umar")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message_text = request.form.get("message")

        # Create the email message
        msg = Message(
            subject=f"Portfolio Contact: New message from {name}",
            recipients=["umamco2026@gmail.com"],  # your receiving email
            body=f"Sender Name: {name}\nEmail: {email}\n\nMessage:\n{message_text}"
        )

        # Send the email
        mail.send(msg)

        # Flash success message
        flash("Your message has been sent successfully!", "success")

    return render_template("contact.html", title="Contact | Amin Umar")

# ------------------------------
# RUN THE SERVER
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)
