# API Documentation - Tourism Management System

## Base URL
```
http://localhost:8000/api/
```

## Authentication
Currently, no authentication is required for the API endpoints.

---

## 1. Customers (`/api/customers/`)

### Model Fields
- `id` (AutoField, Primary Key)
- `name` (CharField, max_length=100)
- `email` (CharField, max_length=100)
- `phone` (CharField, max_length=20, optional)
- `identity_document` (CharField, max_length=50, optional)
- `nationality` (CharField, max_length=50, optional)

### Available Endpoints

#### List all customers
- **GET** `/api/customers/`
- **Response**: Array of customer objects

#### Create a new customer
- **POST** `/api/customers/`
- **Request Body**:
```json
{
    "name": "John Doe",
    "email": "john.doe@email.com",
    "phone": "+1234567890",
    "identity_document": "12345678",
    "nationality": "American"
}
```

#### Get a specific customer
- **GET** `/api/customers/{id}/`
- **Response**: Customer object

#### Update a customer
- **PUT** `/api/customers/{id}/`
- **PATCH** `/api/customers/{id}/`
- **Request Body**: Customer fields to update

#### Delete a customer
- **DELETE** `/api/customers/{id}/`

---

## 2. Tourist Sites (`/api/tourist-sites/`)

### Model Fields
- `id` (AutoField, Primary Key)
- `name` (CharField, max_length=100)
- `location` (CharField, max_length=150, optional)
- `site_type` (CharField, choices: 'natural', 'cultural', 'other')
- `description` (TextField, optional)

### Available Endpoints

#### List all tourist sites
- **GET** `/api/tourist-sites/`
- **Response**: Array of tourist site objects

#### Create a new tourist site
- **POST** `/api/tourist-sites/`
- **Request Body**:
```json
{
    "name": "Machu Picchu",
    "location": "Cusco, Peru",
    "site_type": "cultural",
    "description": "Ancient Incan citadel located in the Eastern Cordillera"
}
```

#### Get a specific tourist site
- **GET** `/api/tourist-sites/{id}/`
- **Response**: Tourist site object

#### Update a tourist site
- **PUT** `/api/tourist-sites/{id}/`
- **PATCH** `/api/tourist-sites/{id}/`
- **Request Body**: Tourist site fields to update

#### Delete a tourist site
- **DELETE** `/api/tourist-sites/{id}/`

---

## 3. Tour Plans (`/api/tour-plans/`)

### Model Fields
- `id` (AutoField, Primary Key)
- `name` (CharField, max_length=100)
- `description` (TextField, optional)
- `total_duration` (IntegerField, optional, in minutes)
- `price` (DecimalField, max_digits=10, decimal_places=2)
- `tourist_sites` (ManyToManyField through TourPlanTouristSite)

### Available Endpoints

#### List all tour plans
- **GET** `/api/tour-plans/`
- **Response**: Array of tour plan objects

#### Create a new tour plan
- **POST** `/api/tour-plans/`
- **Request Body**:
```json
{
    "name": "Cusco Adventure",
    "description": "3-day tour through Cusco and surrounding areas",
    "total_duration": 4320,
    "price": "299.99"
}
```

#### Get a specific tour plan
- **GET** `/api/tour-plans/{id}/`
- **Response**: Tour plan object

#### Update a tour plan
- **PUT** `/api/tour-plans/{id}/`
- **PATCH** `/api/tour-plans/{id}/`
- **Request Body**: Tour plan fields to update

#### Delete a tour plan
- **DELETE** `/api/tour-plans/{id}/`

---

## 4. Tour Plan Tourist Sites (`/api/tour-plan-sites/`)

### Model Fields
- `tour_plan` (ForeignKey to TourPlan)
- `tourist_site` (ForeignKey to TouristSite)
- `visit_order` (IntegerField)
- `stay_time` (IntegerField, optional, in minutes)

### Available Endpoints

