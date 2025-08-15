# 🎬 Movie Ticket Booking System

## 📌 Overview
The **Movie Ticket Booking System** is a full-stack Django web application that allows users to browse movies, select seats, and securely book tickets.  
It includes authentication, scheduling, payment gateway integration, and a REST API for movie record creation.  
Designed for Admins, Theater Owners, and Customers with role-based access.

---

## 🗄️ Database & Data
- **Database:** SQLite (`db.sqlite3`) is used for development and testing.
- **Models include:**
  - **accounts** – Users and roles (Admin, Theater Owner, Customer).
  - **movies** – Movie details (title, description, genre, language, poster).
  - **theaters** – Theater and screen information.
  - **bookings** – Showtimes, seat allocation, booking details.
  - **payments** – Stripe payment transactions linked to bookings.
  - **reviews** – User reviews and ratings for movies.
- **Data Source:**
  - Initially populated via Django Admin.
  - Optionally load fixtures or external APIs for movie data.

---

## 📂 Project Structure
```plaintext
movie-ticket-booking/
├── accounts/           # User models, authentication, role management
├── bookings/           # Booking logic, showtimes, seat allocation
├── dashboard/          # Admin/theater dashboards and stats
├── movies/             # Movie management, REST API endpoints
├── theaters/           # Theater and screen schema
├── payments/           # Payment processing, gateway integration
├── reviews/            # Movie reviews and ratings functionality
├── media/              # Uploaded images (e.g., movie posters)
├── static/             # CSS, JS, images
├── templates/          # HTML templates
├── db.sqlite3          # Development database
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
└── README.md           # Project overview and instructions


### 4. **Setup & Run Instructions**

A step-by-step guide on running the project locally:
## Setup & Run

Follow these steps to get the project running:

1. **Clone the repository**  
   ```bash
   git clone https://github.com/popkowshik/movie-ticket-booking.git
   cd movie-ticket-booking

2. **Create & activate a virtual environment**
python3 -m venv venv
source venv/bin/activate      # Linux & macOS
venv\Scripts\activate         # Windows

3. **Install dependencies**
pip install -r requirements.txt

4. **Apply Migrations** 
python manage.py migrate

5. **Run the development server**
python manage.py runserver


### 5. **Usage**

Guide users on how to navigate features of the app:
```markdown
## Usage

- **User accounts**  
  - Admins: Access dashboards, manage movies, theaters, and bookings.  
  - Theater Owners: Schedule shows, manage theaters/screens.  
  - Customers: Browse movies, select seats, book tickets, view booking history.

- **Booking flow**  
  1. Browse available movies and select a showtime.  
  2. Choose your seats on a seat map.  
  3. Proceed to payment gateway (e.g., Stripe).  
  4. Upon success, receive booking confirmation and booking ID.

- **API endpoints**  
  - `POST /api/movies/`: Create new movie records (provide example payload).  
  - Add more API endpoints as relevant.

- **Admin Interface**  
  - Visit `/admin/` to manage all models (requires admin credentials).

Technologies Used

Backend: Python, Django

Frontend: HTML5, CSS, JavaScript

Database: SQLite

Payments: Stripe API

Other: Django REST Framework


