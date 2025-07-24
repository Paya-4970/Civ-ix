📄 README.md

# 🗳️ Civix - Interactive Session Voting Platform

**Civix** is a Django-based platform that allows users to create and participate in interactive sessions, vote on decisions, and communicate through a simple message system.

## 📌 Features

- ✅ User Registration & Authentication (Login, Logout, Signup)
- 🎯 Create and manage **Scenarios** and **Sessions**
- 👤 Role assignment for session participants
- 🗳️ Vote on decision options within sessions
- 💬 Non-real-time messaging system between participants
- 🛡️ Access control (only main users can create sessions)

---

## 🚀 Getting Started

### 1. Clone the repository

```
git clone https://github.com/Paya-4970/civix.git
cd civix
2. Create a virtual environment

python -m venv env
source env/bin/activate      # On Windows: env\Scripts\activate
3. Install dependencies

pip install -r requirements.txt
4. Set up the database

python manage.py makemigrations
python manage.py migrate
5. Create a superuser

python manage.py createsuperuser
6. Run the server

python manage.py runserver
🗂️ Project Structure

✨ Usage Guide
Register or Login as a user.

If you're a main user, create scenarios and sessions.

Invite participants to join sessions.

Participants can send messages and cast votes.

View votes and decisions in session room.


🛠️ Built With
Python 3.12

Django 4.x

SQLite3 (default DB)

HTML/CSS (custom & optional Tailwind/Bootstrap)

Optional: Channels (for future real-time support)

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

👤 Author
Made with ❤️ by paya hatami
