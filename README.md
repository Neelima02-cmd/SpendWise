\# 💜 SpendWise — Personal Expense Tracker



SpendWise is a simple and user-friendly web application that helps users track their daily expenses, manage their budget, and receive automatic alerts when their spending approaches or exceeds their budget.



\## 🎯 Problem Statement



Many people find it difficult to keep track of their daily spending and stay within a fixed budget. SpendWise provides a simple digital solution to record expenses, organize them by category, monitor total spending, and receive budget alerts.



\## ✨ Features



\- 👤 User registration and login

\- 🔐 Secure user authentication

\- 💰 Add and manage personal expenses

\- 🏷️ Categorize expenses

\- 📊 Track total spending

\- 🎯 Set a custom personal budget

\- 🚦 Automatic budget status alerts

\- 🟢 Safe spending notification

\- 🟠 Near-budget warning

\- 🔴 Over-budget alert

\- 🗑️ Delete expenses

\- 👥 Each user can access only their own expenses

\- 📱 Responsive and user-friendly interface



\## 🚦 Budget Alert System



SpendWise automatically calculates the percentage of the budget used.



| Budget Usage | Status |

|---|---|

| Below 80% | 🟢 Safe |

| 80% – 99% | 🟠 Near Budget |

| 100% or above | 🔴 Over Budget |



\## 🛠️ Technologies Used



\- \*\*Frontend:\*\* HTML, CSS, Bootstrap 5

\- \*\*Backend:\*\* Python, Django

\- \*\*Database:\*\* SQLite

\- \*\*Authentication:\*\* Django Authentication

\- \*\*Version Control:\*\* Git \& GitHub



\## 📂 Project Structure



```text

SpendWise/

│

├── config/

│   ├── settings.py

│   ├── urls.py

│   ├── asgi.py

│   └── wsgi.py

│

├── expenses/

│   ├── migrations/

│   ├── templates/

│   │   └── expenses/

│   ├── models.py

│   ├── views.py

│   └── tests.py

│

├── manage.py

├── requirements.txt

├── .gitignore

└── README.md

