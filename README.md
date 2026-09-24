# 🎂 Birthday Wisher

A Python automation project that automatically sends personalized birthday emails using **Python, SMTP, and GitHub Actions**.

The program checks the birthdays listed in `birthdays.csv` every day. If someone has a birthday on the current date, it randomly selects a letter template, personalizes it with their name, and sends the birthday email automatically.

## ✨ Features

* 📅 Checks birthdays automatically every day
* 🎲 Randomly selects one of three birthday letter templates
* ✉️ Sends personalized emails using Gmail SMTP
* ⚙️ Runs automatically through GitHub Actions
* 🔐 Uses GitHub Secrets to protect email credentials
* 🐍 Uses Python for the complete automation

## 🛠️ Technologies Used

* Python
* Pandas
* SMTP
* GitHub Actions
* GitHub Secrets
* CSV

## 📂 Project Structure

```text
scheduled-tasks/
│
├── .github/
│   └── workflows/
│       ├── scheduled.yml
│       └── test.yml
│
├── letter_templates/
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
│
├── birthdays.csv
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔄 How It Works

1. The GitHub Actions workflow runs the Python script automatically every day.
2. `main.py` gets the current date.
3. `birthdays.csv` is loaded using Pandas.
4. The program checks whether today's date matches a birthday.
5. If there is a match, one of the three letter templates is randomly selected.
6. `[NAME]` in the template is replaced with the person's name.
7. The personalized message is sent through Gmail SMTP.

## ⚙️ GitHub Actions

The project uses two workflows:

### `scheduled.yml`

Runs the Birthday Wisher automatically according to the configured cron schedule.

It can also be triggered manually using the **Run workflow** button.

### `test.yml`

Checks that:

* Required GitHub Secrets are configured
* Required project files exist
* Python syntax is valid
* The project setup is ready to run

## 🔐 Security

Email credentials are **not stored directly in the Python code**.

The project uses GitHub Secrets:

```text
MY_EMAIL
MY_PASSWORD
```

This keeps sensitive credentials outside the source code.

> Never commit your email password, App Password, or other sensitive credentials to GitHub.

## 📋 Birthday Data

Birthday information is stored in `birthdays.csv` using the following format:

```text
name,email,year,month,day
```

The program uses the `month` and `day` values to determine whether someone has a birthday today.



---

**Built with Python 🐍 and GitHub Actions ⚙️**
