## Overview

This is a **Movie Ticket Booking System**, a full-stack Django web application designed to facilitate browsing movies, selecting seats, and booking tickets. Built with Python, Django, and standard web technologies, 
it supports authentication, scheduling, payment handling, and a REST API for movie record creation.

## Database & Data

- The application uses **SQLite** (`db.sqlite3`) as its default database—ideal for development and testing.
- Database models include:
  - **accounts**: Users and roles (Admin, Theater Owner, Customer).
  - **movies**: Movie details (title, duration, description, poster, etc.).
  - **theaters**: Theater and screen information.
  - **bookings**: Booking records with showtime, seats, user info, and payment status.
  - **payments**: Transaction details tied to each booking.
  - **reviews**: User reviews and ratings for movies.
  - **dashboard**: Aggregated views/stats (if applicable).
- Sample or seed data (if any) can be loaded via fixtures or Django admin. (Add details if you have fixtures or from external APIs.)

## Project Structure

movie-ticket-booking/
├── accounts/ # User models, authentication, role management
├── bookings/ # Booking logic, showtimes, seat allocation
├── dashboard/ # Admin/theater dashboards and stats
├── movies/ # Movie management, REST API endpoints
├── theaters/ # Theater and screen schema
├── payments/ # Payment processing, gateway integration
├── reviews/ # Movie reviews and ratings functionality
├── media/ # Uploaded images (e.g., movie posters)
├── static/ # CSS, JS, images
├── templates/ # HTML templates
├── db.sqlite3 # Development database
├── manage.py # Django management script
├── requirements.txt # Python dependencies
└── README.md # Project overview and 

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













instructions