#### List all tour plan-site relationships
- **GET** `/api/tour-plan-sites/`
- **Response**: Array of tour plan-site relationship objects

#### Create a new tour plan-site relationship
- **POST** `/api/tour-plan-sites/`
- **Request Body**:
```json
{
    "tour_plan": 1,
    "tourist_site": 2,
    "visit_order": 1,
    "stay_time": 120
}
```

#### Get a specific relationship
- **GET** `/api/tour-plan-sites/{id}/`
- **Response**: Tour plan-site relationship object

#### Update a relationship
- **PUT** `/api/tour-plan-sites/{id}/`
- **PATCH** `/api/tour-plan-sites/{id}/`
- **Request Body**: Relationship fields to update

#### Delete a relationship
- **DELETE** `/api/tour-plan-sites/{id}/`

---

## 5. Tour Requests (`/api/tour-requests/`)

### Model Fields
- `id` (AutoField, Primary Key)
- `customer` (ForeignKey to Customer)
- `tour_plan` (ForeignKey to TourPlan)
- `request_date` (DateField)
- `tour_date` (DateField)
- `people_count` (IntegerField)
- `notes` (TextField, optional)

### Available Endpoints

#### List all tour requests
- **GET** `/api/tour-requests/`
- **Response**: Array of tour request objects

#### Create a new tour request
- **POST** `/api/tour-requests/`
- **Request Body**:
```json
{
    "customer": 1,
    "tour_plan": 1,
    "request_date": "2025-06-11",
    "tour_date": "2025-07-15",
    "people_count": 4,
    "notes": "Family vacation with children"
}
```

#### Get a specific tour request
- **GET** `/api/tour-requests/{id}/`
- **Response**: Tour request object

#### Update a tour request
- **PUT** `/api/tour-requests/{id}/`
- **PATCH** `/api/tour-requests/{id}/`
- **Request Body**: Tour request fields to update

#### Delete a tour request
- **DELETE** `/api/tour-requests/{id}/`

---

## 6. Service Records (`/api/service-records/`)

### Model Fields
- `id` (AutoField, Primary Key)
- `tour_request` (ForeignKey to TourRequest)
- `status` (CharField, choices: 'confirmed', 'cancelled', 'completed')
- `record_date` (DateField)
- `comments` (TextField, optional)

### Available Endpoints

#### List all service records
- **GET** `/api/service-records/`
- **Response**: Array of service record objects

#### Create a new service record
- **POST** `/api/service-records/`
- **Request Body**:
```json
{
    "tour_request": 1,
    "status": "confirmed",
    "record_date": "2025-06-11",
    "comments": "Tour confirmed, payment received"
}
```

#### Get a specific service record
- **GET** `/api/service-records/{id}/`
- **Response**: Service record object

#### Update a service record
- **PUT** `/api/service-records/{id}/`
- **PATCH** `/api/service-records/{id}/`
- **Request Body**: Service record fields to update

#### Delete a service record
- **DELETE** `/api/service-records/{id}/`

---

## Standard HTTP Response Codes

- **200 OK**: Successful GET, PUT, PATCH requests
- **201 Created**: Successful POST requests
- **204 No Content**: Successful DELETE requests
- **400 Bad Request**: Invalid request data
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server error

## Data Formats

### Date Fields
All date fields should be provided in ISO 8601 format: `YYYY-MM-DD`

### Decimal Fields
Price fields should be provided as strings with up to 2 decimal places: `"299.99"`

### Foreign Key References
When creating or updating records with foreign key relationships, provide the ID of the referenced object as an integer.

---

## Additional Notes

1. All endpoints support standard DRF filtering, ordering, and pagination parameters.
2. The API uses Django REST Framework's `ModelViewSet`, which provides full CRUD functionality.
3. All endpoints return JSON responses.
4. The API follows RESTful conventions for URL structure and HTTP methods.

## Admin Interface
Django admin interface is available at: `http://localhost:8000/admin/`

---

*Generated on: June 11, 2025*
